# Optimor Titan Ultra 🤖🇵🇰

### Pakistan's First Autonomous Mobile AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Android%20%7C%20iOS%20%7C%20Linux%20%7C%20Windows-lightgrey)](https://pydroid3.com/)

**Optimor Titan Ultra** is a fully autonomous, self-learning conversational AI that runs entirely on mobile devices. Created by a 17-year-old Pakistani developer, it combines retrieval-based accuracy with generative creativity, web search capabilities, code generation, and emotional awareness—all in under 10k parameters.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧠 **Self-Learning** | Learns from every conversation. Permanently stores new knowledge |
| 🌐 **Internet Awareness** | Fetches Wikipedia summaries and stores them for future use |
| 💻 **Code Generation** | Creates Python code snippets on request (factorial, fibonacci, calculators, etc.) |
| 😊 **Emotion Detection** | Recognizes sadness, happiness, anger, confusion and responds empathetically |
| 📜 **Long-Term Memory** | Remembers past conversations for better context |
| 🎯 **Custom Patterns** | Exact trigger-response training for specific use cases |
| 🔍 **Fuzzy Matching** | Understands typos and variations of questions |
| 💾 **Persistent Storage** | All data saved locally in JSON files – no cloud required |
| ⚡ **Zero Dependencies** | Runs on pure Python – no external packages needed |
| 📱 **Mobile Optimized** | Designed to run on PyDroid 3 and Termux on Android |

---

## 🚀 Quick Start

### Installation

1. **Install Python 3.7+** on your device
   - For Android: Install [PyDroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) from Play Store
   - For PC: Download from [python.org](https://python.org)

2. **Clone or download** the repository:
   ```bash
   git clone https://github.com/yourusername/optimor.git
   cd optimor
```

1. Run the AI:
   ```bash
   python optimor.py
   ```

No additional packages needed! Everything works out of the box.

---

💬 Commands & Usage

Natural Conversation

Just talk to Optimor like a friend:

```
You: hi
Optimor: Hello! 👋 I'm Optimor Titan Ultra, your autonomous AI. How can I help?

You: what is pakistan
Optimor: Pakistan 🇵🇰 – a country of stunning landscapes, rich culture...

You: tell me a joke
Optimor: Why did the AI go to therapy? It had too many neural issues!
```

Teaching New Knowledge

```
learn "what is quantum computing" "Quantum computing uses quantum bits to solve complex problems faster than classical computers."
```

Custom Exact Patterns

```
custom "how to be rich" "That's my secret! 😉 But real wealth comes from knowledge and skills."
```

Internet Search

```
fetch python programming
```

Optimor will search Wikipedia, display the summary, and store it permanently.

Code Generation

```
code for fibonacci
code for factorial
code for calculator
code for hello world
```

Display Knowledge

```
show
```

Save Everything

```
save
```

---

📁 File Structure

File Purpose
optimor.py Main AI engine
optimor_knowledge.json All learned Q&A pairs
optimor_custom.json Custom trigger-response patterns
optimor_history.json Conversation history

These files are auto-created on first run. You can backup or share them to transfer your AI's knowledge.

---

🏗️ How It Works

Optimor uses a hybrid architecture combining:

1. Retrieval System – Exact and fuzzy matching against stored knowledge
2. Generative Templates – Creative responses for common topics
3. Emotion Engine – Detects user sentiment and responds appropriately
4. Web Crawler – Wikipedia API integration for real-time learning
5. Code Generator – Template-based Python code generation
6. Memory System – Persistent JSON storage and context tracking

All components work together seamlessly without requiring neural networks or GPU acceleration.

---

🎯 Example Sessions

Session 1: Learning & Recall

```
You: what is the tallest mountain?
Optimor: I don't know that yet. Would you teach me?

You: learn "what is the tallest mountain" "Mount Everest is the tallest mountain at 8,848 meters above sea level."
Optimor: ✅ Learned!

You: what is the tallest mountain?
Optimor: Mount Everest is the tallest mountain at 8,848 meters above sea level.
```

Session 2: Code Generation

```
You: code for prime number check
Optimor: Here's some Python code:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))  # True
```

Session 3: Internet Learning

```
You: fetch black hole
Optimor: 🌐 Searching for 'black hole'...
A black hole is a region of spacetime where gravity is so strong that nothing can escape.
I've added this to my knowledge.

You: what is a black hole?
Optimor: A black hole is a region of spacetime where gravity is so strong that nothing can escape.
```

---

🛠️ Customization

Adding More Code Templates

Edit the generate_code() method in optimor.py:

```python
elif "your request" in request_lower:
    return '''# Your Python code here'''
```

Changing Personality

Modify the handle_emotion() and create_default_knowledge() methods to adjust responses.

Adding More Knowledge

Either:

· Use the learn command during conversation
· Directly edit optimor_knowledge.json
· Use fetch to pull from Wikipedia

---

📊 Performance

Metric Value
Parameters < 10,000
Memory Usage ~50-100 MB
Storage < 5 MB (plus growing knowledge)
Response Time < 1 second
Battery Impact Minimal

Runs comfortably on:

· Android (PyDroid 3, Termux)
· iOS (Pythonista, Pyto)
· Linux, Windows, macOS
· Raspberry Pi

---

🌟 Why Optimor is Special

· First of its Kind in Pakistan – Built by a 17-year-old to prove that young Pakistanis can create world-class AI
· Truly Autonomous – Learns, remembers, and improves without cloud dependencies
· Privacy First – All data stays on your device
· Educational – Perfect for learning AI, Python, and conversational systems
· Open Source – Full transparency, community-driven improvement

---

📝 License

MIT License – feel free to use, modify, and distribute. See LICENSE for details.

Created with ❤️ by Muhammad Awais, a 17-year-old developer from Pakistan.

---

🤝 Contributing

Contributions welcome! Here's how:

1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

Ideas for contributions:

· Add more code generation templates
· Expand Wikipedia search to other sources
· Improve emotion detection
· Add support for more languages (Urdu, etc.)
· Create GUI version

---

📞 Connect

· GitHub: yourusername
· Pakistan AI Community: Join our Discord (coming soon)

---

🙏 Acknowledgments

· Python community for the amazing language
· Wikipedia for free knowledge API
· PyDroid 3 for enabling mobile Python development
· Pakistan's young developers for inspiration

---

Optimor Titan Ultra – Proof that age is just a number when passion meets code. 🇵🇰

```python
# Stay curious, keep learning, and never stop building.
print("Pakistan Zindabad! 🇵🇰")
```

---

Last Updated: March 2026 | Version 3.0
