# 🏢 Advanced Building Energy Consumption Predictor

Predict annual energy consumption with occupancy variation, climate zone data, and performance gap reduction analysis.

## 🚀 Quick Start

### Option 1: Using Python Script (Easiest)
```bash
cd /Users/supunvidarshana/Desktop/project25
python3 run_app.py
```

### Option 2: Using Shell Script
```bash
cd /Users/supunvidarshana/Desktop/project25
./run_streamlit.sh
```

### Option 3: Manual Terminal Command
```bash
cd /Users/supunvidarshana/Desktop/project25
.venv/bin/python -m streamlit run .venv/streamlit_app_enhanced.py
```

## 📋 Features

- **📊 Predict Energy**: Predict building energy consumption based on multiple parameters
- **📈 Occupancy Analysis**: Analyze peak and off-peak occupancy patterns
- **🌍 Climate Data**: Upload and manage climate zone data
- **🔧 HVAC System Details**: Configure HVAC systems via CSV upload or manual input
- **📉 Gap Reduction**: Analyze and reduce performance gaps between predicted and actual energy
- **📁 Upload Data**: Upload building data, climate data, and HVAC system specifications

## 📦 Project Files

- `data_generation_enhanced.py` - Generate synthetic building energy dataset
- `ml_pipeline_with_gap_reduction.py` - ML model training with gap reduction
- `.venv/streamlit_app_enhanced.py` - Main streamlit web application
- `building_energy_enhanced.csv` - Sample building energy data
- `climate_zone_data.csv` - Climate zone information
- `hvac_system_types.csv` - HVAC system specifications
- `energy_model_with_gap_reduction.joblib` - Trained ML model

## 🔧 Installation

### Initial Setup (One time only)

1. **Create virtual environment:**
```bash
cd /Users/supunvidarshana/Desktop/project25
python3 -m venv .venv
```

2. **Activate virtual environment:**
```bash
source .venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install --upgrade pip
pip install pandas numpy scikit-learn xgboost lightgbm joblib streamlit plotly faker
```

4. **On macOS, install OpenMP (required for XGBoost):**
```bash
brew install libomp
```

### After Setup

Just use one of the Quick Start commands above!

## 🌐 Access the App

Once running, the app will be available at:
- **Local**: `http://localhost:8501`
- **Network**: `http://192.168.x.x:8501`

## 📝 Usage Guide

### Step 1: Climate Zone
Select a built-in climate zone or upload your own climate data CSV

### Step 2: Building Information
Enter basic building details (area, floors, age, building type, etc.)

### Step 3: HVAC System Details
- **Option A**: Upload HVAC system data from CSV file
- **Option B**: Manually configure HVAC specifications

### Step 4: Occupancy Variation
Configure peak and off-peak occupancy patterns and power densities

### Step 5: Systems & Environment
Set outdoor temperature, humidity, and other environmental parameters

### Prediction & Analysis
Click "Predict Energy Consumption" to get results with:
- Annual energy consumption prediction
- Detailed breakdown by system
- Performance gap analysis
- Recommendations for optimization

## 📊 Data Format

### HVAC System CSV Format
```csv
building_id,hvac_system_type,hvac_efficiency,energy_recovery,compressor_type,refrigerant_type,system_age_years,seasonal_cop_summer,seasonal_cop_winter,maintenance_status
B00001,Split,0.85,Yes,Rotary,R410A,9,4.2,3.8,Good
B00002,VRF,0.92,Yes,Scroll,R32,6,4.8,4.1,Excellent
```

### Climate Data CSV Format
```csv
location,climate_zone,avg_annual_temp,avg_humidity,heating_degree_days,cooling_degree_days
Miami,1,28.5,75,200,3500
Phoenix,2,32.1,35,1200,2800
```

## 🔬 Model Performance

- **R² Score**: 0.5724
- **MAE**: 22,885 kWh
- **RMSE**: 45,541 kWh
- **MAPE**: 21.48%

## 🐛 Troubleshooting

### "No module named 'pandas'"
```bash
.venv/bin/pip install pandas
```

### "XGBoost not found" (macOS)
```bash
brew install libomp
.venv/bin/pip install --upgrade xgboost
```

### App not starting
1. Verify `.venv` exists
2. Run: `.venv/bin/pip install streamlit`
3. Try the Python script: `python3 run_app.py`

### Port already in use
The app will automatically use the next available port (8502, 8503, etc.)

## 📚 Technology Stack

- **Python 3.13**
- **Streamlit** - Web application framework
- **Scikit-learn** - Machine learning
- **XGBoost** - Gradient boosting
- **LightGBM** - Fast gradient boosting
- **Pandas** - Data analysis
- **Plotly** - Interactive visualizations
- **Joblib** - Model serialization

## 📝 Notes

Always validate predictions with actual measurements for critical decisions.

---

For questions or issues, please check the troubleshooting section above.
