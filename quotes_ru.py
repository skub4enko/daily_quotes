import ctypes
import datetime
import json
import random
from pathlib import Path

PHRASE_FILE = "quotes_ru.txt"
STATE_FILE = "phrase_state.json"
USED_PHRASES_FILE = "used_phrases.json"  # New file for used phrases


def load_phrases():
    with open(PHRASE_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    return [phrase.strip() for phrase in content.split("\n\n") if phrase.strip()]


def load_state():
    if Path(STATE_FILE).exists():
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f)


def load_used_phrases():
    if Path(USED_PHRASES_FILE).exists():
        with open(USED_PHRASES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_used_phrases(used_phrases):
    with open(USED_PHRASES_FILE, "w", encoding="utf-8") as f:
        json.dump(used_phrases, f)


def show_phrase(message):
    ctypes.windll.user32.MessageBoxW(0, message, "Phrase of the Day", 0x40)


def main():
    today = datetime.date.today().isoformat()
    phrases = load_phrases()
    state = load_state()
    used_phrases = load_used_phrases()

    # Filter phrases that have already been used
    available_phrases = [phrase for phrase in phrases if phrase not in used_phrases]

    # If there are no available phrases, clear the list of used phrases
    if not available_phrases:
        print("All phrases have been used. Resetting the used phrases list.")
        used_phrases = []  # Clear list of used phrases
        available_phrases = phrases  # All phrases are available again

    # We choose a random phrase
    phrase = random.choice(available_phrases)

    # Updating the state
    state = {"date": today, "phrase": phrase}
    save_state(state)

    # Add the used phrase to the list and save
    used_phrases.append(phrase)
    save_used_phrases(used_phrases)

    show_phrase(phrase)


if __name__ == "__main__":
    main()
