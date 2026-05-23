# F1 Pit Lap Predictor

A comprehensive data analysis and machine learning project for predicting optimal pit stop strategies and lap times in Formula 1 racing.

## Project Overview

This project analyzes Formula 1 telemetry data to predict pit stop windows, tire degradation rates, and optimize race strategies. It uses real F1 data from the FastF1 library to build models that can simulate different pit stop strategies and predict lap times based on tire age and compound.

## Features

- **Data Collection**: Automatically fetches F1 session data using the FastF1 library
- **Data Cleaning**: Comprehensive data cleaning pipeline to handle telemetry inconsistencies
- **Degradation Analysis**: Analyzes tire degradation rates for different compounds and teams
- **Long Run Detection**: Identifies extended tire stints for strategic analysis
- **Race Simulation**: Simulates different pit stop strategies to find optimal approaches
- **Consistency Filtering**: Ensures data quality and consistency across analyses
- **Visualization**: Generates insights through data visualization

## Project Structure

```
F1-pit-lap-predictor/
├── app.py                          # Main application entry point
├── main.py                         # Primary script for data processing
├── requirements.txt                # Project dependencies
├── README.md                       # This file
│
├── src/                            # Source code modules
│   ├── data_collection.py         # FastF1 data retrieval and caching
│   ├── data_cleaning.py           # Data preprocessing and cleaning
│   ├── degradation_analysis.py    # Tire degradation curve analysis
│   ├── long_run_detection.py      # Identify and analyze long tire stints
│   ├── consistency_filter.py      # Data validation and filtering
│   └── visualizing.py             # Data visualization utilities
│
├── data/                           # Data directory
│   ├── raw/                       # Raw F1 telemetry data
│   │   └── bahrain_fp2_2022.csv  # Example raw session data
│   └── clean/                     # Processed data files
│       ├── final_clean            # Complete cleaned dataset
│       ├── clean_data.csv         # Cleaned session data
│       ├── hard.csv               # Hard compound analysis
│       ├── medium.csv             # Medium compound analysis
│       ├── soft.csv               # Soft compound analysis
│       ├── long_runs_hard.csv     # Long run stints (hard)
│       ├── long_runs_medium.csv   # Long run stints (medium)
│       ├── long_runs_soft.csv     # Long run stints (soft)
│       ├── team_degradation.csv   # Team degradation metrics
│       ├── fuel_correction.py     # Fuel load adjustment script
│       └── race_simulator.py      # Race strategy simulator
│
├── cache/                          # FastF1 cache for faster data retrieval
│   ├── fastf1_http_cache.sqlite   # HTTP request cache
│   └── 2022/                      # Cached sessions by year
│
├── models/                         # Machine learning models (future)
├── notebooks/                      # Jupyter notebooks for analysis
└── .venv/                         # Python virtual environment
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
cd D:\Projects\F1-pit-lap-predictor
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Data Collection
```bash
python main.py
```
This script:
- Enables FastF1 caching for faster subsequent runs
- Loads F1 session data from the specified year and race
- Stores raw data in the `data/raw/` directory

### Data Cleaning & Analysis
```bash
python src/data_cleaning.py
python src/degradation_analysis.py
python src/long_run_detection.py
```

### Race Strategy Simulation
```bash
python data/clean/race_simulator.py
```
Simulates different pit stop strategies and outputs total race times for each strategy.

## Key Dependencies

- **fastf1**: Official F1 data library
- **pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning algorithms
- **matplotlib/seaborn**: Data visualization (future)
- **numpy**: Numerical computing

## Data Format

### Raw Data
- Session telemetry includes lap times, tire information, track position, and performance metrics
- Data is cached locally to minimize API requests

### Cleaned Data
- Standardized tire compound names (SOFT, MEDIUM, HARD)
- Calculated tire age and lap time in seconds
- Team and driver information normalized
- Outliers removed through consistency filtering

## Analysis Metrics

### Tire Degradation
- Linear degradation rate (seconds per lap)
- Polynomial and Random Forest degradation models
- R² scores for model accuracy
- Per-team and per-compound analysis

### Race Simulation
- Base pace estimation: ~97 seconds per lap (Bahrain example)
- Pit penalty: ~22 seconds (average pit stop + penalties)
- Strategy comparison: 2-stop vs 3-stop pit strategies

## Future Works

### 1. **Advanced ML Models**
   - Develop neural networks for tire degradation prediction
   - Implement LSTM models for time-series lap time forecasting
   - Create ensemble models combining multiple prediction methods
   - Support Vector Machine (SVM) optimization

### 2. **Real-Time Race Prediction**
   - Live pit stop window recommendations during races
   - Dynamic strategy adjustment based on race conditions
   - Weather impact modeling
   - Fuel consumption and weight distribution analysis

### 3. **Multi-Season Analysis**
   - Historical trend analysis across multiple seasons
   - Driver performance consistency metrics
   - Team strategy pattern recognition
   - Track-specific optimization

### 4. **Web Dashboard**
   - Flask/Django web application for visualization
   - Interactive race scenario simulator
   - Real-time data updates during F1 weekends
   - User-friendly strategy comparison tools
   - API endpoints for external integrations

### 5. **Enhanced Data Features**
   - Fuel load impact on lap times
   - Brake and tire temperature effects
   - DRS zone analysis and efficiency metrics
   - Accident and yellow flag impact modeling
   - Weather data integration (temperature, wind, rain)

### 6. **Performance Optimization**
   - Database integration (PostgreSQL/MongoDB) for large datasets
   - Parallel processing for multi-race analysis
   - Caching optimization
   - API rate limiting and error handling

### 7. **Predictive Features**
   - Qualifying vs Race performance correlation
   - Tire life prediction models
   - Driver consistency predictions
   - Setups impact on performance

### 8. **Validation & Testing**
   - Unit tests for all modules
   - Integration tests for data pipeline
   - Backtesting against historical race results
   - Cross-validation for model accuracy

### 9. **Documentation**
   - API documentation
   - Tutorial notebooks
   - Data schema documentation
   - Model explanation guides

### 10. **Model Deployment**
   - Containerization with Docker
   - Cloud deployment options (AWS/Azure/GCP)
   - CI/CD pipeline setup
   - Model versioning and management

## Contributing

Guidelines for contributing to this project:
1. Create a feature branch
2. Commit your changes
3. Push to the branch
4. Create a Pull Request

## License

This project is open source and available under MIT License.

## Data Sources

- **FastF1 Library**: https://github.com/theOehrly/Fast-F1
- **Formula 1 Official Data**: Accessed through FastF1 API

## Authors

- Project developed for F1 strategy analysis and optimization

## Acknowledgments

- FastF1 library maintainers
- Formula 1 data providers
- Data analysis and machine learning community

## Contact

For questions, issues, or suggestions, please open an issue in the project repository.

---

**Last Updated**: May 23, 2026
**Status**: Active Development

