import requests
import pandas as pd
import time

API_KEY = os.getenv('TMDB_API_KEY', 'YOUR_KEY_HERE')
BASE_URL = "https://api.themoviedb.org/3"

# 11 Canon MCU TV series (2021-2025)
mcu_tv_series = [
    "WandaVision",
    "The Falcon and the Winter Soldier",
    "Loki",
    "Hawkeye",
    "Moon Knight",
    "Ms. Marvel",
    "She-Hulk: Attorney at Law",
    "Secret Invasion",
    "Agatha All Along",
    "Echo",
    "Daredevil: Born Again",
]

tv_data = []

print("Fetching MCU TV series from TMDB...\n")

for series_title in mcu_tv_series:
    search_url = f"{BASE_URL}/search/tv?api_key={API_KEY}&query={series_title}"
    
    try:
        search_response = requests.get(search_url)
        search_response.raise_for_status()
        search_results = search_response.json()['results']
        
        if not search_results:
            print(f"✗ Not found: {series_title}")
            continue
        
        # Get first result
        series = search_results[0]
        series_id = series['id']
        
        # Fetch full details
        detail_url = f"{BASE_URL}/tv/{series_id}?api_key={API_KEY}&language=en-US"
        detail_response = requests.get(detail_url)
        detail_response.raise_for_status()
        series_detail = detail_response.json()
        
        series_info = {
            'id': series_detail.get('id'),
            'title': series_detail.get('name'),
            'first_air_date': series_detail.get('first_air_date'),
            'number_of_seasons': series_detail.get('number_of_seasons'),
            'number_of_episodes': series_detail.get('number_of_episodes'),
            'vote_average': series_detail.get('vote_average'),
            'popularity': series_detail.get('popularity'),
            'status': series_detail.get('status'),
        }
        
        tv_data.append(series_info)
        print(f"✓ {series_detail.get('name')} (ID: {series_id}) - {series_detail.get('first_air_date', 'N/A')[:4]}")
        
        time.sleep(0.25)
        
    except Exception as e:
        print(f"✗ Error fetching {series_title}: {e}")

# Save to CSV
df = pd.DataFrame(tv_data)
df = df.sort_values('first_air_date')
df.to_csv('mcu_tv_series.csv', index=False)

print(f"\n✓ SUCCESS! Fetched {len(tv_data)} MCU TV series")
print(f"✓ Saved to 'mcu_tv_series.csv'")
print("\nTV Series fetched:")
print(df[['title', 'first_air_date', 'number_of_episodes']].to_string(index=False))