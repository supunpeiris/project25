import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

def generate_enhanced_building_dataset(n_samples=5000):
    """
    Generate enhanced synthetic building energy dataset with new features
    """
    np.random.seed(42)
    random.seed(42)
    fake = Faker()
    
    data = {}
    
    # === BASIC BUILDING CHARACTERISTICS ===
    data['total_floor_area'] = np.random.uniform(500, 50000, n_samples)  # m²
    data['number_of_floors'] = np.random.randint(1, 50, n_samples)
    data['building_age'] = np.random.randint(1, 100, n_samples)
    
    # === NEW: OCCUPANCY VARIATION ===
    data['occupancy_peak'] = np.random.uniform(0.7, 1.3, n_samples)  # Peak occupancy multiplier
    data['occupancy_off_peak'] = np.random.uniform(0.2, 0.5, n_samples)  # Off-peak occupancy multiplier
    data['peak_hours_per_day'] = np.random.randint(4, 10, n_samples)  # Hours of peak occupancy
    data['base_occupant_count'] = np.random.randint(10, 2000, n_samples)
    
    # Calculate actual occupant counts
    data['peak_occupant_count'] = (data['base_occupant_count'] * data['occupancy_peak']).astype(int)
    data['off_peak_occupant_count'] = (data['base_occupant_count'] * data['occupancy_off_peak']).astype(int)
    
    # === NEW: CLIMATE ZONE WITH REALISTIC DATA ===
    climate_zones = np.random.choice([1, 2, 3, 4, 5, 6, 7], n_samples, p=[0.1, 0.15, 0.2, 0.25, 0.15, 0.1, 0.05])
    climate_descriptions = ['Hot-Humid', 'Hot-Dry', 'Warm-Humid', 'Mixed-Dry', 'Cool-Humid', 'Cold', 'Very-Cold']
    data['climate_zone'] = climate_zones
    data['climate_description'] = [climate_descriptions[z-1] for z in climate_zones]
    
    # Generate temperatures based on climate zone with seasonal variation
    base_temps = []
    for zone in climate_zones:
        if zone == 1:  # Hot-Humid
            base_temps.append(np.random.uniform(25, 35))
        elif zone == 2:  # Hot-Dry
            base_temps.append(np.random.uniform(28, 40))
        elif zone == 3:  # Warm-Humid
            base_temps.append(np.random.uniform(20, 30))
        elif zone == 4:  # Mixed-Dry
            base_temps.append(np.random.uniform(15, 28))
        elif zone == 5:  # Cool-Humid
            base_temps.append(np.random.uniform(10, 22))
        elif zone == 6:  # Cold
            base_temps.append(np.random.uniform(-5, 15))
        else:  # Very-Cold
            base_temps.append(np.random.uniform(-10, 10))
    
    data['outdoor_temperature'] = np.array(base_temps)
    data['humidity'] = np.random.uniform(20, 90, n_samples)
    
    # === NEW: HVAC SYSTEM TYPE ===
    hvac_types = ['Split', 'VRF', 'Chiller', 'Packaged', 'Heat Pump']
    data['hvac_system_type'] = np.random.choice(hvac_types, n_samples, p=[0.4, 0.2, 0.2, 0.1, 0.1])
    
    # === NEW: ENERGY RECOVERY SYSTEM ===
    data['has_energy_recovery'] = np.random.choice([0, 1], n_samples, p=[0.6, 0.4])
    
    # === SYSTEM EFFICIENCIES WITH OCCUPANCY VARIATION ===
    data['hvac_efficiency_base'] = np.random.uniform(0.6, 0.95, n_samples)
    # Efficiency varies with occupancy
    data['hvac_efficiency_peak'] = data['hvac_efficiency_base'] * np.random.uniform(0.9, 1.0, n_samples)
    data['hvac_efficiency_off_peak'] = data['hvac_efficiency_base'] * np.random.uniform(1.0, 1.1, n_samples)
    
    # Lighting and equipment with occupancy variation
    data['lighting_power_density_base'] = np.random.uniform(5, 20, n_samples)  # W/m²
    data['equipment_power_density_base'] = np.random.uniform(3, 15, n_samples)  # W/m²
    
    # Peak hours have higher power density
    data['lighting_power_density_peak'] = data['lighting_power_density_base'] * np.random.uniform(1.2, 1.5, n_samples)
    data['equipment_power_density_peak'] = data['equipment_power_density_base'] * np.random.uniform(1.3, 1.8, n_samples)
    
    # Off-peak hours have lower power density
    data['lighting_power_density_off_peak'] = data['lighting_power_density_base'] * np.random.uniform(0.3, 0.7, n_samples)
    data['equipment_power_density_off_peak'] = data['equipment_power_density_base'] * np.random.uniform(0.2, 0.5, n_samples)
    
    # === OPERATIONAL FACTORS ===
    data['total_operating_hours'] = np.random.uniform(8, 24, n_samples)
    data['weekday_numeric'] = np.random.randint(0, 7, n_samples)
    data['has_elevator_numeric'] = np.random.choice([0, 1], n_samples, p=[0.3, 0.7])
    data['floor_height'] = np.random.uniform(3, 5, n_samples)
    
    # === BUILDING TYPE ===
    building_types = np.random.choice(['Office', 'Residential', 'Commercial', 'Educational', 'Healthcare'], 
                                     n_samples, p=[0.4, 0.2, 0.2, 0.1, 0.1])
    data['building_type'] = building_types
    
    # === CALCULATE WEIGHTED AVERAGES FOR DAILY OPERATIONS ===
    data['avg_daily_occupants'] = (
        data['peak_occupant_count'] * data['peak_hours_per_day'] + 
        data['off_peak_occupant_count'] * (data['total_operating_hours'] - data['peak_hours_per_day'])
    ) / data['total_operating_hours']
    
    data['avg_lighting_power'] = (
        data['lighting_power_density_peak'] * data['peak_hours_per_day'] + 
        data['lighting_power_density_off_peak'] * (data['total_operating_hours'] - data['peak_hours_per_day'])
    ) / data['total_operating_hours']
    
    data['avg_equipment_power'] = (
        data['equipment_power_density_peak'] * data['peak_hours_per_day'] + 
        data['equipment_power_density_off_peak'] * (data['total_operating_hours'] - data['peak_hours_per_day'])
    ) / data['total_operating_hours']
    
    data['avg_hvac_efficiency'] = (
        data['hvac_efficiency_peak'] * data['peak_hours_per_day'] + 
        data['hvac_efficiency_off_peak'] * (data['total_operating_hours'] - data['peak_hours_per_day'])
    ) / data['total_operating_hours']
    
    # === ENGINEERED FEATURES ===
    data['occupant_density_peak'] = data['peak_occupant_count'] / data['total_floor_area']
    data['occupant_density_off_peak'] = data['off_peak_occupant_count'] / data['total_floor_area']
    
    # HVAC system type efficiency factors
    hvac_efficiency_factors = {'Split': 0.9, 'VRF': 1.1, 'Chiller': 1.0, 'Packaged': 0.85, 'Heat Pump': 1.05}
    data['hvac_type_factor'] = [hvac_efficiency_factors[t] for t in data['hvac_system_type']]
    
    # Energy recovery savings
    data['energy_recovery_savings'] = data['has_energy_recovery'] * np.random.uniform(0.1, 0.25, n_samples)
    
    # Peak load intensity
    data['peak_load_intensity'] = (
        data['occupancy_peak'] * 
        data['lighting_power_density_peak'] / data['lighting_power_density_base'] * 
        data['equipment_power_density_peak'] / data['equipment_power_density_base']
    )
    
    # === CREATE DATAFRAME ===
    df = pd.DataFrame(data)
    
    # === CALCULATE ENERGY CONSUMPTION WITH NEW FEATURES ===
    # Base energy calculation
    base_energy = (
        df['total_floor_area'] * 0.8 +           # Area impact
        df['avg_daily_occupants'] * 120 +        # Weighted occupant impact
        df['avg_hvac_efficiency'] * -5000 +      # Weighted efficiency impact
        df['avg_lighting_power'] * 200 +         # Weighted lighting impact
        df['avg_equipment_power'] * 180 +        # Weighted equipment impact
        df['outdoor_temperature'] * 50 +         # Temperature impact
        df['building_age'] * 10 +                # Age penalty
        df['peak_load_intensity'] * 1000 +       # Peak load impact
        df['hvac_type_factor'] * -2000 +         # HVAC type impact
        df['has_energy_recovery'] * -1500        # Energy recovery savings
    )
    
    # Add noise and outliers
    noise = np.random.normal(0, 0.15, n_samples) * base_energy
    outliers = np.random.choice([0, 1], n_samples, p=[0.95, 0.05])
    outlier_factor = np.where(outliers == 1, np.random.uniform(1.5, 3.0, n_samples), 1.0)
    
    df['energy_consumption_kwh'] = np.maximum((base_energy + noise) * outlier_factor, 1000)
    
    # Add ID and location
    df['building_id'] = [f'B{str(i).zfill(5)}' for i in range(n_samples)]
    df['building_name'] = [f'{fake.company()} Building' for _ in range(n_samples)]
    df['location'] = [fake.city() for _ in range(n_samples)]
    
    # Convert categorical to numeric for ML
    df['building_type_numeric'] = pd.Categorical(df['building_type']).codes
    df['hvac_system_type_numeric'] = pd.Categorical(df['hvac_system_type']).codes
    
    return df

