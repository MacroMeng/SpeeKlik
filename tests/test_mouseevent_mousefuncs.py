import mouse_event


def test_can_do_run_all():
    checker = []
    m = mouse_event.MouseEvents(
        [
            mouse_event.MouseClick(100, 800, 0),
            mouse_event.MouseClick(1200, 50, 0.6),
            mouse_event.MouseClick(1020, 80, 1.2)
        ]
    )

    def appender(mc):
        checker.append((mc.x, mc.y, mc.delay))

    m.run_all(appender)

    assert checker == [(100, 800, 0), (1200, 50, 0.6), (1020, 80, 1.2)]
