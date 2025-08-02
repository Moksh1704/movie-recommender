import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movie data
movies = pd.read_csv('movies.csv')
movies['genres'] = movies['genres'].replace("(no genres listed)", "")

# TF-IDF Vectorizer on genres
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# Cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Mapping movie titles to indices
indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# Recommendation function
def recommend_movies(title, num_recommendations=5):
    idx = indices.get(title)
    if idx is None:
        return []
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()

# --- Streamlit UI ---
st.title("🎬 Movie Recommendation App")
st.write("Find movies similar to your favorite!")

movie_list = movies['title'].sort_values().tolist()
selected_movie = st.selectbox("Choose a movie:", movie_list)
num_recs = st.slider("Number of recommendations:", 3, 10, 5)

if st.button("Recommend"):
    recs = recommend_movies(selected_movie, num_recs)
    if recs:
        st.subheader("Recommended Movies:")
        for i, movie in enumerate(recs, start=1):
            st.write(f"{i}. {movie}")
    else:
        st.error("Movie not found or no recommendations available.")
