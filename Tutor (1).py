# streamlit run "D:\\Tutor (1).py"

import streamlit as st
import json
import streamlit.components.v1 as components

st.set_page_config(page_title="Word Quest", layout="centered")

JSON_PATH = r"C:\Users\Chethan H S\OneDrive\Desktop\Chapterwisewordslist.json"

with open(JSON_PATH, "r", encoding="utf-8") as f:
    word_data = json.load(f)

chapters = list(word_data.keys())


st.session_state.setdefault("chapter_index", 0)
st.session_state.setdefault("chapter_started", False)

st.markdown("""
<h1 style="
text-align:center;
font-weight:900;
background: linear-gradient(90deg,#2563EB,#22C55E);
-webkit-background-clip:text;
color:transparent;
font-size:48px;">
Word Quest 🌈
</h1>
<p style="text-align:center;color:#374151;font-size:18px;">
Listen • Speak • Learn
</p>
""", unsafe_allow_html=True)

selected_chapter = st.selectbox(
    "📘 Choose a Chapter",
    chapters,
    index=st.session_state.chapter_index
)

words = word_data[selected_chapter]

js_words = [
    {
        "word": w["english"].lower(),
        "emoji": w.get("emoji", "📘"),
        "kannada": w.get("kannada", ""),
        "translit": w.get("kannada_transliteration", "")
    }
    for w in words
]


if st.button("🚀 Start Chapter"):
    st.session_state.chapter_started = True

if st.session_state.chapter_started:

    html_code = f"""
<!DOCTYPE html>
<html>
<head>
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

<style>
body {{
    background: linear-gradient(135deg, #E0F2FE, #ECFDF5);
    font-family: system-ui;
}}
.card {{
    background: white;
    border-radius: 28px;
    padding: 30px;
    box-shadow: 0 18px 40px rgba(0,0,0,0.15);
}}
.mic {{
    border: 3px dashed #38BDF8;
    background: #EFF6FF;
    border-radius: 20px;
    padding: 18px;
}}
.active {{
    border-color: #22C55E;
    background: #ECFDF5;
}}
.pill {{
    background: #DBEAFE;
    padding: 6px 14px;
    border-radius: 999px;
    font-weight: 700;
    color: #1D4ED8;
}}
.btn {{
    padding: 14px 22px;
    border-radius: 16px;
    font-weight: 800;
    transition: 0.2s;
}}
.btn-gray {{
    background: #E5E7EB;
}}
.btn:hover {{
    transform: scale(1.05);
}}
</style>
</head>

<body class="flex justify-center p-6">

<div class="w-full max-w-md">

<div class="flex justify-between mb-4">
    <span id="progress" class="pill"></span>
    <span class="pill">Score: <span id="score">0</span></span>
</div>

<div class="card text-center">
    <div id="emoji" class="text-8xl mb-4">✨</div>
    <div id="word" class="text-6xl font-black mb-2 text-slate-800"></div>
    <div id="kannada" class="text-2xl text-slate-700"></div>
    <div id="translit" class="italic text-slate-500 mb-6"></div>

    <div id="mic" class="mic">
        <p id="instruction" class="uppercase font-bold text-blue-600">Listen…</p>
        <p id="heard" class="text-xl mt-2"></p>
    </div>

    <div class="flex justify-between mt-6">
        <button onclick="retryWord()" class="btn btn-gray">🔁 Retry</button>
        <button onclick="skipWord()" class="btn btn-gray">⏭ Skip</button>
    </div>
</div>

</div>

<script>
const words = {json.dumps(js_words)};
let index = 0;
let score = 0;
let attempts = 0;
let recognition = null;
let isListening = false;
let skipInProgress = false;

function init() {{
    const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SR();
    recognition.lang = "en-US";
    recognition.onresult = onResult;
    recognition.onerror = retryAuto;
    recognition.onend = () => {{
        isListening = false;
        if (skipInProgress) return;
    }};
    loadWord();
}}

function loadWord() {{
    if (index >= words.length) {{
        showEnd();
        return;
    }}

    attempts = 0;
    const w = words[index];

    document.getElementById("progress").innerText =
        `Word ${{index + 1}} / ${{words.length}}`;

    document.getElementById("emoji").innerText = w.emoji;
    document.getElementById("word").innerText = w.word;
    document.getElementById("kannada").innerText = w.kannada;
    document.getElementById("translit").innerText = w.translit;
    document.getElementById("heard").innerText = "";
    document.getElementById("instruction").innerText = "Listen…";

    speak(w.word);
}}

function speak(word) {{
    if (recognition && isListening) {{
        recognition.stop();
        isListening = false;
    }}
    speechSynthesis.cancel();

    const u = new SpeechSynthesisUtterance(word);
    u.rate = 0.85;
    u.onend = () => {{
        if (skipInProgress) return;
        document.getElementById("instruction").innerText = "Say it 🎙️";
        document.getElementById("mic").classList.add("active");
        isListening = true;
        recognition.start();
    }};
    speechSynthesis.speak(u);
}}

function onResult(e) {{
    if (skipInProgress) return;

    const spoken = e.results[0][0].transcript.toLowerCase().trim();
    const correct = words[index].word;

    document.getElementById("heard").innerText = `"${{spoken}}"`;
    document.getElementById("mic").classList.remove("active");

    if (spoken.includes(correct)) {{
        score++;
        document.getElementById("score").innerText = score;
        confetti({{particleCount: 40, spread: 80}});
        index++;
        setTimeout(loadWord, 1000);
    }} else {{
        retryAuto();
    }}
}}

function retryAuto() {{
    if (skipInProgress) return;

    attempts++;
    if (attempts < 3) {{
        setTimeout(() => speak(words[index].word), 900);
    }} else {{
        index++;
        setTimeout(loadWord, 900);
    }}
}}

function retryWord() {{
    attempts = 0;
    speak(words[index].word);
}}

function skipWord() {{
    skipInProgress = true;
    attempts = 0;

    speechSynthesis.cancel();
    try {{ recognition.abort(); }} catch(e){{}}

    index++;

    setTimeout(() => {{
        skipInProgress = false;
        loadWord();
    }}, 250);
}}

function showEnd() {{
    document.body.innerHTML = `
    <div class="text-center mt-32">
        <h2 class="text-5xl font-black text-green-600">Chapter Completed 🎉</h2>
        <p class="mt-6 text-3xl font-bold">
            Score: ${{score}} / ${{words.length}}
        </p>
    </div>`;
}}

init();
</script>

</body>
</html>
"""
    components.html(html_code, height=850, scrolling=False)
