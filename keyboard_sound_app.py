import os
import json
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
        print(f"Sound file {sound_path} not found!")

def main():
    """
    Main function to capture input from the terminal.
    """
    sound_mapping = load_sound_mapping()
    print("Keyboard sound app is running. Type keys to hear sounds!")
    print("Type 'exit' to quit.")

    while True:
        key = input("Key: ").strip()
        if key.lower() == "exit":
            print("Exiting program.")
            break
        play_sound(key, sound_mapping)

if __name__ == "__main__":
    main()
    