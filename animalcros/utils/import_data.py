#extract data from csv files and make them python readable
import os
import pandas as pd

FISH_DATASET_PATH = os.path.join('/ac', 'data', 'fish.csv')
INSECTS_DATASET_PATH = os.path.join('/ac', 'data', 'insects.csv')
SEA_CREATURES_DATASET_PATH = os.path.join('/ac', 'data', 'seacreatures.csv')


#when getting image split such that link name