import sys
import time

import pyautogui as p

# def test_pos_get_move_to_RD():
#     print("move your mouse to RD.")
#     time.sleep(3)
#     assert p.position() == (p.size()[0]-1, p.size()[1]-1)


def test_can_move_mouse():
    p.PAUSE = 1e-100000
    p.FAILSAFE = False
    for i in range(p.size()[0]):
        for j in range(p.size()[1]):
            p.moveTo(i, j, duration=p.PAUSE)
    p.FAILSAFE = True
    p.PAUSE = 0.1
    assert p.position() == (p.size()[0]-1, p.size()[1]-1)
