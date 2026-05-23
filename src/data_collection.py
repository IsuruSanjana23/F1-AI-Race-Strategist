import fastf1
import pandas as pd
import os

cache_dir = '../data/raw/cache'
os.makedirs(cache_dir, exist_ok=True)
fastf1.Cache.enable_cache('../data/raw/cache')  # Enable caching to speed up data retrieval

def get_session_data(year, race , session_type):
    session = fastf1.get_session(
        year,
        race,
        session_type
    )

    session.load()

    return session.laps

laps = get_session_data(2022, 'Bahrain', 'FP2')

#print(laps.head())

laps.to_csv('data/raw/bahrain_fp2_2022.csv', index=False)