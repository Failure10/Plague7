import os
import json
import keyboard
import pygame
import threading

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
        print(f"Sound file {sound_file} not found!")

def background_listener(sound_mapping):
    """
    Listen to keyboard events in the background.
    """
    print("Keyboard sound app is running in the background. Press keys to hear sounds!")
    print("Press ESC to exit.")

    for key in sound_mapping.keys():
        keyboard.on_press_key(key, lambda _, k=key: play_sound(k, sound_mapping))

    # Keep the listener running until 'esc' is pressed
    keyboard.wait("esc")
    print("Exiting program.")

def main():
    """
    Main function to launch the background listener.
    """
    # Load the key-to-sound mapping
    sound_mapping = load_sound_mapping()

    # Run the listener in a background thread
    listener_thread = threading.Thread(target=background_listener, args=(sound_mapping,))
    listener_thread.daemon = True  # Ensures the thread exits when the main program exits
    listener_thread.start()

    # Keep the main program alive
    while True:
        pass

if __name__ == "__main__":
    main()
    