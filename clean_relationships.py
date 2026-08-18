import pandas as pd
import re

# Read the CSV
df = pd.read_csv('character_relationships_complete_correction_needed.csv')

print(f"Starting with {len(df)} rows\n")

# List of vague/non-person characters to remove
vague_characters = [
    'The Avengers', 'Avengers', 'S.H.I.E.L.D.', 'S.H.I.E.L.D. Agents',
    'The Hulk', 'Tesseract', 'Greater Threat', 'Unexpected Enemy',
    'Invisible Villain', 'City of New York', 'Loved Ones', 'Old Friends',
    'Classmates', 'Family', 'US Government', 'Ten Rings', 'Presence from Past',
    'Warriors Three', 'Clint\'s Family', 'Asgardian Warriors'
]

# Remove rows where character_1 or character_2 is vague
before = len(df)
df = df[~df['character_1'].isin(vague_characters)]
df = df[~df['character_2'].isin(vague_characters)]
after = len(df)
print(f"✓ Removed vague characters: {before - after} rows\n")

# Standardize character names
name_mappings = {
    'Tony Stark': 'Tony Stark',
    'Iron Man': 'Tony Stark',
    'Bruce Banner': 'Bruce Banner',
    'The Hulk': 'Bruce Banner',
    'Thor': 'Thor Odinson',
    'Thor Odinson': 'Thor Odinson',
    'Steve Rogers': 'Steve Rogers',
    'Captain America': 'Steve Rogers',
    'Natasha Romanoff': 'Natasha Romanoff',
    'Black Widow': 'Natasha Romanoff',
    'Clint Barton': 'Clint Barton',
    'Hawkeye': 'Clint Barton',
    'Wanda Maximoff': 'Wanda Maximoff',
    'Scarlet Witch': 'Wanda Maximoff',
    'Vision': 'Vision',
    'Sam Wilson': 'Sam Wilson',
    'Falcon': 'Sam Wilson',
    'Bucky Barnes': 'Bucky Barnes',
    'Winter Soldier': 'Bucky Barnes',
    'Peter Parker': 'Peter Parker',
    'Spider-Man': 'Peter Parker',
}

# Apply mappings
for old_name, new_name in name_mappings.items():
    df['character_1'] = df['character_1'].replace(old_name, new_name)
    df['character_2'] = df['character_2'].replace(old_name, new_name)

print(f"✓ Standardized character names\n")

# Remove duplicates (keep first occurrence)
before = len(df)
df = df.drop_duplicates(subset=['media_type', 'title', 'character_1', 'character_2', 'relationship'], keep='first')
after = len(df)
print(f"✓ Removed duplicates: {before - after} rows\n")

# Remove rows with empty character names
before = len(df)
df = df[(df['character_1'].notna()) & (df['character_2'].notna())]
df = df[(df['character_1'] != '') & (df['character_2'] != '')]
after = len(df)
print(f"✓ Removed empty character names: {before - after} rows\n")

# Add manual Avengers relationships
avengers_relationships = [
    # The Avengers - main team members
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Tony Stark', 'character_2': 'Steve Rogers', 'relationship': 'ally', 'description': 'Team members brought together by S.H.I.E.L.D. to fight Loki', 'source': 'Manual'},
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Tony Stark', 'character_2': 'Thor Odinson', 'relationship': 'ally', 'description': 'Team members working together to stop Loki\'s invasion', 'source': 'Manual'},
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Tony Stark', 'character_2': 'Bruce Banner', 'relationship': 'ally', 'description': 'Team members brought together to fight the common threat', 'source': 'Manual'},
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Tony Stark', 'character_2': 'Natasha Romanoff', 'relationship': 'ally', 'description': 'S.H.I.E.L.D. agent and Iron Man team up against Loki', 'source': 'Manual'},
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Tony Stark', 'character_2': 'Clint Barton', 'relationship': 'ally', 'description': 'S.H.I.E.L.D. agent and Iron Man work together as Avengers', 'source': 'Manual'},
    
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Steve Rogers', 'character_2': 'Thor Odinson', 'relationship': 'ally', 'description': 'First meeting as Avengers teammates against Loki', 'source': 'Manual'},
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Steve Rogers', 'character_2': 'Bruce Banner', 'relationship': 'ally', 'description': 'Captain America and Hulk team up as Avengers', 'source': 'Manual'},
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Steve Rogers', 'character_2': 'Natasha Romanoff', 'relationship': 'ally', 'description': 'S.H.I.E.L.D. agent Black Widow fights alongside Captain America', 'source': 'Manual'},
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Steve Rogers', 'character_2': 'Clint Barton', 'relationship': 'ally', 'description': 'Avengers teammates working together to save Earth', 'source': 'Manual'},
    
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Thor Odinson', 'character_2': 'Bruce Banner', 'relationship': 'ally', 'description': 'Asgardian and Hulk form alliance against Loki', 'source': 'Manual'},
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Thor Odinson', 'character_2': 'Natasha Romanoff', 'relationship': 'ally', 'description': 'S.H.I.E.L.D. agent and Thor work as Avengers teammates', 'source': 'Manual'},
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Thor Odinson', 'character_2': 'Clint Barton', 'relationship': 'ally', 'description': 'Asgardian and Hawkeye fight together as Avengers', 'source': 'Manual'},
    
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Bruce Banner', 'character_2': 'Natasha Romanoff', 'relationship': 'ally', 'description': 'Black Widow brings Hulk into Avengers team', 'source': 'Manual'},
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Bruce Banner', 'character_2': 'Clint Barton', 'relationship': 'ally', 'description': 'Hulk and Hawkeye work together against Loki\'s army', 'source': 'Manual'},
    
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Natasha Romanoff', 'character_2': 'Clint Barton', 'relationship': 'ally', 'description': 'S.H.I.E.L.D. agents and longtime partners fight as Avengers', 'source': 'Manual'},
    
    # Villain
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Loki', 'character_2': 'Tony Stark', 'relationship': 'enemy', 'description': 'Loki is the primary antagonist opposing the Avengers', 'source': 'Manual'},
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Loki', 'character_2': 'Steve Rogers', 'relationship': 'enemy', 'description': 'Loki conflicts with Captain America and the Avengers', 'source': 'Manual'},
    {'order': 6, 'media_type': 'Movie', 'title': 'The Avengers', 'character_1': 'Loki', 'character_2': 'Thor Odinson', 'relationship': 'enemy', 'description': 'Loki is Thor\'s adopted brother, now his enemy', 'source': 'Manual'},
]

avengers_df = pd.DataFrame(avengers_relationships)
df = pd.concat([df, avengers_df], ignore_index=True)

print(f"✓ Added {len(avengers_df)} manual Avengers relationships\n")

# Sort and save
df = df.sort_values(['order', 'title']).reset_index(drop=True)
df.to_csv('character_relationships_cleaned.csv', index=False)

print(f"{'='*60}")
print(f"✓ DATA CLEANING COMPLETE")
print(f"{'='*60}")
print(f"Final dataset: {len(df)} rows")
print(f"Quality improvements:")
print(f"  - Removed vague/abstract characters")
print(f"  - Standardized character names")
print(f"  - Removed duplicates")
print(f"  - Added Avengers team relationships")
print(f"\nSample of cleaned data:")
print(df[['media_type', 'title', 'character_1', 'character_2', 'relationship']].head(20))