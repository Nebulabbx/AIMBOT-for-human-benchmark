
import time
import numpy as np
import mss
import win32api
import win32con

# Screen region to scan (CHANGE THIS)
SCAN_REGION = {
    'top': 300, 'left': 454, 'width': 1500, 'height': 800
}

# Target color (BGR, NOT RGB)
TARGET_COLOR = np.array([232, 195, 149])
TOLERANCE = 1

CLICK_DELAY = 0.01 # seconds between clicks
LOOP_DELAY = 0.001  # main loop delay

sct = mss.mss()

def left_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def grab_screen():
    img = sct.grab(SCAN_REGION)
    frame = np.array(img)[:, :, :3]  # BGRA -> BGR
    return frame

def find_color(frame, target, tol):
    lower = np.clip(target - tol, 0, 255)
    upper = np.clip(target + tol, 0, 255)

    color_mask = np.all((frame >= lower) & (frame <= upper), axis=2)
    non_white_mask = (np.max(frame, axis=2) - np.min(frame, axis=2)) > 25

    mask = color_mask & non_white_mask

    if np.any(mask):
        y, x = np.where(mask)
        return x[0], y[0]

    return None


print("Aimbot running...")
print("Press CTRL+C to stop") #Too lazy to add a toggle and kill switch

while True:
    frame = grab_screen()
    pos = find_color(frame, TARGET_COLOR, TOLERANCE)

    if pos:
        x, y = pos
        screen_x = SCAN_REGION["left"] + x
        screen_y = SCAN_REGION["top"] + y

        left_click(screen_x, screen_y)
        time.sleep(CLICK_DELAY)

    time.sleep(LOOP_DELAY)

