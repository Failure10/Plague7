import os
import json
import keyboard
import pygame
import daemon

# Initialize pygame mixer for playing sounds
pygame.mixer.init()

SOUND_DIRECTORY = "sounds"
CONFIG_FILE = "sounds_config.json"
DEFAULT_SOUND = "default_click.wav"

def load_sound_mapping():
    """
    Load the key-to-sound mapping from the configuration file.
    """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return {}

def play_sound(key, sound_mapping):
    """
    Play the sound associated with the key.
    If no sound is mapped, play the default sound.
    """
    sound_file = sound_mapping.get(key, DEFAULT_SOUND)
    sound_path = os.path.join(SOUND_DIRECTORY, sound_file)
    if os.path.exists(sound_path):
        pygame.mixer.Sound(sound_path).play()
    else:
        print(f"Sound file '{sound_file}' not found!")

def background_listener():
    """
    Listen to keyboard events and play sounds in the background.
    """
    sound_mapping = load_sound_mapping()
    print("Keyboard sound app is now running in the background.")
    for key in sound_mapping.keys():
        keyboard.on_press_key(key, lambda _, k=key: play_sound(k, sound_mapping))
    keyboard.wait("esc")

def run_daemon():
    """
    Run the background listener as a daemon process.
    """
    with daemon.DaemonContext():
        background_listener()

if __name__ == "__main__":
    run_daemon()pip install python-daemon