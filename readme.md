```markdown
# 📈 Tesla Stock ML Trading Agent

This repository contains the implementation of a **Machine Learning (ML) trading agent** designed to predict Tesla's stock price movements and perform trading in a simulated real-time environment.

---

## 🚀 Project Overview

This project involves:

- Using historical and contextual stock data to train a predictive ML model (XGBoost).
- Making daily trading decisions (Buy/Sell/Hold) based on the model predictions.
- Simulating trades with a starting capital of \$10,000, factoring in transaction fees, to maximize profits within the trading week.

---

## 📆 Simulation Details

**Simulation Period:** March 24 – March 28, 2025  
**Starting Capital:** \$10,000 USD  
**Transaction Fee:** 1% per transaction  
**Daily Order Submission Deadline:** 9:00 AM EST  
**Order Execution Time:** 10:00 AM EST (based on market prices)

---

## 🗂️ Project Files

- `TSLA.csv` - Historical Tesla stock data used for training.
- `train_model.py` - Script for data preprocessing and training the ML model.
- `predict_daily.py` - Script for generating daily trade decisions.
- `tsla_model.pkl` - Saved trained XGBoost ML model.
- `requirements.txt` - Python libraries required to run this project.

---

## ⚙️ Installation & Setup

Clone this repository:

```bash
git clone <your-repo-url>
cd <repo-folder>
```

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## 📌 Usage

### 🔧 Train the Model (Run before the simulation week):

```bash
python train_model.py
```

### 📊 Generate Daily Predictions (Run daily from March 24–28, before 9:00 AM EST):

```bash
python predict_daily.py
```

Each run of `predict_daily.py` outputs a daily recommended trade action: **Buy**, **Sell**, or **Hold**.

---

## 🧠 Machine Learning Model

- **Algorithm Used:** [XGBoost Classifier](https://xgboost.ai/)
- **Features Used:**
  - Open, High, Low, Close, Volume
  - SMA (Simple Moving Average, 10-day)
  - EMA (Exponential Moving Average, 20-day)
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)

---

## 📋 Assignment Guidelines

- **Code Freeze:** Sunday, March 23, 2025, at 11:00 PM EST.
- **Daily Transactions:** Submit via provided forms before 9:00 AM EST each day from March 24 to March 28.
- **Requirement:** At least one buy or sell transaction must be completed (five consecutive "Hold" transactions result in disqualification).

---

## 📝 Deliverables

- ✅ Daily trading decisions submitted via daily forms.
- ✅ GitHub repository URL submitted before the code freeze deadline.
- ✅ Final report and presentation summarizing strategy, results, and insights.

---

## ✨ Contributors

- Your Name ([@GitHubUsername](https://github.com/yourusername))
- Group Members' Names ([@GitHubUsername](https://github.com/memberusername))

---

## 📞 Questions?

If you have any questions or need further clarification, please feel free to reach out.
```
