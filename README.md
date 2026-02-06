first it has a screen region selector u can edit the resolution in it
if u dont know u can use this small code
"
import win32api, time

print("Move mouse to TOP-LEFT of target area (wait 3s)")
time.sleep(3)
x1, y1 = win32api.GetCursorPos()

print("Move mouse to BOTTOM-RIGHT of target area (wait 3s)")
time.sleep(3)
x2, y2 = win32api.GetCursorPos()

print("\nUSE THIS:")
print({
    "top": y1,
    "left": x1,
    "width": x2 - x1,
    "height": y2 - y1
})
"
also u can mess around with the tolarace of the program(it can add a bias that prevents the program from overfitting the value u are searching for)
