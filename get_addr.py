import pyautogui

last_pos = pyautogui.position()
try:
    while True:
        new_pos = pyautogui.position()
        if last_pos != new_pos:
            print(new_pos)
            last_pos = new_pos
except KeyboardInterrupt:
    print('\nexit.')