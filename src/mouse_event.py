from collections.abc import Callable


Pos = tuple[int, int]


class MouseEvents:
    def __init__(self, events: list[Pos] | None = None):
        if events is None:
            self.events = []
        self.events = events

    def add_pos(self, pos: Pos):
        self.events.append(pos)

    def run_all(self, caller: Callable[[Pos], None]):
        for event in self.events:
            caller(event)
