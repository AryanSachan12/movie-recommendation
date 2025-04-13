import streamlit as st
import pickle
import os
import subprocess

# Initialize variables
movies = None
movies_names = None
similarity = None


#Check if the pickle files already exist
def check_and_run_notebook():
    if not os.path.exists("movies.pkl") or not os.path.exists("similarity.pkl"):
        st.text(
            "Movie and/or similarity files are missing. Running model_training.ipynb to generate them..."
        )
        # Run the notebook to generate the pickle files if they don't exist
        result = subprocess.run(
            [
                "jupyter",
                "nbconvert",
                "--to",
                "notebook",
                "--execute",
                "model_training.ipynb",
            ],
            capture_output=True,
            text=True,
        )
        # Check if the notebook ran successfully
        if result.returncode != 0:
            st.error(f"Error while running the notebook: {result.stderr}")
        else:
            st.success("Model files generated successfully!")


# Load the models if they exist
def load_models():
    global movies, movies_names, similarity

    if os.path.exists("movies.pkl") and os.path.exists("similarity.pkl"):
        movies = pickle.load(open("movies.pkl", "rb"))
        similarity = pickle.load(open("similarity.pkl", "rb"))
        
        return movies, similarity

    return None, None


# Movie recommendation logic
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:6
    ]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# Streamlit UI
st.title("Movie Recommendation System")

#Step 1: Ensure models are loaded or generated
with st.spinner("Checking files..."):
    check_and_run_notebook()
    
with st.spinner("Loading files..."):
    movies, similarity = load_models()
    movies_names = movies["title"].values

# Step 2: Show the appropriate status message
if movies is not None and similarity is not None:
    selected_movie_name = st.selectbox("Which movie do you like?", movies_names)

    if st.button("Recommend"):
        recommendations = recommend(selected_movie_name)

        for i in recommendations:
            st.write(i)
else:
    st.error(
        "Model and similarity files are not found. Please check the notebook generation process."
    )
