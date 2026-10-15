# Word Quest 🚀
### A Kannada-Supported English Vocabulary and Speaking Tutor

Word Quest is an interactive learning application designed to help children practise English vocabulary with Kannada-language support. Learners see a word alongside an emoji, Kannada meaning, and transliteration, hear the English word spoken aloud, and then say the word into a microphone.

The application provides immediate feedback, retries, word skipping, progress tracking, and a score for each chapter.

## Preview

The Version 1 interface presents each vocabulary item visually. For example, the **sun** card displays an emoji, the English word, its Kannada meaning (**ಸೂರ್ಯ**) and transliteration. After the word is recognised, the interface shows a completed state.

## Features

- **Chapter-wise learning:** Choose a unit and practise its vocabulary.
- **Visual vocabulary cards:** Display the English word, an emoji, Kannada meaning, and transliteration.
- **Text-to-speech:** Hear each English word before attempting to say it.
- **Speech recognition:** Capture the learner's spoken response through the browser.
- **Automatic answer checking:** Compare recognised speech with the target word.
- **Retry support:** Automatically retries an unrecognised or incorrect response, with up to three attempts per word.
- **Skip control:** Move to the next word when needed.
- **Progress and scoring:** Show the current word position, score, and final chapter score.
- **Positive reinforcement:** Celebrate correct responses with a confetti animation.

## Technology Stack

| Technology | Role |
|---|---|
| Python | Application logic and vocabulary loading |
| Streamlit | Main web application and chapter selector |
| HTML and CSS | Embedded learning interface and visual styling |
| JavaScript | Speech interaction, answer checking, retries, progress, and scoring |
| Browser Web Speech API | Text-to-speech and speech recognition |
| JSON | Chapter-wise vocabulary, Kannada meanings, transliterations, and emojis |
| Tailwind CSS CDN | Interface styling |
| Canvas Confetti | Correct-answer celebration |

**Browser compatibility:** Speech recognition depends on browser support and microphone permissions. The interface also loads styling and confetti libraries from external CDNs, so an internet connection is required for those resources.

## Project Structure

```text
Smart_Tutor_0.1-main/
├── Chapterwisewordslist.json   # Chapter-wise vocabulary data
├── Tutor (1).py                # Main Streamlit application
├── TEST_CODE.py                # Alternative/test implementation
├── TEST_CODE.txt               # Text copy of the alternative implementation
└── const_wordList.txt          # Additional vocabulary list
```

The main application is `Tutor (1).py`, which loads `Chapterwisewordslist.json`.

## Vocabulary Units

The supplied vocabulary file contains these 10 units:

1. Unit 1 — Health is Happiness
2. Unit 2 — People Around Me
3. Unit 3 — Just Being Kind
4. Unit 4 — Krishna and Sudama
5. Unit 5 — Flowers in the Sky
6. Unit 6 — A Day Out
7. Unit 7 — Life Then and Now
8. Unit 8 — Travel Around
9. Unit 9 — People Who Help Us
10. Unit 10 — Enjoy Yourself

Each vocabulary entry uses these fields:

| Field | Description |
|---|---|
| `english` | Target English word |
| `kannada` | Kannada meaning |
| `kannada_transliteration` | Transliteration for pronunciation support |
| `emoji` | Visual cue associated with the word |

Example entry:

```json
{
  "english": "sun",
  "kannada": "ಸೂರ್ಯ",
  "kannada_transliteration": "ಸನ್",
  "emoji": "☀️"
}
```

## Getting Started

### Prerequisites

- Python 3
- A modern browser with Web Speech API support (Chrome or Edge is a practical starting point)
- A working microphone
- Internet access for the external CSS and confetti resources, and for browser speech services where required

### 1. Extract the project

Extract `Smart_Tutor_0.1-main.zip` and open a terminal in the extracted project directory.

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the Python dependency

```bash
python -m pip install streamlit
```

The main script uses Streamlit and Python's built-in `json` module. The learning interface uses JavaScript in the browser.

### 4. Make the vocabulary path portable

The current `Tutor (1).py` file contains an absolute Windows path to `Chapterwisewordslist.json`. It will not work on another machine until that path is updated.

In `Tutor (1).py`, replace the existing `JSON_PATH` assignment and file-opening block with:

```python
from pathlib import Path

JSON_PATH = Path(__file__).with_name("Chapterwisewordslist.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    word_data = json.load(f)
```

Keep `import json` at the top of the file. Place `Chapterwisewordslist.json` in the same directory as `Tutor (1).py`.

### 5. Run the application

```bash
streamlit run "Tutor (1).py"
```

Open the local URL shown in the terminal. Streamlit commonly uses:

```text
http://localhost:8501
```

## How to Use

1. Launch the application.
2. Choose a unit from **Choose a Chapter**.
3. Select **Start Chapter**.
4. Review the displayed emoji, English word, Kannada meaning, and transliteration.
5. Listen as the application speaks the English word.
6. Allow microphone access and say the word clearly when prompted.
7. If the recognised text matches the target word, the score increases and the app moves to the next word.
8. Use **Retry** to repeat the current word or **Skip** to move on.
9. At the end of the unit, review the chapter-completion message and score.

## How It Works

The diagram below illustrates how the learner, vocabulary data, Streamlit application, and browser speech features work together.

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/3feb3174-0e8b-4837-925f-2277f80381c1" />


## Troubleshooting

**The application cannot find the JSON file**
- Confirm that `Chapterwisewordslist.json` is in the same directory as `Tutor (1).py`.
- Apply the relative-path fix in the setup section.

**The microphone or speech recognition does not work**
- Use a browser that supports speech recognition.
- Allow microphone access in the browser.
- Check the system microphone and browser site permissions.
- Try a current version of Chrome or Edge.
- Speech recognition behaviour may vary by browser, operating system, and network.

**A spoken word is marked incorrect**
- Speak clearly and wait for the listening prompt.
- Reduce background noise and try again.
- The current implementation compares recognised text with the target word. It does **not** perform phoneme-level pronunciation assessment, so speech recognition errors can affect results.

**The styling or celebration animation does not load**
- Check the internet connection because Tailwind CSS and Canvas Confetti are loaded from CDNs.
- Refresh the application after checking the connection.

## Future Improvements

- Add persistent learner profiles, saved progress, and chapter history.
- Provide more detailed pronunciation feedback and phoneme-level evaluation.
- Add a dedicated microphone/listening indicator and controls to replay audio.
- Let learners revisit missed words and practise them separately.
- Add configurable speech speed and accessibility options.
- Validate vocabulary data and provide clearer errors for missing or malformed entries.
- Add automated tests and a `requirements.txt` file for reproducible setup.
- Expand vocabulary and add more languages or learning levels.
