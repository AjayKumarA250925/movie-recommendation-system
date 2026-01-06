# Movie Recommendation System

A content-based movie recommendation system built with Python, Streamlit, and machine learning. This app recommends movies similar to your selection using TF-IDF vectorization and cosine similarity.

## Features

- Content-based filtering using movie metadata (genres, keywords, cast, crew, overview)
- TF-IDF vectorization for text feature extraction
- Cosine similarity for finding similar movies
- Interactive web interface built with Streamlit
- Movie poster display using TMDb API
- 5000+ movies in the database

## Technologies Used

- **Python 3.8+**
- **Streamlit** - Web interface
- **Pandas** - Data manipulation
- **Scikit-learn** - TF-IDF vectorization and cosine similarity
- **TMDb API** - Movie posters and metadata

## Project Structure

```
movie_recommendation/
│
├── app.py                              # Streamlit web application
├── Movie_recommendation_system.ipynb   # Data processing and model building
├── requirements.txt                     # Python dependencies
├── setup_instructions.md               # Detailed setup guide
├── README.md                           # This file
│
├── tmdb_5000_movies.csv               # Dataset (to be downloaded)
├── tmdb_5000_credits.csv              # Dataset (to be downloaded)
│
├── movies.pkl                         # Processed movie data (generated)
└── similarity.pkl                     # Similarity matrix (generated)
```

## Installation

### 1. Clone or Download this Repository

```bash
cd movie_recommendation
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Download the Dataset

Download the TMDb 5000 Movie Dataset from Kaggle:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Place these files in the project root:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

### 4. Get TMDb API Key

1. Create a free account at https://www.themoviedb.org/
2. Go to Settings > API
3. Request an API key (Developer option)
4. Copy your API key

### 5. Configure API Key

Open [app.py](app.py) and replace `YOUR_API_KEY` with your actual TMDb API key (line 32).

### 6. Build the Recommendation Model

Open and run all cells in `Movie_recommendation_system.ipynb`. This will:
- Load and merge the datasets
- Extract and process features (genres, keywords, cast, crew, overview)
- Create TF-IDF vectors
- Calculate cosine similarity matrix
- Save the processed data as `movies.pkl` and `similarity.pkl`

### 7. Run the Streamlit App

```bash
streamlit run app.py
```

The app will open at http://localhost:8501

## How It Works

### Content-Based Filtering

The recommendation system uses content-based filtering, which suggests movies similar to a given movie based on its features:

1. **Feature Extraction**: Combines movie overview, genres, keywords, top 3 cast members, and director into a single "tags" feature
2. **Text Vectorization**: Uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert text into numerical vectors
3. **Similarity Calculation**: Computes cosine similarity between all movie vectors
4. **Recommendation**: Returns the top 5 most similar movies based on cosine similarity scores

### Algorithm Details

- **TF-IDF Vectorizer**: Extracts 5000 most important features, removes English stop words
- **Cosine Similarity**: Measures similarity between movie vectors (0 = completely different, 1 = identical)
- **Top-N Selection**: Returns 5 movies with highest similarity scores (excluding the input movie itself)

## Usage

1. Launch the app using `streamlit run app.py`
2. Select a movie from the dropdown menu
3. Click "Get Recommendations"
4. View 5 similar movie recommendations with posters

## Dataset Information

- **Source**: TMDb 5000 Movie Dataset
- **Movies**: ~4800 movies (after preprocessing)
- **Features Used**:
  - Overview (plot summary)
  - Genres
  - Keywords
  - Cast (top 3 actors)
  - Director
  - Movie ID (for poster fetching)

## Example Recommendations

**Input**: Avatar
**Output**:
- Guardians of the Galaxy
- Star Trek Into Darkness
- John Carter
- Star Trek Beyond
- Aliens

## Customization

### Change Number of Recommendations

In [app.py](app.py#L36), modify the slice in the recommendation function:

```python
movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
# Change [1:6] to [1:11] for 10 recommendations
```

### Modify TF-IDF Features

In [Movie_recommendation_system.ipynb](Movie_recommendation_system.ipynb), adjust the vectorizer parameters:

```python
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
# Increase max_features for more detailed analysis
# Remove stop_words parameter to include all words
```

## Troubleshooting

### Model files not found
Run all cells in `Movie_recommendation_system.ipynb` to generate `movies.pkl` and `similarity.pkl`

### Posters not loading
Check that your TMDb API key is correctly configured in [app.py](app.py#L32)

### Dataset not found
Download the TMDb datasets from Kaggle and place them in the project root directory

## Future Enhancements

- [ ] Add collaborative filtering for hybrid recommendations
- [ ] Include movie ratings and popularity in the algorithm
- [ ] Add genre-based filtering
- [ ] Implement search functionality
- [ ] Add movie details and trailers
- [ ] Deploy to cloud (Streamlit Cloud, Heroku, etc.)

## License

This project is open source and available for educational purposes.

## Credits

- Dataset: [TMDb 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Movie Data & Posters: [The Movie Database (TMDb)](https://www.themoviedb.org/)
- Reference: Based on content-based filtering techniques

## Contact

For questions or suggestions, please open an issue in the repository.
