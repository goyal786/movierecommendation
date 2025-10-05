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

## 🧠 How It Works

1.Data Preprocessing

- Combines tmdb_5000_movies.csv and tmdb_5000_credits.csv

- Extracts relevant features: genres, keywords, cast, crew, overview

- Cleans and formats data for model training

2.Feature Engineering

- Converts text-based features into vectorized form using CountVectorizer

- Each movie is represented as a numerical vector

3.Similarity Computation

- Computes cosine similarity between all movie vectors

- Stores this matrix in similarity.pkl for fast retrieval

4.Recommendation Function

- When a user enters a movie name, the app retrieves the top 5 most similar movies

- Displays them dynamically via Streamlit UI

---

## 🎥 Example Output

If you search for "The Dark Knight", you might get:

| Rank | Recommended Movie     |
|:----:|:----------------------|
| 1️⃣  | Batman Begins         |
| 2️⃣  | The Dark Knight Rises |
| 3️⃣  | Man of Steel          |
| 4️⃣  | Iron Man              |
| 5️⃣  | Spider-Man 2          |

---

## 🪪 License

This project is licensed under the MIT License — see the LICENSE
 file for details.




