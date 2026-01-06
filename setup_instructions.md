# Setup Instructions

## 1. Download the Dataset

You need the TMDb 5000 Movie Dataset. You can download it from:
- **Kaggle**: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Download these two files and place them in the project root:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

## 2. Get TMDb API Key

To fetch movie posters, you need a TMDb API key:

1. Go to https://www.themoviedb.org/
2. Create a free account
3. Go to Settings > API
4. Request an API key (choose "Developer" option)
5. Fill in the required information
6. Copy your API key

## 3. Update the API Key

Open `app.py` and replace `YOUR_API_KEY` on line 32 with your actual TMDb API key:

```python
url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_ACTUAL_API_KEY&language=en-US"
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## 5. Run the Jupyter Notebook

Open and run `Movie_recommendation_system.ipynb` to:
- Load and preprocess the data
- Build the recommendation model
- Generate `movies.pkl` and `similarity.pkl` files

## 6. Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your default browser at http://localhost:8501
