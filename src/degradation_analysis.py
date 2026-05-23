import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor

# Get the absolute path to the data file
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_dir, '../data/clean/final_clean')

df = pd.read_csv(data_file)

team_name='Mercedes'

team_df=df[
    df['Team']==team_name
    ]

results=[]


# Loop through compounds
for compound in team_df[
    'Compound'
].unique():

    compound_df=team_df[
        team_df['Compound']==compound
        ]

    driver_results=[]


    # Driver loop
    for driver in compound_df[
        'Driver'
    ].unique():

        driver_df=compound_df[
            compound_df['Driver']==driver
            ]


        # Stint loop
        for stint in driver_df[
            'Stint'
        ].unique():

            stint_df=driver_df[
                driver_df['Stint']==stint
                ]

            if len(stint_df)<5:
                continue


            X=stint_df[
                ['TyreLife']
            ]

            y=stint_df[
                'LapTimeSec'
            ]


            # -------- Linear --------

            linear=LinearRegression()

            linear.fit(
                X,
                y
            )

            linear_pred=linear.predict(
                X
            )

            linear_r2=r2_score(
                y,
                linear_pred
            )


            # -------- Polynomial --------

            poly=Pipeline([

                (
                    'poly',
                    PolynomialFeatures(
                        degree=2
                    )
                ),

                (
                    'model',
                    LinearRegression()
                )

            ])

            poly.fit(
                X,
                y
            )

            poly_pred=poly.predict(
                X
            )

            poly_r2=r2_score(
                y,
                poly_pred
            )


            # -------- Random Forest --------

            rf=RandomForestRegressor(

                n_estimators=100,

                random_state=42

            )

            rf.fit(
                X,
                y
            )

            rf_pred=rf.predict(
                X
            )

            rf_r2=r2_score(
                y,
                rf_pred
            )


            driver_results.append({

                'Driver':driver,

                'Compound':compound,

                'Stint':stint,

                'NumLaps':
                    len(stint_df),

                'Linear_R2':
                    linear_r2,

                'Poly_R2':
                    poly_r2,

                'RF_R2':
                    rf_r2,

                'Linear_DegRate':
                    linear.coef_[0]

            })



    driver_results=pd.DataFrame(
        driver_results
    )

    if len(driver_results)==0:
        continue


    # Weighted averages

    weighted_deg=(

            (
                    driver_results[
                        'Linear_DegRate'
                    ]

                    *

                    driver_results[
                        'NumLaps'
                    ]

            ).sum()

            /

            driver_results[
                'NumLaps'
            ].sum()

    )


    weighted_linear_r2=(

            (
                    driver_results[
                        'Linear_R2'
                    ]

                    *

                    driver_results[
                        'NumLaps'
                    ]

            ).sum()

            /

            driver_results[
                'NumLaps'
            ].sum()

    )


    weighted_poly_r2=(

            (
                    driver_results[
                        'Poly_R2'
                    ]

                    *

                    driver_results[
                        'NumLaps'
                    ]

            ).sum()

            /

            driver_results[
                'NumLaps'
            ].sum()

    )


    weighted_rf_r2=(

            (
                    driver_results[
                        'RF_R2'
                    ]

                    *

                    driver_results[
                        'NumLaps'
                    ]

            ).sum()

            /

            driver_results[
                'NumLaps'
            ].sum()

    )


    results.append({

        'Compound':compound,

        'Linear_R2':
            weighted_linear_r2,

        'Poly_R2':
            weighted_poly_r2,

        'RF_R2':
            weighted_rf_r2,

        'Linear_DegRate':
            weighted_deg

    })


results=pd.DataFrame(
    results
)

print(
    f"\nTeam Degradation: {team_name}"
)

print(results)

results.to_csv(

    os.path.join(
        script_dir,
        '../data/clean/team_degradation.csv'
    ),

    index=False

)