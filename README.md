# Optimor – Pakistan’s First Mobile Transformer AI

**Optimor** is a lightweight Transformer-based AI designed to run entirely on mobile devices (Android). Built by Muhammad Awais at age 17, it aims to demonstrate that advanced AI can be created and deployed on consumer hardware.


## ✨ Features

- **Real Transformer architecture** – Multi‑head self‑attention, feed‑forward networks, positional encodings.
- **On‑device inference** – Runs locally using only Python and NumPy.
- **English dictionary vocabulary** – 204 words (expandable).
- **Conversational interface** – Chat with the AI in terminal.

## 🧠 Current Status

| Component           | Status          |
|---------------------|-----------------|
| Transformer code    | ✅ Complete     |
| Vocabulary loading  | ✅ Working      |
| Forward pass        | ✅ Working      |
| Training / Backprop | ❌ Needs work   |

The model initializes correctly and can generate responses, but the output is currently random dictionary words because **the training loop does not yet properly update weights**. The transformer architecture is sound; we need help implementing efficient backpropagation (or fixing the numerical gradient approach) to make the model learn from conversation data.

### 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Termux](https://img.shields.io/badge/Termux-000000?style=for-the-badge&logo=termux&logoColor=white)
![Pydroid 3](https://img.shields.io/badge/Pydroid%203-FFD43B?style=for-the-badge&logo=python&logoColor=3776AB)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)


## 🚀 Getting Started

### Prerequisites
- Python 3.7+ (Termux or PyDroid recommended)
- NumPy
- A terminal with storage access

### Installation
```bash
git clone https://github.com/hyboxteam/Optimor.git
cd Optimor
pip install numpy
```

### Run the AI

```bash
python optimor_final.py
```

If the model has not been trained yet, it will attempt to train (slowly) – but currently the training does not reduce loss. You can still chat with the pre‑loaded knowledge base.

## 🤝 How to Contribute

We welcome all skill levels! Here are specific areas where help is needed:

· Implement proper backpropagation – replace the numerical gradient loop with analytical gradients (or fix the current gradient calculation) so the model learns from training data.
· Optimize for mobile – reduce memory usage, speed up inference, convert to pure Python where possible.
· Expand vocabulary – add more words from words.json or support sub‑word tokenization.
· Improve response generation – add sampling temperature, beam search, or better fallback strategies.
· Create a simple GUI – integrate with a mobile app or web interface.

## How to Submit

1. Fork the repository.
2. Create a new branch for your feature/fix.
3. Commit your changes.
4. Open a pull request with a clear description.

For major changes, please open an issue first to discuss.

📂 Project Structure

```
Optimor/
├── optimor_final.py          # Main AI script
├── words.json                # English dictionary (source: dwyl/english-words)
└── README.md                 # This file
```

## 🎯 Vision

To create an open‑source Transformer AI that anyone can run on their phone – and to prove that young developers in Pakistan can build world‑class AI tools.

## 👨‍💻 Creator

Muhammad Awais – a 17‑year‑old developer from Pakistan, passionate about AI and open source.

· GitHub: @hyboxteam
· Contact: awais.112191@gmail.com

### 📄 License

MIT – free to use, modify, and share.

---


### 💖 Support & Donate

If you'd like to support my development work, feel free to contribute through any of these platforms:

![Easypaisa](https://img.shields.io/badge/Easypaisa-2ECC71?style=for-the-badge&logo=esewa&logoColor=white)  
`+923437335632`

![Binance](https://img.shields.io/badge/Binance_UID-F3BA2F?style=for-the-badge&logo=binance&logoColor=black)  
`1155138880`

![BNB Chain](https://img.shields.io/badge/BNB_Chain-F3BA2F?style=for-the-badge&logo=binance&logoColor=black)  
`0xc26f066E2ec5822a5508Ae0455CCA0A236B620d3`



---
Pakistan Zindabad! 🇵🇰
Let’s make mobile AI a reality together.
