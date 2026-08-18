import requests
import pandas as pd
import json
import time

# Your API keys
TMDB_API_KEY = os.getenv('TMDB_API_KEY', 'YOUR_KEY_HERE')
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY', 'YOUR_KEY_HERE')

# Read your movies and TV series
movies_df = pd.read_csv('mcu_movies_clean.csv')
tv_df = pd.read_csv('mcu_tv_series.csv')

# Add media_type column to distinguish
movies_df['media_type'] = 'Movie'
tv_df['media_type'] = 'TV Series'

# Combine both
all_titles = pd.concat([movies_df[['order', 'id', 'title', 'media_type']], 
                        tv_df[['order', 'id', 'title', 'media_type']]], 
                       ignore_index=True)

print(f"Extracting characters from {len(all_titles)} titles\n")

relationships = []
success_count = 0
error_count = 0

for idx, row in all_titles.iterrows():
    title = row['title']
    media_id = row['id']
    media_type = row['media_type']
    
    print(f"[{idx+1}/{len(all_titles)}] {media_type}: {title}...", end=" ")
    
    try:
        # Get plot summary from TMDB
        if media_type == 'Movie':
            tmdb_url = f"https://api.themoviedb.org/3/movie/{media_id}?api_key={TMDB_API_KEY}"
        else:
            tmdb_url = f"https://api.themoviedb.org/3/tv/{media_id}?api_key={TMDB_API_KEY}"
        
        tmdb_response = requests.get(tmdb_url)
        tmdb_response.raise_for_status()
        media_data = tmdb_response.json()
        
        # Get plot (movies use 'overview', TV uses 'overview')
        plot_summary = media_data.get('overview', 'No plot available')
        
        if not plot_summary or plot_summary == 'No plot available':
            print("✗ No plot")
            error_count += 1
            continue
        
        # Build prompt for Claude
        prompt = f"""Extract main character relationships from this {media_type.lower()} plot.

Title: {title}
Plot: {plot_summary}

Return ONLY valid JSON, no other text:

{{
    "relationships": [
        {{"character_1": "Name 1", "character_2": "Name 2", "relationship": "ally/enemy/mentor/romantic/colleague/family", "description": "Brief description"}}
    ]
}}

Extract only main characters (top 5-8). If no relationships, return empty array."""
        
        # Call Claude API
        claude_response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": CLAUDE_API_KEY,
                "content-type": "application/json",
            },
            json={
                "model": "claude-sonnet-4-6",
                "max_tokens": 1024,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
            },
        )
        
        claude_response.raise_for_status()
        response_data = claude_response.json()
        
        # Extract response text
        response_text = response_data['content'][0]['text']
        
        # Find and parse JSON
        json_start = response_text.find('{')
        json_end = response_text.rfind('}') + 1
        
        if json_start == -1 or json_end == 0:
            print("✗ No JSON")
            error_count += 1
            continue
        
        json_str = response_text[json_start:json_end]
        extracted_data = json.loads(json_str)
        
        # Save relationships
        rel_count = 0
        for rel in extracted_data.get('relationships', []):
            relationships.append({
                'order': row['order'],
                'media_type': media_type,
                'media_title': title,
                'media_id': media_id,
                'character_1': rel.get('character_1'),
                'character_2': rel.get('character_2'),
                'relationship_type': rel.get('relationship'),
                'description': rel.get('description'),
            })
            rel_count += 1
        
        print(f"✓ {rel_count} relationships")
        success_count += 1
        time.sleep(0.5)  # Respectful API usage
        
    except Exception as e:
        print(f"✗ Error: {str(e)[:50]}")
        error_count += 1
        time.sleep(0.5)

# Save to CSV
if relationships:
    relationships_df = pd.DataFrame(relationships)
    relationships_df = relationships_df.sort_values('order')
    relationships_df.to_csv('character_relationships_complete.csv', index=False)
    
    print(f"\n{'='*60}")
    print(f"✓ EXTRACTION COMPLETE")
    print(f"{'='*60}")
    print(f"Total relationships extracted: {len(relationships)}")
    print(f"Successful titles: {success_count}")
    print(f"Failed titles: {error_count}")
    print(f"Saved to: character_relationships_complete.csv")
    print(f"\nSample relationships:")
    print(relationships_df[['media_type', 'media_title', 'character_1', 'character_2', 'relationship_type']].head(15))
else:
    print("✗ No relationships extracted")