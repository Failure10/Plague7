import os
import json
from pynput import keyboard
import pygame

# Initialize pygame mixer for playing sounds
pygame.mixer.init()

# Directory where sound files are stored
SOUND_DIRECTORY = "sounds"

# Path to the sound configuration file
CONFIG_FILE = "sounds_config.json"

# Default sound for keys not mapped
DEFAULT_SOUND = "default_click.wav"

def load_sound_mapping():
    """
    Load the key-to-sound mapping from the configuration file.
    """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print(f"Error: {CONFIG_FILE} is not a valid JSON file.")
    else:
        print(f"Warning: {CONFIG_FILE} not found. Using default settings.")
    return {}

def play_sound(key, sound_mapping):
    """
    Play the sound associated with the key.
    If no sound is mapped, play the default sound.
    """
    try:
        sound_file = sound_mapping.get(key, DEFAULT_SOUND)
        sound_path = os.path.join(SOUND_DIRECTORY, sound_file)
        if os.path.exists(sound_path):
            pygame.mixer.Sound(sound_path).play()
        else:
            print(f"Sound file {sound_path} not found!")
    except Exception as e:
        print(f"Error playing sound: {e}")

def on_press(key, sound_mapping):
    """
    Called when a key is pressed.
    """
    try:
        if hasattr(key, 'char') and key.char is not None:
            play_sound(key.char, sound_mapping)
        elif hasattr(key, 'name'):
            play_sound(key.name, sound_mapping)
    except Exception as e:
        print(f"Error processing key: {e}")

def main():
    """
    Main function to start listening to keyboard events.
    """
    print("Keyboard sound app is running. Press keys to hear sounds!")
    print("Press ESC to exit.")
    
    # Ensure sound directory exists
    os.makedirs(SOUND_DIRECTORY, exist_ok=True)

    # Load the key-to-sound mapping
    sound_mapping = load_sound_mapping()

    # Listen for keyboard key presses
    with keyboard.Listener(on_press=lambda key: on_press(key, sound_mapping)) as listener:
        listener.join()

if __name__ == "__main__":
    main()