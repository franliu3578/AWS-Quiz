# 🌟 Interactive Quiz App for Python Basics & AWS AIF-C01 🐍🚀

Welcome to the **Interactive Quiz Application**! Whether you're:
- 🐍 Strengthen your Python basics with beginner-friendly quizzes.
- 🚀 Preparing for the **AWS Certified AI Practitioner (AIF-C01)** exam,  

Built with Streamlit, this app offers a clean, user-friendly interface to practice, learn, and master essential topics interactively. 🎯


## ✨ Features You’ll Love

- 🎯 **Engaging Quiz Interface**:
  - Intuitive, interactive quiz design.
  - Supports Python basics and AWS AIF-C01 content.

- 📂 **Multiple Quiz Categories**:
  - 🐍 **Python Quizzes**: Perfect for coding beginners.
  - ☁️ **AWS Certification Quizzes**: Specifically tailored for AIF-C01 exam preparation.

- 🔄 **Randomized and Targeted Practice**:
  - Load specific JSON files for focused learning.
  - Randomize questions for a unique session every time.

- 📊 **Progress Tracking**:
  - Instant results with detailed feedback, hints, and explanations.

- 🛠️ **Custom Input Fields**:
  - Handle coding challenges directly in the app with real-time evaluation.


```plaintext

20241117_Python_AWS_AIF_C01_Quiz/
├── app.py                    # 🌐 Main Streamlit application
├── code/                     # 🧩 Core logic modules
│   ├── quiz_logic.py         # 🚦 Main quiz engine
│   ├── range_quiz.py         # 🎯 Logic for range-based quizzes
│   ├── random_30_quiz.py     # 🔄 Logic for randomized quizzes
│   └── customer_quiz.py      # 🤝 Custom quiz configurations
├── data/                     # 📊 Quiz data
│   ├── json/                 # 🗂️ JSON quiz files
│   │   ├── python_tabime_20.json     # Python quizzes
│   │   ├── aws_aif_c01_eng_87.json  # AWS quizzes (English)
│   │   ├── aws_aif_c01_sc_43.json   # AWS quizzes (Simplified Chinese)
│   │   ├── python_tabime_all_31.json # Combined Python question sets
│   └── pdf/                  # 📄 PDF reference materials
│       ├── AIF_C01_part1_英87題.pdf # AWS AIF-C01 English questions
│       ├── Python_part2_20題.pdf   # Python practice questions
├── .venv/                    # ⚙️ Virtual environment
├── requirements.txt          # 📜 Python package dependencies
├── pyproject.toml            # 🛠️ Poetry configuration file
├── README.md                 # 📘 Project documentation
└── banner.png                # 🎨 App banner for branding

```

## 🚀 Get Started

### Install Dependencies:

Using Poetry:
```bash
poetry install
```
Or using pip:
```bash
pip install -r requirements.txt
```

### Run the App:
```bash
streamlit run app.py
```

### Start Practicing:

1. Select Python or AWS quizzes.
2. Answer questions, get feedback, and track your progress!

---

## 📚 What You’ll Learn

### Python Basics 🐍:
- Variables, data types, loops, and functions.
- Designed for beginners starting their coding journey.

### AWS AIF-C01 Certification ☁️:
- Cloud fundamentals, machine learning basics, and AWS AI tools.
- Includes real-world AIF-C01 exam-style questions.

---

## 🌟 Why Use This App?

- 🧠 Boost Your Knowledge: Strengthen key skills in Python and AWS.
- 🔥 Stay Motivated: Immediate feedback keeps you engaged.
- 🛠️ Build Confidence: Tackle real exam questions and Python problems.

---

## ❤️ Contribute & Collaborate
-We value your feedback! Here’s how you can collaborate:

- 📝 Suggest new quiz topics or question formats.
- 🛠️ Contribute additional Python or AWS-related content.
- 🌟 Enhance the UI/UX for better user engagement.

## ⚠️ Disclaimer
- This app is for educational purposes only and should not be used for commercial distribution or sharing beyond personal use. Content referenced from TibaMe or AWS materials remains the property of its rightful owner.

---

- 💡 Ready to learn and grow? Dive into the app and supercharge your Python and AWS skills today! 🚀✨