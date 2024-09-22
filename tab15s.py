import pyautogui
import time

def switch_tabs(interval=40):
    while True:
        pyautogui.hotkey('ctrl', 'tab')  # Switch to the next tab
        time.sleep(interval)  # Wait for the specified interval

if __name__ == "__main__":
    print("Starting tab switcher. Press Ctrl+C to stop.")
    switch_tabs()
        
