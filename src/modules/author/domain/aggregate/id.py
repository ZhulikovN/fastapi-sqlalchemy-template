from pydantic import PositiveInt

from src.core.snowflake import seq


class AuthorId(PositiveInt):
    gt = 1

    @staticmethod
    def next_id() -> "AuthorId":
        return seq.__next__()