def generate_climate_data_csv(filename='climate_zone_data.csv'):
    """Generate realistic climate zone data for upload"""
    np.random.seed(42)
    
    climate_zones = [1, 2, 3, 4, 5, 6, 7]
    descriptions = ['Hot-Humid', 'Hot-Dry', 'Warm-Humid', 'Mixed-Dry', 'Cool-Humid', 'Cold', 'Very-Cold']
    avg_temps = [30, 32, 25, 22, 16, 5, -2]
    avg_humidity = [75, 40, 65, 45, 70, 60, 55]
    heating_dd = [100, 500, 1500, 3000, 4500, 6000, 7500]
    cooling_dd = [4000, 3500, 2500, 1500, 800, 300, 100]
    
    data = []
    for zone, desc, temp, humid, hdd, cdd in zip(climate_zones, descriptions, avg_temps, 
                                                avg_humidity, heating_dd, cooling_dd):
        for _ in range(100):  # Multiple locations per zone
            location = f"City_{zone}_{_}"
            data.append({
                'location': location,
                'climate_zone': zone,
                'climate_description': desc,
                'avg_annual_temp': temp + np.random.normal(0, 3),
                'avg_summer_temp': temp + 5 + np.random.normal(0, 2),
                'avg_winter_temp': temp - 5 + np.random.normal(0, 2),
                'avg_humidity': humid + np.random.normal(0, 10),
                'heating_degree_days': hdd + np.random.normal(0, 200),
                'cooling_degree_days': cdd + np.random.normal(0, 200),
                'solar_radiation_kwh_m2': np.random.uniform(1200, 2200),
                'rainfall_mm': np.random.uniform(200, 2000)
            })
    
    df_climate = pd.DataFrame(data)
    df_climate.to_csv(filename, index=False)
    print(f"Climate data saved to {filename}")
    return df_climate

if __name__ == "__main__":
    # Generate enhanced dataset
    print("Generating enhanced building energy dataset...")
    df = generate_enhanced_building_dataset(n_samples=5000)
    
    # Save datasets
    df.to_csv('building_energy_enhanced.csv', index=False)
    print(f"Enhanced dataset saved: {len(df)} samples")
    
    # Generate climate data
    climate_df = generate_climate_data_csv('climate_zone_data.csv')
    
    # Display statistics
    print("\n=== Key Statistics ===")
    print(f"Occupancy Peak Multiplier: {df['occupancy_peak'].mean():.2f} ± {df['occupancy_peak'].std():.2f}")
    print(f"Occupancy Off-Peak Multiplier: {df['occupancy_off_peak'].mean():.2f} ± {df['occupancy_off_peak'].std():.2f}")
    print(f"HVAC System Types: {df['hvac_system_type'].value_counts().to_dict()}")
    print(f"Energy Recovery Systems: {df['has_energy_recovery'].sum()} / {len(df)}")
    print(f"Average Daily Occupants: {df['avg_daily_occupants'].mean():.0f}")
    print(f"Energy Consumption: {df['energy_consumption_kwh'].mean():,.0f} kWh")