f = open("song_path.txt","r")
file_path = f.read()
f.close()
f = open("volume.txt","r")
volume = f.read()
f.close()


from pynput import keyboard
import pygame
import os
print("A keyboard sound mimic application made by newor0599 from github.com")
print("https://github.com/newor0599")
def play_sound(sound_file):
    global volume
    pygame.init()
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(int(volume)/100)
    except pygame.error:
        os.system(f"msg * An error has occured, please check the sound file you imported")
        os.system("taskkill /im python.exe /t /f")

pressed_keys = set()

def on_press(key):
    try:
        if key.char and key.char not in pressed_keys:
            pressed_keys.add(key.char)
            play_sound(file_path)
    except AttributeError:
        ...
def on_release(key):
    try:
        if key.char in pressed_keys:
            pressed_keys.remove(key.char)
    except AttributeError:
        pass
def main():
    global keys
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
main()

