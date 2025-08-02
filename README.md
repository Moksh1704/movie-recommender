# Movie-Recommender
A simple movie recommender system using Streamlit and content-based filtering.



## 📄 `README.md`


# 🎬 Movie Recommendation System

A simple **content-based movie recommender system** built with **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**. It recommends movies based on genres using TF-IDF and cosine similarity.



## 🚀 Demo

Run the app locally and explore movie recommendations from the MovieLens dataset.

> Example:  
Input: `Toy Story (1995)`  
→ Output: A list of similar movies based on genres.



## 📦 Features

- Recommend similar movies based on genre metadata.
- Clean and simple web interface built using Streamlit.
- Real-time recommendations.
- Adjustable number of results (3–10).



## 🧠 How It Works

- **TF-IDF Vectorization**: Genres are vectorized using TF-IDF.
- **Cosine Similarity**: Used to calculate similarity between movie genre vectors.
- **Recommendation Function**: Returns top N similar movies.

## 📁 Dataset

This project uses the [MovieLens Latest Small Dataset (100k)](https://grouplens.org/datasets/movielens/).

Place the `movies.csv` file in:
```

project-folder/ml-latest-small/movies.csv

````

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone https://github.com/Moksh1704/movie-recommender.git
cd movie-recommender
````

### 2. Install requirements

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pandas scikit-learn streamlit
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open your browser at [http://localhost:8501](http://localhost:8501)

---

## 📚 Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit

---

## 📜 License

MIT License. Feel free to use and adapt.

---

## 🤝 Acknowledgments

* [MovieLens Dataset by GroupLens](https://grouplens.org/datasets/movielens/)

````

---

## ✅ Next Steps:

1. **Create a file** in your project folder called `README.md`.
2. Paste the code above into it.
3. Save it.
4. Then run:
   ```bash
   git add README.md
   git commit -m "Add README"
   git push
````


