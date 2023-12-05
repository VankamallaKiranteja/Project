import random
import pandas as pd

# Initialize an empty DataFrame
locations = [ 'Visakhapatnam', 'Vijayawada', 'Guntur', 'Nellore', 'Kurnool', 'Kakinada',
    'Tirupati', 'Kadapa', 'Rajahmundry', 'Ongole', 'Anantapur', 'Eluru']
data = {
   
    'Location': [],
    'Temperature (°C)': [],
    'Dissolved Oxygen (ppm)': [],
    # 'CO2 Concentration (ppm)': [],
    # 'Salinity (ppt)': [],
    # 'Alkalinity (µmol/kg)': [],
    # 'Dissolved Inorganic Carbon (µmol/kg)': [],
    # 'Biological Activity (mg/m³)': [],
    # 'Ocean Circulation (m/s)': [],
    # 'Atmospheric CO2 Concentration (ppm)': [],
    'pH': []
}

# Generate 500 rows of synthetic data
for _ in range(500):
    
    location = random.choice(locations)
    temperature = round(random.uniform(25, 35), 1)
    # co2_concentration = random.randint(380, 420)
    # salinity = round(random.uniform(32, 38), 1)
    # alkalinity = random.randint(1800, 2400)
    # dissolved_inorganic_carbon = random.randint(1800, 2400)
    # biological_activity = round(random.uniform(0, 1), 2)
    # ocean_circulation = round(random.uniform(0, 0.5), 2)
    # atmospheric_co2_concentration = random.randint(400, 420)
    dissolved_oxgen = random.randint(0, 25)
    ph = round(random.uniform(6.0, 10.0), 2)
    
   
    data['Location'].append(location)
    data['Temperature (°C)'].append(temperature)
    data['Dissolved Oxygen (ppm)'].append(dissolved_oxgen)
    # data['CO2 Concentration (ppm)'].append(co2_concentration)
    # data['Salinity (ppt)'].append(salinity)
    # data['Alkalinity (µmol/kg)'].append(alkalinity)
    # data['Dissolved Inorganic Carbon (µmol/kg)'].append(dissolved_inorganic_carbon)
    # data['Biological Activity (mg/m³)'].append(biological_activity)
    # data['Ocean Circulation (m/s)'].append(ocean_circulation)
    # data['Atmospheric CO2 Concentration (ppm)'].append(atmospheric_co2_concentration)
    data['pH'].append(ph)

# Create a DataFrame
df = pd.DataFrame(data)
# Save to a CSV file
df.to_csv('seawater_ph_dataset.csv', index=False)