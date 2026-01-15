# SpamHam-project
This project classifies French emails into **spam** or **ham (non-spam)** using Machine Learning models and provides a web interface with Flask.

---

## 📁 Project Structure
predectionProjet/
├── data/                        # Dataset
│   └── spam_ham_emails_fr_500.csv
├── artifacts/                   # Generated models
│   ├── model.pkl
│   └── encoder.pkl
├── backend/                     # Backend code
│   ├── train.py
│   ├── server.py
│   └── utils.py
├── frontend/                    # Frontend interface
│   ├── index.html
│   ├── style.css
│   └── script.js
├── README.md
├── requirements.txt
└── .gitignore

---

## 🔧 Tech Stack

- Python 3
- Flask
- Pandas, Numpy
- Scikit-learn
- NLTK (stopwords)
- HTML / CSS / JavaScript

---

## 🚀 How to Run

### 1️⃣ Install Dependencies

```bash
1.pip3 install -r requirements.txt
requirements.txt should contain:
Flask
pandas
scikit-learn
nltk
2.Make sure the dataset is in data/ folder:
predectionProjet/data/spam_ham_emails_fr_500.csv
3.Train model
cd backend
python3 train.py
This will generate:
predectionProjet/artifacts/model.pkl
predectionProjet/artifacts/encoder.pkl
4.run server
python3 server.py
