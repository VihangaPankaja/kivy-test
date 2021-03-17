import ctypes
from win32api import GetSystemMetrics

scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)

print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))
print(scaleFactor)

