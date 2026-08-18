import requests
import pandas as pd

# Your TMDB API key
API_KEY = os.getenv('TMDB_API_KEY', 'YOUR_KEY_HERE')
BASE_URL = "https://api.themoviedb.org/3"

# COMPLETE MCU movie list with CORRECT TMDB IDs
mcu_movies = {
    10138: "Iron Man",
    10195: "Captain America: The First Avenger",
    76338: "Thor",
    24428: "The Avengers",
    76339: "Thor: The Dark World",
    271110: "Captain America: The Winter Soldier",
    121856: "Guardians of the Galaxy",
    102899: "Guardians of the Galaxy Vol. 2",
    131631: "Doctor Strange",
    284052: "Spider-Man: Homecoming",
    284053: "Thor: Ragnarok",
    299536: "Avengers: Infinity War",
    299534: "Avengers: Endgame",
    363088: "Spider-Man: Far From Home",
    566525: "Spider-Man: No Way Home",
    100402: "Captain America: Civil War",
    99861: "Ant-Man",
    102531: "Ant-Man and the Wasp",
    267649: "Captain Marvel",
    100383: "Iron Man 2",
    68721: "Iron Man 3",
    70047: "The Incredible Hulk",
    120467: "Avengers: Age of Ultron",
    284054: "Doctor Strange in the Multiverse of Madness",
    370172: "Black Panther: Wakanda Forever",
    429617: "Shang-Chi and the Legend of the Ten Rings",
    524047: "Eternals",
    505642: "Black Widow",
    337339: "Thor: Love and Thunder",
    516486: "Ant-Man and the Wasp: Quantumania",
    550988: "Guardians of the Galaxy Vol. 3",
    667538: "The Marvels",
    569094: "Black Panther",
    333484: "Captain Marvel (2019)",
}

movies_data = []

print("Fetching COMPLETE MCU movie data from TMDB...")
print(f"Total movies to fetch: {len(mcu_movies)}\n")

for movie_id, movie_title in mcu_movies.items():
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        movie = response.json()
        
        # Extract relevant fields
        movie_info = {
            'id': movie.get('id'),
            'title': movie.get('title'),
            'release_date': movie.get('release_date'),
            'budget': movie.get('budget'),
            'revenue': movie.get('revenue'),
            'runtime': movie.get('runtime'),
            'vote_average': movie.get('vote_average'),
            'popularity': movie.get('popularity'),
            'genres': [g['name'] for g in movie.get('genres', [])]
        }
        
        movies_data.append(movie_info)
        print(f"✓ {movie.get('title')} ({movie.get('release_date', 'N/A')[:4]})")
        
    except Exception as e:
        print(f"✗ Error fetching {movie_title}: {e}")

# Create DataFrame and save to CSV
df = pd.DataFrame(movies_data)
df = df.sort_values('release_date')  # Sort by release date
df.to_csv('mcu_movies_complete.csv', index=False)

print(f"\n✓ SUCCESS! Fetched {len(movies_data)} MCU movies")
print(f"✓ Saved to 'mcu_movies_complete.csv'")
print("\nFirst 5 movies (chronological):")
print(df[['title', 'release_date', 'vote_average']].head())