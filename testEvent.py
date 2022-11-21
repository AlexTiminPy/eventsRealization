from eventClass import Event

ev = Event()


def a():
    print("a")


def b():
    print("b")


def c():
    print("c")


assert len(ev.performers) == 0
ev += a
assert len(ev.performers) == 1
ev -= a
assert len(ev.performers) == 0
ev + a
ev - a
ev + a
ev += b
ev += c
assert len(ev.performers) == 3
ev.activate_next_with_clear()
assert len(ev.performers) == 2
ev.activate_all_with_clear()
assert len(ev.performers) == 0
