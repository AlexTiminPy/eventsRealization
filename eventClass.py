import copy
from collections.abc import Callable
from typing import NoReturn, Self, Union


class Event:
    """
    You must use callable object without any returned value
    The return value will be ignored

    Use "activate_next" if your next performer must be reused or
    "activate_next_with_clear" if your next performer single-used

    Use "activate_all" if your performers must be reused or
    "activate_all_with_clear" if your performers single-used
    """

    def __init__(self, start_performers: Union[Self, list] = None) -> Self:
        self.performers = []
        if start_performers is None:
            return
        if not self.validate_start_performers(start_performers=start_performers):
            return
        if isinstance(start_performers, Event):
            self.performers = copy.deepcopy(start_performers.performers)
        elif isinstance(start_performers, list):
            self.performers = copy.deepcopy(start_performers)

    @staticmethod
    def validate_start_performers(start_performers: list) -> bool:
        for perf in start_performers:
            if not callable(perf):
                return False
        return True

    def __add__(self, func: Callable) -> NoReturn:
        self.add_performer(func=func)

    def __iadd__(self, func: Callable) -> Self:
        self.add_performer(func=func)
        return self

    def __sub__(self, func: Callable) -> NoReturn:
        self.del_performer(func=func)

    def __isub__(self, func: Callable) -> Self:
        self.del_performer(func=func)
        return self

    def add_performer(self, func: Callable) -> NoReturn:
        if not callable(func):
            raise TypeError("attempt to add a non-functional object")
        self.performers.append(func)

    def del_performer(self, func: Callable) -> NoReturn:
        if func not in self.performers:
            raise NameError("no such object found")
        self.performers.remove(func)

    def activate_next(self) -> NoReturn:
        if not self.performers:
            raise IndexError("no performer found")
        self.performers[0]()

    def activate_next_with_clear(self) -> NoReturn:
        self.activate_next()
        self.performers.pop(0)

    def activate_all(self) -> NoReturn:
        if not self.performers:
            raise IndexError("no any performers found")
        for perf in self.performers:
            perf()

    def activate_all_with_clear(self) -> NoReturn:
        self.activate_all()
        self.performers = []
