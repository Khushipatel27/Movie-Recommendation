# 🎬 Movie Recommendation System

This project is a content-based movie recommendation system built with **Python**, **Streamlit**, and **TMDB API**.  
It suggests similar movies based on a selected title and displays their posters.

---

## 🚀 Features
- Select any movie from the dataset.
- Get **10 movie recommendations** instantly.
- Displays movie posters fetched from TMDB API.
- Simple and interactive **Streamlit web app**.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Khushipatel27/movie-recommendation.git
   cd movie-recommender
   ```

2. Create and activate a virtual environment:
```
python -m venv myenv
source myenv/bin/activate #for mac
myenv\Scripts\activate #for windows
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Make sure you have the following files in your project:
- movie_dict.pkl
- similarity.pkl

▶️ Running the App

Run the following command:
```
streamlit run app.py
```

## 📸 Demo Screenshots
<img width="1869" height="1854" alt="Screenshot 2025-09-09 000534" src="https://github.com/user-attachments/assets/b3057abd-8e24-4d0c-8afa-2449fc4f8928" />
<img width="1565" height="1697" alt="Screenshot 2025-09-09 000514" src="https://github.com/user-attachments/assets/3d1c138d-7b2f-4b32-abd3-3503279078b4" />

## 📂 Output Example

When you select a movie, the system will display 10 recommendations in 2 rows with posters:
Movie Selected: Avatar

Recommendations:
- John Carter
- Guardians of the Galaxy
- The Avengers
- Thor
- Star Trek
- Green Lantern
- Man of Steel
- Prometheus

## ⚡ Tech Stack
- Python
- Streamlit
- Pandas
- Pickle
- Requests (TMDB API)

## 🙌 Acknowledgements
TMDB API for movie posters and metadata.



