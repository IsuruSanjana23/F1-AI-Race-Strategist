import pandas as pd

df = pd.read_csv('../data/clean/medium.csv')

team_name = 'Mercedes'

team_df = df[df['Team']==team_name]

team_df['Stint'] = (
    team_df
    .groupby('Driver')['Compound']
    .transform(
        lambda x:
        (x != x.shift()).cumsum()
    )
)
print(
    team_df[
        [
            'Driver',
            'LapNumber',
            'Compound',
            'TyreLife',
            'Stint',
            'LapTimeSec'
        ]
    ]
)
import matplotlib.pyplot as plt

plt.scatter(team_df['TyreLife'] , team_df['LapTimeSec'])
plt.xlabel('TyreLife')
plt.ylabel('LapTimeSec')
plt.show()