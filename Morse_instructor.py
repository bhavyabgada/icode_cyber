import pygame
import numpy as np
import time

# Initialize Pygame mixer for mono sound
pygame.mixer.init(frequency=44100, size=-16, channels=1)

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----'
}

# Parameters for generating sound
FREQ = 1000  # Frequency in Hz
SAMPLE_RATE = 44100  # Samples per second
AMPLITUDE = 32767  # Max amplitude for 16-bit audio


def generate_tone(frequency, duration):
    """Generate a sine wave tone."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    wave = AMPLITUDE * np.sin(2 * np.pi * frequency * t)
    return wave.astype(np.int16)  # 1D array for mono sound


def play_tone(frequency, duration):
    """Play a tone using Pygame."""
    sound_array = generate_tone(frequency, duration)
    sound = pygame.sndarray.make_sound(sound_array)
    sound.play()
    time.sleep(duration)  # Ensure sound plays for the specified duration


def play_morse_for_letter(letter):
    """Play the Morse code for a single letter."""
    morse = MORSE_CODE_DICT[letter.upper()]
    print(f"Playing Morse code for letter: {letter.upper()} ({morse})")
    for symbol in morse:
        if symbol == '.':
            play_tone(FREQ, 0.2)  # Dot sound (200ms)
        elif symbol == '-':
            play_tone(FREQ, 0.6)  # Dash sound (600ms)
        time.sleep(0.2)  # Pause between symbols


def morse_code_controller(message):
    """Control playback of Morse code letter by letter using text-based input."""
    letters = list(message.upper())
    index = 0

    print("\n--- Morse Code Controller ---")
    print("Enter '^[[C' to play the next letter (Right Arrow)")
    print("Enter '^[[D' to play the previous letter (Left Arrow)")
    print("Enter '^[[B' to repeat the current letter (Down Arrow)")
    print("Enter 'q' to quit.")
    print("-----------------------------")

    while True:
        # Display the current letter
        if 0 <= index < len(letters):
            print(f"Current letter: {letters[index]}")
        else:
            print("No letter to display (out of bounds).")

        # Get user input
        key = input("Enter your command: ").strip()
        print(f"Raw input received: {repr(key)}")  # Debugging: show raw input

        if key == '\x1b[C':  # Right arrow
            if index < len(letters) - 1:
                index += 1
                play_morse_for_letter(letters[index])
            else:
                print("Already at the last letter.")

        elif key == '\x1b[D':  # Left arrow
            if index > 0:
                index -= 1
                play_morse_for_letter(letters[index])
            else:
                print("Already at the first letter.")

        elif key == '\x1b[B':  # Down arrow
            if 0 <= index < len(letters):
                play_morse_for_letter(letters[index])
            else:
                print("No current letter to repeat.")

        elif key.lower() == 'q':  # Quit
            print("Exiting Morse code controller.")
            break

        else:
            print("Invalid input. Please use '^[[C', '^[[D', '^[[B', or 'q'.")


# Input message to play
message = input("Enter the message to play as Morse code: ")
print("Starting Morse code playback...")
morse_code_controller(message)
