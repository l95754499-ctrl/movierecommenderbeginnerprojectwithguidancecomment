# Movie Recommender System - Project Documentation
knowlege of python coding reading and documentation of basics of data analysis and maths intution behind the problem

you look the live link of given project and make your own change to make better and deploy 
online and show link on resume with descrition of the project
S-situation
T-task
A-Action
R-Result
The STAR Breakdown
Situation: Users often face decision fatigue when trying to find movies to watch out of thousands of available options.
Task: Build a machine learning recommendation engine that suggests 5 highly relevant movies based on a user's selected movie, utilizing the TMDB dataset of 5,000+ movies.
Action:
Preprocessed complex, unstructured JSON data (genres, keywords, cast, and crew) using Python and Pandas.
Combined extracted text attributes into unified tags and mapped them to a multi-dimensional vector space using Scikit-Learn’s CountVectorizer (Bag-of-Words NLP technique).
Applied the mathematical concept of Cosine Similarity to compute distances between 5,000 movie vectors, ranking them to find nearest neighbors.
Built an interactive frontend using Streamlit and integrated the TMDB REST API to fetch and display dynamic movie posters in real-time.
Result: Successfully deployed a fast, end-to-end machine learning web application online, demonstrating the ability to take a data science problem from raw data cleaning all the way to a production-ready UI.

kaggle data set data anlysis using jupyter notebook
install required python modules and deploy it online using steam lit

This document explains the technical details, mathematical intuition, and deployment strategies for the Movie Recommender System project. It also provides a roadmap for upgrading this project to a production-level portfolio piece for your resume.

---

## 1. How the Project Works (Intuition, Math, Tech, and Tools)

### **Intuition**
The project is a **Content-Based Recommender System**. The core idea is that if a user likes a particular movie, they will also like other movies that are similar to it in terms of content (e.g., genre, cast, crew, keywords, and overview). 

### **Mathematical Concept: Cosine Similarity**
To find "similar" movies, we represent each movie as a vector in a multi-dimensional space. The text data (overview, genres, keywords, cast, crew) is combined into a single "tags" string for each movie and then transformed into vectors using a technique like **Bag of Words** (`CountVectorizer` or `TF-IDF`).

Once we have vectors for all movies, we calculate the **Cosine Similarity** between them. Cosine similarity measures the cosine of the angle between two vectors:
* **Value of 1 (Angle = 0°):** The vectors are identical (the movies are exactly the same).
* **Value of 0 (Angle = 90°):** The vectors are orthogonal (no similarity).
By sorting these similarity scores in descending order, we can fetch the top 5 most similar movies for any given movie.

### **Tech Stack & Tools**
- **Python:** The primary programming language used.
- **Pandas & NumPy:** For data manipulation, cleaning, and preprocessing (extracting features from JSON formats in the TMDB dataset).
- **Scikit-Learn (sklearn):** For text vectorization (`CountVectorizer`) and calculating cosine similarity.
- **Streamlit:** A fast and easy way to create a web application UI for data science projects.
- **TMDB API:** Used to dynamically fetch movie posters based on the movie ID.
- **Pickle:** To serialize (save) and deserialize (load) the trained models (`movie_list.pkl` and `similarity.pkl`) so we don't have to compute similarities on the fly.

---

## 2. Upgrading to a Production-Level Portfolio Project

To make this project stand out on your resume, consider implementing the following production-level features:

### **A. Architecture & Engineering**
- **Modular Code:** Refactor `app.py` into multiple files (e.g., `api.py` for TMDB calls, `model.py` for recommendation logic, `ui.py` for Streamlit layout).
- **Caching:** Use Streamlit's `@st.cache_data` or `@st.cache_resource` for loading the heavy `.pkl` files and caching API responses to improve load times.
- **Hybrid Recommender:** Combine the current content-based filtering with **Collaborative Filtering** (using user ratings).
- **Vector Database:** Instead of storing similarity in a massive pickle file, use a vector database like **Pinecone, Milvus, or Qdrant** to search for nearest neighbors efficiently.

### **B. UI/UX Improvements**
- Upgrade deprecated Streamlit functions (change `st.beta_columns` to `st.columns`).
- Add a hero section, better typography, CSS styling (via `st.markdown(unsafe_allow_html=True)`), and a "Loading..." spinner while fetching posters.
- Include more details like Movie Ratings, Release Date, Cast details, and a Trailer link.

### **C. DevOps & MLOps**
- **Dockerization:** Write a `Dockerfile` to containerize the app.
- **CI/CD Pipeline:** Use GitHub Actions to automatically test and deploy your app when you push changes.
- **Logging & Monitoring:** Implement Python's `logging` module to track API errors or missing posters.

---

## 3. How to Host It Online for Free

You can host this project completely for free using **Streamlit Community Cloud**, which is the easiest platform for Streamlit apps.

### **Steps to Deploy on Streamlit Cloud:**
1. **Push Code to GitHub:**
   - Create a GitHub repository and push your project files (`app.py`, notebook, `.pkl` files, and `requirements.txt`).
   - *Note:* If your `similarity.pkl` is larger than 100MB, you need to use **Git LFS (Large File Storage)** or compress the matrix.
2. **Create a `requirements.txt` file:**
   - Ensure you have a file listing all dependencies. It should look like this:
     ```text
     streamlit==1.28.0
     pandas
     requests
     scikit-learn
     ```
3. **Deploy via Streamlit:**
   - Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
   - Click **"New app"**.
   - Select your repository, the branch (`main`), and the main file path (`app.py`).
   - Click **"Deploy!"**
   - In a few minutes, your app will be live with a shareable public URL.

*(Alternative free hosting options include Render or Hugging Face Spaces).*

---

## 4. Configuration, API, and Versioning Setup

### **API Setup (TMDB)**
1. Go to [The Movie Database (TMDB)](https://www.themoviedb.org/) and create an account.
2. Go to your account settings -> **API** -> Request an API Key (Developer).
3. Replace the hardcoded API key in `app.py` with your personal key, or better yet, use environment variables:
   - In Streamlit Cloud, add the key in **Advanced Settings -> Secrets**.
   - In code: `api_key = st.secrets["TMDB_API_KEY"]`

### **Python Versioning**
- Recommended Python version: **Python 3.8 to 3.10**.
- Avoid using very old versions (like 3.7) as Streamlit support might be deprecated.

### **Running Locally**
To run this project on your local machine:
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `streamlit run app.py`

deployment guidance
Push Your Code to GitHub
Streamlit Cloud deploys directly from a GitHub repository.

Create a free account on GitHub if you don't have one.
Create a new repository (e.g., movie-recommender-system).
Upload the following files to your new GitHub repository:
app.py
requirements.txt
DOCUMENTATION.md
The model folder containing movie_list.pkl and similarity.pkl (Note: GitHub has a 100MB file limit. If your similarity.pkl is larger than 100MB, let me know, and I can help you compress it).
Step 3: Deploy on Streamlit Community Cloud
Go to Streamlit Community Cloud and click "Continue with GitHub" to log in.
Click the "New app" button.
If prompted, authorize Streamlit to access your GitHub repositories.
In the deployment configuration:
Repository: Select your movie-recommender-system repository.
Branch: main (or master).
Main file path: app.py
Click "Deploy!"
Streamlit will spin up a server, install the dependencies from the requirements.txt, and launch your app. You'll get a public URL (like https://your-movie-recommender.streamlit.app/) that you can share on your resume or portfolio!

Let me know if you need help compressing the .pkl files or if you run into any issues getting the GitHub repository set up.
---
*End of Documentation*
