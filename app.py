import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    """
    Fetches the movie poster from The Movie Database (TMDB) API.
    
    Args:
        movie_id (int): The TMDB movie ID.
        
    Returns:
        str: The full URL path to the movie poster image.
    """
    # Make a GET request to the TMDB API using the movie ID and a provided API key
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json() # Parse the JSON response
    
    # Extract the poster path from the JSON data
    poster_path = data['poster_path']
    
    # Construct the full URL for the image
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    """
    Recommends top 5 similar movies based on cosine similarity.
    
    Args:
        movie (str): The name of the movie selected by the user.
        
    Returns:
        tuple: Two lists containing recommended movie names and their corresponding poster URLs.
    """
    # Find the index of the selected movie in the dataframe
    index = movies[movies['title'] == movie].index[0]
    
    # Get similarity scores for this movie with all other movies
    # Enumerate helps to keep track of the original index after sorting
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    recommended_movie_posters = []
    
    # Get the top 5 most similar movies (skipping the first one as it's the movie itself)
    for i in distances[1:6]:
        # fetch the movie poster using the movie ID
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        
        # append the movie title to the recommendations list
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


# --- Streamlit Web App UI ---
# To host on website
# Set the title/header of the web application
st.header('Movie Recommender System')

# Load the precomputed movie list and similarity matrix from pickle files
# Note: Ensure that the 'model' directory exists and contains these files.
movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

# Extract only the movie titles for the dropdown menu
movie_list = movies['title'].values

# Create a dropdown select box for the user to pick a movie
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# When the user clicks the 'Show Recommendation' button, execute the recommendation logic
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    # Create 5 columns to display the top 5 recommended movies and their posters
    col1, col2, col3, col4, col5 = st.beta_columns(5) # Note: 'beta_columns' is deprecated in newer Streamlit versions, consider using 'st.columns(5)' instead.
    
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])




