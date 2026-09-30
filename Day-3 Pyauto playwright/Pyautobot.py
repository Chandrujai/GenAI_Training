import pyautogui
import pyperclip
from openpyxl import Workbook, load_workbook
from pathlib import Path
from datetime import datetime
import time
import re


# =========================================================
# SETTINGS
# =========================================================

CITY = "Bengaluru"



# DESKTOP = Path.home() / "Desktop"

# EXCEL_FILE = DESKTOP / "weather_history.xlsx"
# DEBUG_FILE = DESKTOP / "accuweather_debug.txt"

EXCEL_FILE = "weather_history.xlsx"
EXCEL_FILE = Path(EXCEL_FILE)
if EXCEL_FILE.exists():
    workbook = load_workbook(EXCEL_FILE)
DEBUG_FILE = Path("accuweather_debug.txt")
if DEBUG_FILE.exists():
    workbook = load_workbook(DEBUG_FILE)
# =========================================================
# OPEN CHROME
# =========================================================

print("Opening Chrome...")

pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(4)


# =========================================================
# OPEN ACCUWEATHER
# =========================================================

print("Opening AccuWeather...")

pyautogui.hotkey("ctrl", "t")

pyautogui.write("https://www.accuweather.com/")

pyautogui.press("enter")

time.sleep(8)


# =========================================================
# FIND SEARCH BOX
# =========================================================

print("Finding search box...")

# Use browser find
pyautogui.hotkey("ctrl", "f")

time.sleep(2)

pyautogui.write("bengaluru")

time.sleep(2)

pyautogui.press("esc")

time.sleep(1)


# =========================================================
# CLICK SEARCH BOX
# =========================================================

# IMPORTANT:
# This coordinate may need adjustment depending
# on your screen.

pyautogui.click(500, 100)

time.sleep(1)

pyautogui.hotkey("ctrl", "a")

pyautogui.write(CITY)

time.sleep(3)

pyautogui.press("enter")

print(f"Searching for {CITY}...")

time.sleep(8)


# =========================================================
# COPY PAGE TEXT
# =========================================================

print("Copying webpage text...")

pyautogui.hotkey("ctrl", "a")

time.sleep(1)

pyautogui.hotkey("ctrl", "c")

time.sleep(2)

weather_text = pyperclip.paste()

match = re.search(r'\d+(?:\.\d+)?°C', weather_text)

if match:
    weather_text = match.group()


# =========================================================
# SAVE DEBUG TEXT
# =========================================================

with open(DEBUG_FILE, "w", encoding="utf-8") as file:

    file.write(weather_text)


# print()
# print("-----------------------------------------")
# print("DEBUG INFORMATION")
# print("-----------------------------------------")
# print(f"Text captured: {len(weather_text)} characters")
# print(f"Debug file: {DEBUG_FILE}")
# print("-----------------------------------------")


# # =========================================================
# # DISPLAY FIRST PART OF TEXT
# # =========================================================

# print()
# print("First 3000 characters:")
# print("-----------------------------------------")

# print(weather_text[:3000])

# print("-----------------------------------------")


# =========================================================
# SAVE TO EXCEL
# =========================================================

if EXCEL_FILE.exists():

    workbook = load_workbook(EXCEL_FILE)

    worksheet = workbook.active

else:

    workbook = Workbook()

    worksheet = workbook.active

    worksheet.title = "Weather History"

    worksheet.append([
        "Date",
        "Time",
        "City",
        "Weather Information"
    ])


# =========================================================
# APPEND WEATHER INFORMATION
# =========================================================

now = datetime.now()

worksheet.append([
    now.strftime("%Y-%m-%d"),
    now.strftime("%H:%M:%S"),
    CITY,
    weather_text
])


# =========================================================
# SAVE EXCEL
# =========================================================

workbook.save(EXCEL_FILE)

print()
print("-----------------------------------------")
print("Excel updated successfully")
print("-----------------------------------------")
print(f"File: {EXCEL_FILE}")
print("-----------------------------------------")


# =========================================================
# CLOSE CHROME
# =========================================================

time.sleep(2)

pyautogui.hotkey("ctrl", "w")

print()
print("Chrome closed.")
print("Program completed.")

