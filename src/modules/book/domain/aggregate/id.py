from pydantic import PositiveInt

from src.core.snowflake import seq


class BookId(PositiveInt):
    gt = 1

    @staticmethod
    def next_id() -> "BookId":
        return BookId(seq.__next__())
