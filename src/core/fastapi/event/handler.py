import inspect
from contextvars import ContextVar
from typing import Dict, NoReturn, Optional, Type, Union

import anyio
from pydantic import BaseModel

from src.common.protocols.event import BaseEvent
from src.core.fastapi.event.exception import (
    EmptyContextException,
    InvalidEventTypeException,
    InvalidParameterTypeException,
    ParameterCountException,
    RequiredParameterException,
)

_handler_context: ContextVar[Optional["EventHandler"]] = ContextVar(
    "_handler_context", default=None
)


class EventHandlerValidator:
    EVENT_PARAMETER_COUNT = 2

    async def validate(
        self, event: Type[BaseEvent], param: Optional[BaseModel] = None
    ) -> Optional[NoReturn]:
        if not issubclass(event, BaseEvent):
            raise InvalidEventTypeException

        if param and not isinstance(param, BaseModel):
            raise InvalidParameterTypeException

        signature = inspect.signature(event.handle)
        func_parameters = signature.parameters
        if len(func_parameters) != self.EVENT_PARAMETER_COUNT:
            raise ParameterCountException

        base_parameter = func_parameters.get("param")
        if base_parameter is not None and base_parameter.default is not None and not param:
            raise RequiredParameterException(
                cls_name=base_parameter.__class__.__name__,
            )
        return None


class EventHandler:
    def __init__(self, validator: EventHandlerValidator):
        self.events: Dict[BaseEvent, Union[BaseModel, None]] = {}
        self.validator = validator

    async def store(self, event: BaseEvent, param: BaseModel = None) -> None:
        await self.validator.validate(event=type(event), param=param)
        self.events[event] = param

    async def publish(self) -> None:
        await self._run()

        self.events.clear()

    async def _run(self) -> None:
        event: BaseEvent
        async with anyio.create_task_group() as task_group:
            for event, parameter in self.events.items():
                task_group.start_soon(event.handle, parameter)


class EventHandlerMeta(type):
    async def store(self, event: BaseEvent, param: BaseModel = None) -> None:
        handler = self._get_event_handler()
        await handler.store(event=event, param=param)

    async def publish(self) -> None:
        handler = self._get_event_handler()
        await handler.publish()

    def _get_event_handler(self) -> Union[EventHandler, NoReturn]:
        try:
            return _handler_context.get()
        except LookupError:
            raise EmptyContextException


class EventHandlerDelegator(metaclass=EventHandlerMeta):
    def __init__(self):
        self.token = None

    def __enter__(self):
        validator = EventHandlerValidator()
        self.token = _handler_context.set(EventHandler(validator=validator))
        return type(self)

    def __exit__(self, exc_type, exc_value, traceback):
        _handler_context.reset(self.token)


event_handler: Type[EventHandlerDelegator] = EventHandlerDelegator
