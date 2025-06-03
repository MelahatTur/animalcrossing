import pandas as pd

# Load each CSV
fish_df = pd.read_csv('animalcros/data/fish.csv')
fish_df['type'] = 'fish'

insects_df = pd.read_csv('animalcros/data/insects.csv')
insects_df['type'] = 'insect'

sea_critters_df = pd.read_csv('animalcros/data/seaCreatures.csv')
sea_critters_df['type'] = 'seaCreature'

# Get full column set
all_columns = set(fish_df.columns) | set(insects_df.columns) | set(sea_critters_df.columns)

# Reindex all to have same columns
fish_df = fish_df.reindex(columns=all_columns)
insects_df = insects_df.reindex(columns=all_columns)
sea_critters_df = sea_critters_df.reindex(columns=all_columns)

# Combine all
combined_df = pd.concat([fish_df, insects_df, sea_critters_df], ignore_index=True)

# Save combined CSV or process further
combined_df.to_csv('animalcros/data/combined_collectables.csv', index=False)