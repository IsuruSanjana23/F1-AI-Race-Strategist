import pandas as pd
import os
from itertools import permutations

# ==========================================
# Paths
# ==========================================

script_dir = os.path.dirname(
    os.path.abspath(__file__)
)

deg_file = os.path.join(
    script_dir,
    '../data/clean/team_degradation.csv'
)

deg = pd.read_csv(
    deg_file
)

# ==========================================
# Constants
# ==========================================

TOTAL_LAPS = 57
PIT_PENALTY = 22
BASE_PACE = 97
team_name = 'Mercedes'


# ==========================================
# Missing degradation estimation
# ==========================================

def estimate_missing_deg(compound):

    available=deg.set_index(
        'Compound'
    )

    if compound=="HARD":

        if "MEDIUM" in available.index:

            return (
                    available.loc[
                        "MEDIUM",
                        "Linear_DegRate"
                    ]*0.7
            )

    elif compound=="SOFT":

        if "MEDIUM" in available.index:

            return (
                    available.loc[
                        "MEDIUM",
                        "Linear_DegRate"
                    ]*1.4
            )

    return 0.15



# ==========================================
# Get degradation
# ==========================================

def get_deg(compound):

    tyre=deg[
        deg['Compound']==compound
        ]

    if len(tyre)>0:

        return tyre[
            'Linear_DegRate'
        ].iloc[0]

    return estimate_missing_deg(
        compound
    )


# ==========================================
# Simulate strategy
# ==========================================

def simulate_strategy(
        compounds,
        pit_laps
):

    race_time=0

    remaining=TOTAL_LAPS

    for i,compound in enumerate(
            compounds
    ):

        deg_rate=get_deg(
            compound
        )

        if i==0:

            stint_length=pit_laps[0]

        elif i==len(
                compounds
        )-1:

            stint_length=remaining

        else:

            stint_length=(
                    pit_laps[i]
                    -
                    pit_laps[i-1]
            )


        remaining-=stint_length


        for tire_age in range(
                1,
                stint_length+1
        ):

            lap_time=(

                    BASE_PACE
                    +
                    (
                            deg_rate
                            *
                            tire_age
                    )

            )

            race_time+=lap_time


        if i!=len(
                compounds
        )-1:

            race_time+=PIT_PENALTY


    return race_time



# ==========================================
# Generate all strategies
# ==========================================

compounds=[

    "SOFT",
    "MEDIUM",
    "HARD"

]

results=[]


# ---------- Two stop ----------

for strategy in permutations(
        compounds,
        2
):

    for pit1 in range(
            10,
            40
    ):

        total=simulate_strategy(

            strategy,

            [pit1]

        )

        results.append({

            'Strategy':
                "-".join(
                    strategy
                ),

            'PitLaps':
                [pit1],

            'RaceTime':
                total

        })


# ---------- Three stints ----------

for strategy in permutations(
        compounds,
        3
):

    for pit1 in range(
            10,
            25
    ):

        for pit2 in range(
                pit1+10,
                45
        ):

            total=simulate_strategy(

                strategy,

                [pit1,pit2]

            )

            results.append({

                'Strategy':
                    "-".join(
                        strategy
                    ),

                'PitLaps':
                    [pit1,pit2],

                'RaceTime':
                    total

            })


# ==========================================
# Results
# ==========================================

results=pd.DataFrame(
    results
)


results=results.sort_values(
    'RaceTime'
)


# ==========================================
# Display Results
# ==========================================

top_n = 3

print("\n" + "="*70)
print(f"{team_name:^70}")
print("F1 AI STRATEGY SIMULATION RESULTS".center(70))
print("="*70)

print("\nTop Strategies:")

for i, row in results.head(top_n).iterrows():

    print(
        f"""
Strategy      : {row['Strategy']}
Pit Lap(s)    : {row['PitLaps']}
Race Time     : {row['RaceTime']:.2f} sec
        """
    )

    print("-"*70)


# ==========================================
# Best strategy
# ==========================================

best = results.iloc[0]

print("\n" + "="*70)
print("BEST STRATEGY FOUND".center(70))
print("="*70)

print(
    f"""
Strategy           : {best['Strategy']}
Pit Lap(s)         : {best['PitLaps']}
Predicted Time     : {best['RaceTime']:.2f} sec
Confidence          : {(100-(results['RaceTime'].std()/best['RaceTime']*100)):.1f}%
"""
)

print("="*70)



results.to_csv(

    os.path.join(

        script_dir,

        '../data/clean/all_strategy_results.csv'

    ),

    index=False

)