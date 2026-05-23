import pandas as pd

df = pd.read_csv('../data/raw/bahrain_fp2_2022.csv')

# Keep accurate laps
df = df[df['IsAccurate']==True]

# Remove missing lap times
df = df.dropna(
    subset=['LapTime']
)

# Convert lap times
df['LapTime'] = pd.to_timedelta(
    df['LapTime']
)

df['LapTimeSec'] = (
    df['LapTime']
    .dt.total_seconds()
)

# Create stints per driver
df['Stint']=(
    df.groupby('Driver')
    ['Compound']
    .transform(
        lambda x:
        (x!=x.shift())
        .cumsum()
    )
)

clean_runs=[]

for driver in df['Driver'].unique():

    driver_df=df[
        df['Driver']==driver
        ]

    for stint in driver_df[
        'Stint'
    ].unique():

        stint_df=driver_df[
            driver_df['Stint']==stint
            ].copy()

        # Ignore tiny stints
        if len(stint_df)<4:
            continue

        # Calculate IQR inside this stint only
        Q1=stint_df[
            'LapTimeSec'
        ].quantile(0.25)

        Q3=stint_df[
            'LapTimeSec'
        ].quantile(0.75)

        IQR=Q3-Q1

        lower=Q1-(1.5*IQR)
        upper=Q3+(1.5*IQR)

        stint_df=stint_df[
            (stint_df['LapTimeSec']>=lower)
            &
            (stint_df['LapTimeSec']<=upper)
            ]

        clean_runs.append(
            stint_df
        )

# Merge cleaned data
df=pd.concat(
    clean_runs
)

df=df.reset_index(
    drop=True
)

df.to_csv(f'../data/clean/final_clean',index=False)

# Save tire files
""""
for tyre in df[
    'Compound'
].unique():

    tyre_df=df[
        df['Compound']==tyre
        ]

    filename=(
            tyre.lower()
            +'.csv'
    )

    tyre_df.to_csv(
        f'../data/clean/{filename}',
        index=False
    )

    print(
        f"Saved {filename}"
    )

"""