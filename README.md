# 🎬 Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A **Content-Based Movie Recommendation System** built using **Python**, **Pandas**, and **Streamlit** that suggests similar movies based on your input.  
It uses **The Movie Database (TMDB) dataset** and applies **NLP and cosine similarity** to find and display related movies interactively.

---

## 🚀 Features

- 🔍 Search for any movie and instantly get similar recommendations  
- 🎞️ Uses **TMDB dataset** (`tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`)  
- 🧠 Implements **content-based filtering** using **cosine similarity**  
- 💾 Fast recommendations using preprocessed `.pkl` model files  
- 🌐 Clean and interactive **Streamlit web interface**  
- ☁️ Ready for **Heroku or Streamlit Cloud deployment**

---

## 🧰 Tech Stack

| Component | Technology Used |
|------------|-----------------|
| Programming Language | Python 3.x |
| Framework | Streamlit |
| Data Handling | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Model Storage | Pickle |
| Dataset | TMDB 5000 Movies & Credits |

---

## 📂 Project Structure

movierecommendation-main/

│
├── movierecom/

│ ├── appdict.py # Main Streamlit application

│ ├── movies.pkl # Preprocessed movie dataset

│ ├── similarity.pkl # Precomputed similarity matrix

│ ├── tmdb_5000_movies.csv # TMDB movie dataset

│ ├── tmdb_5000_credits.csv # TMDB credits dataset

│ ├── requirements.txt # Required dependencies

│ ├── procfile # For deployment on Heroku

│ └── pro.ipynb # Model training and preprocessing notebook

│
└── README.md # Project documentation


---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/movierecommendation.git
cd movierecommendation-main/movierecom 

