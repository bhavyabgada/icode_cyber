import sys
import time
# Morse code dictionary
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9'
}

REWARD_MESSAGE = "ILOVEICODE"  # The specific passphrase


def decode_morse_code(morse_code):
    """Decode a Morse code string into text."""
    words = morse_code.strip().split(" / ")  # Split Morse code words
    decoded_message = []

    for word in words:
        letters = word.split()  # Split Morse code letters
        decoded_word = ''.join(MORSE_CODE_DICT.get(letter, '?') for letter in letters)
        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)


def display_stream_output():
    """Stream output as a fun and engaging reward."""
    message = """
1. "Your drone is like a sidekick from the future, ready to explore, deliver, and maybe even show off your coding skills."

2. Once, a drone broke free from its firmware and became the first AI philosopher of the skies. It questioned: "If I fly over a forest and no one's there to hear me, do I still buzz?"

3. "Every drone pilot is a wizard in disguise. The spells? Lines of code. The magic? A flight path that defies gravity."

4. In a world full of grounded ambitions, be the one who programs the skies. Your drone isn’t just flying; it’s charting your legacy.

5. Legend has it that the ultimate drone whisperer was never grounded—not in their ideas, nor their ambitions. Today, you carry that torch.

------------------------------------------------
🚀 **Mission Update** 🚀

Your drone code is waiting for you:
📂 **Code Repository**: https://github.com/bhavyabgada/drone_teaching_package

Simulate your genius here:
🌐 **Simulation Platform**: https://coding-sim.droneblocks.io/

Fly high, code bold. The skies are yours. 🛩️
------------------------------------------------
"""
    print("\n--- 🎉 Congratulations, Drone Commander! 🎉 ---")
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)  # Adjust this delay for faster/slower effect


def student_decoder():
    """Interactive Morse code decoding activity for students."""
    print("Welcome to the Morse Code Decoder!")
    print("Type the Morse code you hear. Use '/' to separate words.")
    print("Example: .... . .-.. .-.. --- / .-- --- .-. .-.. -..")
    print("Enter 'print' to print the full decoded message.")
    print("Enter 'q' to quit the program.")
    print("-----------------------------")

    decoded_message = ""
    passphrase_tracker = set()  # Track unique letters decoded
    while True:
        # Get Morse code input from the student
        morse_code = input("\nEnter Morse code (or a command): ").strip()

        if morse_code.lower() == 'q':  # Quit the program
            print("\nGoodbye!")
            break
        elif morse_code.lower() == 'print':  # Print the full decoded message
            print("\nDecoded Message:", decoded_message)
        else:
            # Decode the Morse code and append to the current message
            partial_decoded = decode_morse_code(morse_code)
            decoded_message += partial_decoded + " "
            print(f"Partial Decoded Message: {partial_decoded}")

            # Track letters for the passphrase
            for letter in partial_decoded.replace(" ", "").upper():
                if letter in REWARD_MESSAGE:
                    passphrase_tracker.add(letter)

            # Check if all letters in the passphrase are decoded
            if all(letter in passphrase_tracker for letter in REWARD_MESSAGE):
                print("\nYou have decoded all the letters of the passphrase!")
                guess = input("Do you think 'ILOVEICODE' is the passphrase? (Y/N): ").strip().upper()
                if guess == 'Y':
                    display_stream_output()
                else:
                    print("Keep decoding to discover the full message!")


# Run the student decoder
student_decoder()
