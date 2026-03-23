"""
OPTIMOR TITAN ULTRA v3.0
Pakistan's First Autonomous AI
- Self‑learning from conversations
- Internet knowledge retrieval (Wikipedia)
- Code generation & assistance
- Long‑term memory & context
- Emotionally aware
- No external packages needed
Created by Muhammad Awais (Age 17)
"""

import json
import os
import random
import re
import time
import threading
import urllib.request
import urllib.parse
import hashlib
from datetime import datetime
from difflib import get_close_matches

class OptimorTitan:
    def __init__(self):
        self.knowledge = {}           # main Q&A store
        self.custom_patterns = {}     # exact trigger → response
        self.conversation_history = [] # for context
        self.learning_mode = True      # if True, asks when unknown
        self.web_search_enabled = True # if True, tries Wikipedia on unknown topics
        self.last_topic = None
        self.load_all()
        self.start_background_tasks()

    # ------------------ File Management ------------------
    def load_all(self):
        """Load all data files; create them if missing."""
        # Knowledge base
        if os.path.exists('optimor_knowledge.json'):
            with open('optimor_knowledge.json', 'r') as f:
                self.knowledge = json.load(f)
            print(f"✓ Loaded {len(self.knowledge)} knowledge entries")
        else:
            self.create_default_knowledge()
            print(f"✓ Created new knowledge base ({len(self.knowledge)} entries)")

        # Custom patterns
        if os.path.exists('optimor_custom.json'):
            with open('optimor_custom.json', 'r') as f:
                self.custom_patterns = json.load(f)
            print(f"✓ Loaded {len(self.custom_patterns)} custom patterns")

        # Conversation history
        if os.path.exists('optimor_history.json'):
            with open('optimor_history.json', 'r') as f:
                self.conversation_history = json.load(f)
            print(f"✓ Loaded {len(self.conversation_history)} past conversations")

    def save_all(self):
        """Save all data to disk."""
        with open('optimor_knowledge.json', 'w') as f:
            json.dump(self.knowledge, f, indent=2)
        with open('optimor_custom.json', 'w') as f:
            json.dump(self.custom_patterns, f, indent=2)
        with open('optimor_history.json', 'w') as f:
            json.dump(self.conversation_history[-500:], f, indent=2)  # keep last 500

    # ------------------ Default Knowledge ------------------
    def create_default_knowledge(self):
        """Initial knowledge to get started."""
        self.knowledge = {
            "hi": "Hello! 👋 I'm Optimor Titan Ultra, your autonomous AI. How can I help?",
            "hello": "Assalam-o-Alaikum! 🌟 Ready to chat, learn, or build something?",
            "how are you": "I'm running at full power! ⚡ How about you?",
            "what is your name": "I'm Optimor Titan Ultra – Pakistan's first self‑learning AI. Created by Muhammad Awais.",
            "who is your creator": "Muhammad Awais, a 17‑year‑old Pakistani developer. He built me to explore AI on mobile!",
            "what can you do": "I can chat, learn from you, search the internet (Wikipedia), generate code, and remember our talks. Just ask!",
            "bye": "Khuda Hafiz! 🙏 Keep learning. I'll be here when you return.",
            "goodbye": "Take care! 🌟 Remember: every expert was once a beginner.",
            "thank you": "You're welcome! 😊 Your satisfaction is my fuel.",
            "tell me a joke": random.choice([
                "Why did the AI go to therapy? It had too many neural issues!",
                "What's a computer's favorite beat? An algorithm!",
                "Why did the Python programmer break up? Too many unresolved dependencies!"
            ]),
            "what is pakistan": "Pakistan 🇵🇰 – a country of stunning landscapes, rich culture, and warm people. Home to K2 and my creator!",
            "what is k2": "K2 – the 'Savage Mountain', second highest peak on Earth (8,611 m), located in Pakistan's Karakoram range.",
            "what is ai": "Artificial Intelligence – making machines think and learn. I'm a small but growing example!",
            "how do i learn coding": "Start with Python! Build small projects, ask me for help, and never stop practicing. I can generate code for you!",
        }

    # ------------------ Internet Knowledge ------------------
    def fetch_wikipedia_summary(self, topic):
        """Retrieve summary from Wikipedia using the API."""
        try:
            topic_enc = urllib.parse.quote(topic)
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic_enc}"
            req = urllib.request.Request(url, headers={'User-Agent': 'OptimorTitan/1.0'})
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                if 'extract' in data:
                    summary = data['extract']
                    # limit length
                    if len(summary) > 500:
                        summary = summary[:500] + "..."
                    return summary
                else:
                    return None
        except Exception as e:
            print(f"[Web fetch error] {e}")
            return None

    def learn_from_web(self, topic):
        """Search Wikipedia for a topic and store it in knowledge."""
        print(f"🌐 Searching Wikipedia for '{topic}'...")
        summary = self.fetch_wikipedia_summary(topic)
        if summary:
            # store with a normalized key
            key = f"what is {topic}"
            self.knowledge[key] = summary
            self.save_all()
            return summary
        else:
            return None

    # ------------------ Code Generation ------------------
    def generate_code(self, request):
        """Generate simple Python code based on user request."""
        request_lower = request.lower()
        if "hello world" in request_lower:
            return 'print("Hello, World!")'
        elif "add two numbers" in request_lower:
            return '''
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8
'''
        elif "factorial" in request_lower:
            return '''
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120
'''
        elif "fibonacci" in request_lower:
            return '''
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a+b
    print()

fibonacci(10)
'''
        elif "calculator" in request_lower:
            return '''
# Simple calculator
while True:
    expr = input("Enter expression (or 'quit'): ")
    if expr == 'quit':
        break
    try:
        print("Result:", eval(expr))
    except:
        print("Invalid expression")
'''
        else:
            # fallback: generic template
            return f'''# Python code generated for: {request}
# (You may need to adapt this to your needs)

def solve_problem():
    # Your code here
    pass

if __name__ == "__main__":
    solve_problem()
'''
    # ------------------ Core Response Logic ------------------
    def normalize(self, text):
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', '', text)
        return text

    def detect_emotion(self, text):
        text_lower = text.lower()
        if any(w in text_lower for w in ['sad', 'depressed', 'lonely', 'upset']):
            return 'sad'
        if any(w in text_lower for w in ['happy', 'great', 'awesome', 'excited']):
            return 'happy'
        if any(w in text_lower for w in ['angry', 'mad', 'hate', 'frustrated']):
            return 'angry'
        if any(w in text_lower for w in ['what', 'huh', 'confused', 'understand']):
            return 'confused'
        return 'neutral'

    def handle_emotion(self, emotion):
        if emotion == 'sad':
            return "I'm here for you. 💙 Sometimes talking helps. Want to share what's on your mind?"
        if emotion == 'happy':
            return "That's wonderful! 😊 Tell me more about what's making you happy!"
        if emotion == 'angry':
            return "I sense you're upset. 🫂 I'm sorry if I did something wrong. Let me try again – what can I help with?"
        if emotion == 'confused':
            return "I'm happy to clarify! 😊 Could you ask again or tell me what you're looking for?"
        return None

    def get_response(self, user_input):
        """Main decision engine."""
        original = user_input.strip()
        norm = self.normalize(original)

        # 1. Emotion override
        emotion = self.detect_emotion(original)
        emotion_response = self.handle_emotion(emotion)
        if emotion_response:
            return emotion_response

        # 2. Custom patterns (exact trigger)
        for trigger, resp in self.custom_patterns.items():
            if trigger in norm or norm in trigger:
                return resp

        # 3. Direct knowledge match
        if original in self.knowledge:
            return self.knowledge[original]
        if norm in self.knowledge:
            return self.knowledge[norm]

        # 4. Fuzzy match
        all_q = list(self.knowledge.keys())
        matches = get_close_matches(norm, all_q, n=1, cutoff=0.7)
        if matches:
            return self.knowledge[matches[0]]

        # 5. Code generation request
        if any(phrase in original.lower() for phrase in ["write code", "generate code", "code for", "python code"]):
            return f"```python\n{self.generate_code(original)}\n```"

        # 6. Web search (if enabled)
        if self.web_search_enabled:
            # extract likely topic: take longest words (heuristic)
            words = re.findall(r'\b\w{4,}\b', original)
            topic = words[0] if words else original
            summary = self.learn_from_web(topic)
            if summary:
                # store it
                self.knowledge[original] = summary
                self.save_all()
                return f"🌐 I looked up '{topic}' for you:\n\n{summary}\n\nI'll remember that for next time!"
            else:
                return "I couldn't find that online. Could you teach me? (Use: learn 'question' 'answer')"

        # 7. Learning mode: ask user to teach
        if self.learning_mode:
            return "I don't know that yet. 🤔 Would you teach me? Use: learn 'question' 'answer' (or just type the answer now if you want)"

        # 8. Fallback
        return "Interesting! Tell me more, or teach me something new."

    # ------------------ Learning ------------------
    def learn(self, question, answer):
        """Store a new Q&A pair."""
        question = question.strip()
        self.knowledge[question] = answer
        norm = self.normalize(question)
        if norm != question:
            self.knowledge[norm] = answer
        self.save_all()
        return f"✅ Learned: '{question}'\nNow I'll know that for next time!"

    def learn_custom(self, trigger, response):
        """Store a trigger→response pattern (exact match)."""
        self.custom_patterns[trigger.lower()] = response
        self.save_all()
        return f"✅ Custom pattern saved: when you say '{trigger}', I'll respond accordingly."

    # ------------------ Background Tasks ------------------
    def background_learning(self):
        """Optional: periodically fetch trending topics? For now, just simulate."""
        # Could be extended to scrape news or automatically expand knowledge.
        pass

    def start_background_tasks(self):
        """Start a thread for background learning (if needed)."""
        # For simplicity, we just do a dummy thread; can be extended.
        thread = threading.Thread(target=self.background_learning, daemon=True)
        thread.start()

    # ------------------ Chat Loop ------------------
    def chat(self):
        print("\n" + "="*70)
        print(" 🤖  OPTIMOR TITAN ULTRA v3.0  🤖")
        print(" Pakistan's First Autonomous AI")
        print(" Created by Muhammad Awais (Age 17)")
        print("="*70)
        print("\n✨ Features:")
        print("   • Self‑learning from conversations")
        print("   • Internet lookup (Wikipedia)")
        print("   • Code generation")
        print("   • Emotional awareness")
        print("   • Long‑term memory")
        print("\n💡 Commands:")
        print("   learn 'question' 'answer'        - Teach me facts")
        print("   custom 'trigger' 'response'      - Teach exact patterns")
        print("   fetch 'topic'                    - Look up a topic online")
        print("   show                             - Show what I know")
        print("   code 'request'                   - Generate code (e.g., 'code for factorial')")
        print("   save                             - Force save")
        print("   quit                             - Exit")
        print("="*70)
        print("\n🎯 I'm ready. Just talk to me naturally, or use commands.\n")

        while True:
            try:
                raw = input("👤 You: ").strip()
                if not raw:
                    continue

                # --- Command handling ---
                if raw.lower() == 'quit':
                    self.save_all()
                    print("\n🤖 Optimor: Khuda Hafiz! 🇵🇰 Keep exploring. I'll be here.")
                    break

                if raw.lower() == 'save':
                    self.save_all()
                    print("✓ All data saved.")
                    continue

                if raw.lower() == 'show':
                    print(f"\n📚 I know {len(self.knowledge)} facts.")
                    print(f"🎯 I have {len(self.custom_patterns)} custom patterns.")
                    print("\nRecent topics:")
                    for q in list(self.knowledge.keys())[-10:]:
                        print(f"  • {q}")
                    continue

                if raw.lower().startswith('learn '):
                    rest = raw[6:].strip()
                    if rest.startswith('"'):
                        parts = rest.split('"')
                        if len(parts) >= 3:
                            q = parts[1]
                            a = parts[3] if len(parts) > 3 else "I learned this!"
                            print(f"🤖 Optimor: {self.learn(q, a)}")
                        else:
                            print("Format: learn \"question\" \"answer\"")
                    else:
                        print("Format: learn \"question\" \"answer\"")
                    continue

                if raw.lower().startswith('custom '):
                    rest = raw[7:].strip()
                    if rest.startswith('"'):
                        parts = rest.split('"')
                        if len(parts) >= 3:
                            trig = parts[1]
                            resp = parts[3] if len(parts) > 3 else "I learned this!"
                            print(f"🤖 Optimor: {self.learn_custom(trig, resp)}")
                        else:
                            print("Format: custom \"trigger\" \"response\"")
                    else:
                        print("Format: custom \"trigger\" \"response\"")
                    continue

                if raw.lower().startswith('fetch '):
                    topic = raw[6:].strip()
                    print(f"🤖 Optimor: Searching for '{topic}'...")
                    summary = self.fetch_wikipedia_summary(topic)
                    if summary:
                        # store under a reasonable key
                        key = f"what is {topic}"
                        self.knowledge[key] = summary
                        self.save_all()
                        print(f"🤖 Optimor: {summary}\n\nI've added this to my knowledge.")
                    else:
                        print("🤖 Optimor: Sorry, I couldn't find that topic. Try another keyword.")
                    continue

                if raw.lower().startswith('code '):
                    req = raw[5:].strip()
                    code = self.generate_code(req)
                    print(f"🤖 Optimor: Here's some Python code:\n```python\n{code}\n```")
                    continue

                # --- Normal conversation ---
                response = self.get_response(raw)
                print(f"🤖 Optimor: {response}\n")

                # Store in history
                self.conversation_history.append({
                    "user": raw,
                    "ai": response,
                    "time": datetime.now().isoformat()
                })
                if len(self.conversation_history) > 500:
                    self.conversation_history.pop(0)

            except KeyboardInterrupt:
                self.save_all()
                print("\n\n🤖 Optimor: Goodbye! Stay curious.")
                break
            except Exception as e:
                print(f"⚠️ Error: {e}")
                print("   Don't worry, just keep chatting. I'm learning!")

        self.save_all()

# ------------------ Run ------------------
if __name__ == "__main__":
    ai = OptimorTitan()
    ai.chat()