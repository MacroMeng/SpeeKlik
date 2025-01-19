import pyautogui as pag


if __name__ == "__main__":
    while True:
        print(pag.position(), end="\r", flush=True)
