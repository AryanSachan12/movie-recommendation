# Movie Recommendation System

This is a web-based movie recommendation system built with **Streamlit**, **Python**, and **Machine Learning**. The application uses content-based filtering to recommend movies based on the user's selection.

## Demo

You can try out the live demo of the Movie Recommendation System here:

[Movie Recommendation System - Live Demo](https://aryansachan12-movie-recommendation-app-pomfkx.streamlit.app/)

## Features

- **Movie Recommendations**: Select a movie from a list, and get recommendations based on movie similarity.
- **Content-Based Filtering**: The system uses movie metadata to find similarities between movies and suggest movies accordingly.
- **Real-time Model Loading**: If the model files (`movies.pkl` and `similarity.pkl`) do not exist, the app will automatically run a Jupyter notebook to generate them.

## Installation

### Prerequisites

To run the application locally, you will need to have the following libraries installed:

- Python 3.x
- Streamlit
- Pickle
- Pandas
- Jupyter

### Steps to Run the Project Locally

1. Clone the repository:
    ```bash
    git clone [<repository_url>](https://github.com/AryanSachan12/movie-recommendation.git)
    ```

2. Install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

The app will be available at `http://localhost:8501` in your browser.

## How It Works

- **Movie Dataset**: The application uses a movie dataset that includes information such as movie titles, descriptions, genres, and other relevant features.
- **Model Generation**: When the app starts, it checks for the existence of the model and similarity pickle files (`movies.pkl` and `similarity.pkl`). If these files don't exist, the app automatically runs a Jupyter notebook (`model_training.ipynb`) to generate them.
- **Recommendation Logic**: The content-based recommendation engine compares the movie selected by the user to others in the dataset using a similarity matrix and suggests the most similar movies.

## Files Included

- `app.py`: The main Streamlit app for the movie recommendation system.
- `model_training.ipynb`: A Jupyter notebook for training and saving the recommendation models.
- `movies.pkl`: The pickled dataset of movie information (generated after running the notebook).
- `similarity.pkl`: The pickled similarity matrix of movies (generated after running the notebook).

## Future Improvements

- Integrate additional recommendation algorithms such as collaborative filtering.
- Add user feedback and ratings to improve recommendation accuracy.
- Improve the user interface for better experience.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
