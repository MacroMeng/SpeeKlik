from collections.abc import Callable

Pos = tuple[int, int]


class MouseEvents:
    def __init__(self, events: list[Pos] | None = None):
        if events is None:
            events = []
        self.events = events

    def add_pos(self, pos: Pos):
        self.events.append(pos)

    def run_all(self, caller: Callable[[Pos], None]):
        for event in self.events:
            caller(event)

    def __repr__(self):
        key_lists_str = str(self.events)
        return f"{self.__class__.__name__}({key_lists_str})"

    def __str__(self):
        res = ";".join(f"({event[0]}, {event[1]})" for event in self.events)
        return res
