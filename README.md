# 🛡️ AI-Powered Phishing Detection & Training System

## 📌 Overview

This project is an intelligent cybersecurity system designed to detect phishing emails and improve user awareness through simulated phishing attacks. It combines Machine Learning and rule-based analysis to identify malicious content and suspicious links in real time.

---

## 🚨 Problem Statement

Users continue to fall victim to phishing attacks, which remain one of the most common entry points for cyber breaches.

---

## 💡 Solution

We built a hybrid system that:

* Detects phishing emails using **Machine Learning (NLP-based classification)**
* Analyzes embedded URLs for suspicious patterns
* Provides **risk levels and probability scores**
* Simulates phishing scenarios to train users

---

## ⚙️ Features

* 🔍 Email Content Analysis (ML-based)
* 🔗 Suspicious Link Detection
* 📊 Risk Level Classification (Low / Medium / High)
* 📈 Probability-based Prediction
* 🧠 Hybrid Detection System (ML + Rule-based)
* 🎓 Phishing Simulation Module

---

## 🧠 How It Works

1. User inputs email text
2. Text is processed using TF-IDF vectorization
3. ML model predicts phishing probability
4. URLs are extracted and analyzed
5. Final decision is made using combined logic
6. Output includes prediction, risk level, and suspicious links

---

## 🛠️ Tech Stack

* **Frontend:** HTML, JavaScript
* **Backend:** Flask (Python)
* **Machine Learning:** Scikit-learn (Logistic Regression, TF-IDF)
* **Data Processing:** Pandas

---

## 📊 Model Details

* Algorithm: Logistic Regression
* Accuracy: ~98%

---

## 🚀 How to Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run backend server

```bash
python app.py
```

### 3️⃣ Test API

```bash
python test_api.py
```

---

## 🧪 Example Input

```
Urgent! Your account has been suspended. Click here to verify:
http://fake-bank-login.xyz
```

## ✅ Example Output

```
Prediction: Phishing  
Risk Level: High  
Suspicious Links: [Detected]
```

---

## 👥 Team

* Project Manager: Sahil Gawali
* Team Members: (Add your team here)

---

## 📌 Conclusion

This system not only detects phishing attacks but also addresses the root cause — lack of user awareness — making it a comprehensive cybersecurity solution.
