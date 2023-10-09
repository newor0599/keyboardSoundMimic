from pynput import keyboard
import pygame 
file_path = "main.mp3"
volume = 100
print("A keyboard sound mimic application made by newor0599 from github.com")
print("https://github.com/newor0599")
pygame.mixer.init()
pygame.mixer.music.load(file_path)
pygame.mixer.music.set_volume(int(volume)/100)
def play_sound():
    pygame.mixer.music.play()

pressed_keys = set()

def on_press(key):
    if key and key not in pressed_keys:
        pressed_keys.add(key)
        play_sound()
def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)
def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
main()