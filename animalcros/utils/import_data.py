import pandas as pd
import os

def preprocess_collectables():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fish_path = os.path.join(base_dir, '../data/fish.csv')
    insect_path = os.path.join(base_dir, '../data/insects.csv')
    sea_path = os.path.join(base_dir, '../data/seaCreatures.csv')

    # Load each CSV
    fish_df = pd.read_csv(fish_path)
    fish_df['type'] = 'fish'

    insects_df = pd.read_csv(insect_path)
    insects_df['type'] = 'insect'

    sea_critters_df = pd.read_csv(sea_path)
    sea_critters_df['type'] = 'seaCreature'

    # Normalize column names
    rename_map = {
        "Name": "name",
        "Sell": "price",
        "Icon Image": "image",
        "Critterpedia Description": "description"
    }

    for df in [fish_df, insects_df, sea_critters_df]:
        df.rename(columns=rename_map, inplace=True)

    all_columns = set(fish_df.columns) | set(insects_df.columns) | set(sea_critters_df.columns)
    fish_df = fish_df.reindex(columns=all_columns)
    insects_df = insects_df.reindex(columns=all_columns)
    sea_critters_df = sea_critters_df.reindex(columns=all_columns)

    combined_df = pd.concat([fish_df, insects_df, sea_critters_df], ignore_index=True)

    return combined_df
