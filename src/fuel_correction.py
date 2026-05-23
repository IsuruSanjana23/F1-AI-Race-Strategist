import pandas as pd
import os

script_dir = os.path.dirname(
    os.path.abspath(__file__)
)

df = pd.read_csv(
    os.path.join(
        script_dir,
        'final_clean'
    )
)

total_race_laps=57   # Bahrain example

df['FuelRemaining']=(
        total_race_laps
        -
        df['LapNumber']
)
fuel_loss_per_lap=0.035

df['FuelEffect']=(
        df['FuelRemaining']
        *
        fuel_loss_per_lap
)
df['CorrectedLapTime']=(
        df['LapTimeSec']
        -
        df['FuelEffect']
)

df.to_csv(
    os.path.join(
        script_dir,
        'fuel_corrected.csv'
    ),
    index=False
)