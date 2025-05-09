# Keyboard Sound App

A Python-based application that plays custom sounds when keys are pressed. The app is designed to run in the background, allowing you to hear sound effects while performing other tasks on your computer.

---

## Features

- **Custom Key-to-Sound Mapping**: Map specific keys to custom sound files.
- **Default Sound Playback**: Play a default sound for keys not explicitly mapped.
- **Daemon Mode**: Run the application in the background as a daemon process.
- **Interactive Key Mapping**: Easily modify key-to-sound mappings using a configuration file.
- **Support for Multiple Sound Formats**: Works with `.wav` files.

---

## How It Works

1. **Key Mapping**:
   - The app uses a `sounds_config.json` file to map keys to specific `.wav` sound files.
   - For example:
     ```json
     {
         "a": "click_a.wav",
         "b": "click_b.wav",
         "default": "default_click.wav"
     }
     ```

2. **Sound Playback**:
   - When a key is pressed, the app checks the mapping in `sounds_config.json` and plays the corresponding sound using `pygame`.
   - If the key is not mapped, the app plays the `default_click.wav` sound.

3. **Daemon Mode**:
   - The app can run as a background process using the `keyboard_sound_daemon.py` script, allowing it to run without blocking your terminal.

4. **Keyboard Listener**:
   - The app uses the `keyboard` library to listen for keypress events.

---

## Installation

### Prerequisites

1. **Python 3.8 or newer**: Ensure Python is installed on your system.
2. **Dependencies**:
   - Install the required Python libraries:
     ```bash
     pip install pygame keyboard python-daemon
     ```

### Clone the Repository

1. Clone the project in your GitHub Codespace or local machine:
   ```bash
   git clone https://github.com/Failure10/Plague7.git
   cd Plague7
   ```

2. Ensure the `sounds` directory contains your `.wav` sound files:
   ```
   Plague7/
   ├── sounds/
   │   ├── click_a.wav
   │   ├── click_b.wav
   │   ├── default_click.wav
   ├── keyboard_sound_app.py
   ├── keyboard_sound_daemon.py
   ├── sounds_config.json
   └── README.md
   ```

---

## Usage

### Run the App Normally

To run the app and listen for keypresses:
```bash
python keyboard_sound_app.py
```

The app will remain active in the terminal, playing sounds when keys are pressed. Press `ESC` to exit.

---

### Run the App as a Daemon (Background Mode)

To run the app as a background process:
```bash
python keyboard_sound_daemon.py
```

1. **Verify the Process**:
   - Run `ps aux | grep python` to check if the script is running.
   - You should see `keyboard_sound_daemon.py` in the process list.

2. **Stop the Process**:
   - Find the Process ID (PID) using:
     ```bash
     ps aux | grep keyboard_sound_daemon.py
     ```
   - Kill the process using:
     ```bash
     kill <PID>
     ```

---

### Modify Key-to-Sound Mappings

1. Open `sounds_config.json` in a text editor.
2. Add, remove, or change key mappings. For example:
   ```json
   {
       "a": "click_a.wav",
       "space": "space_sound.wav",
       "enter": "enter_sound.wav",
       "default": "default_click.wav"
   }
   ```
3. Save the file and restart the app to apply changes.

---

## Customization

### Volume Control
To adjust the volume, modify the `set_volume` value in the script. For example:
```python
sound.set_volume(0.5)  # Set volume to 50%
```

---

## Troubleshooting

### Common Issues

1. **Sound File Not Found**:
   - Ensure the `.wav` file exists in the `sounds` directory.
   - Check that the file name in `sounds_config.json` matches exactly.

2. **No Sound Playback**:
   - Verify that you have installed `pygame` correctly.
   - Ensure your audio system is properly configured (e.g., `SDL_AUDIODRIVER` in Codespaces).

3. **Daemon Not Starting**:
   - Check for errors in the `daemon_stdout.log` or `daemon_stderr.log` files.

---

## Contributing

Contributions are welcome! If you’d like to add features or fix bugs, feel free to submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

## donations 

Donations are accepted! My PayPal is sjcrambl@hotmail.com
