from pynput import keyboard

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc: #esc key stops the program
        print("Exiting...")
        return False  

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
