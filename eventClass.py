class Event:
    """
    you must use callable object without any returned value
    the return value will be ignored

    use "activate_next" if your next performer must be reused
    use "activate_next_with_clear" if your next performer single-used

    use "activate_all" if your performers must be reused
    use "activate_all_with_clear" if your performers single-used
    """

    def __init__(self):
        self.performers = []

    def __add__(self, func):
        self.add_event(func=func)

    def __iadd__(self, func):
        self.add_event(func=func)

    def __sub__(self, func):
        self.del_event(func=func)

    def __isub__(self, func):
        self.del_event(func=func)

    def add_event(self, func):
        if not callable(func):
            raise TypeError("attempt to add a non-functional object")
        self.performers.append(func)

    def del_event(self, func):
        if func not in self.performers:
            raise NameError("no such object found")
        self.performers.remove(func)

    def activate_next(self):
        if not self.performers:
            raise IndexError("no performer found")
        self.performers[0]()

    def activate_next_with_clear(self):
        if not self.performers:
            raise IndexError("no performer found")
        self.performers.pop(0)()

    def activate_all(self):
        if not self.performers:
            raise IndexError("no any performers found")
        for perf in self.performers:
            perf()

    def activate_all_with_clear(self):
        if not self.performers:
            raise IndexError("no any performers found")
        for perf in self.performers:
            perf()
        self.performers = []

