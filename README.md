# 🎬 Movie Recommendation System

A Machine Learning based Movie Recommendation System that suggests similar movies based on content similarity. The application is built using Python and Streamlit and displays movie posters, ratings, release year, and overview for each recommended movie.

---

## 📌 Features

- Recommend 5 similar movies
- Displays movie posters using OMDb API
- Shows IMDb rating
- Shows release year
- Displays movie overview
- Interactive Streamlit web interface

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle
- Requests
- OMDb API

---

## 📂 Dataset

This project uses the TMDB 5000 Movie Dataset.

Files used:
- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

---

## 📁 Project Structure

```
Movie-Recommendation-System/
│
├── app.py
├── Movie_Recommendation_System.ipynb
├── movies.pkl
├── similarity.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── requirements.txt
├── README.md
```

---

## ⚙️ How It Works

1. Load movie dataset.
2. Merge movies and credits datasets.
3. Perform data preprocessing.
4. Create tags using genres, keywords, cast, crew, and overview.
5. Apply CountVectorizer to convert text into vectors.
6. Calculate cosine similarity between movies.
7. Save processed data using Pickle.
8. Streamlit loads the saved model and recommends similar movies.
9. Movie posters are fetched dynamically using the OMDb API.

---


## 📚 Machine Learning Concepts Used

- Data Cleaning
- Feature Engineering
- NLP (Text Processing)
- CountVectorizer
- Cosine Similarity
- Recommendation Systems
- Model Serialization using Pickle

---

## 📈 Future Improvements

- Add movie trailers
- Search by genre
- Filter by language
- User authentication
- Deploy on Streamlit Cloud


## Note

The `similarity.pkl` file is not included in this repository because it exceeds GitHub's file size limit (100 MB).

To run the project:
1. Open the Jupyter Notebook.
2. Run all cells to generate `similarity.pkl`.
3. Run the Streamlit app:
   python -m streamlit run app.py

