import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

import os


current_dir = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_dir))
file_path = os.path.join(parent_dir, "Kolkata.csv")

df = pd.read_csv(file_path)

le = LabelEncoder()
df["Location"] = le.fit_transform(df["Location"])

X = df.drop("Price", axis=1)
y = df["Price"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


class PricePredictor:
   
    
    def predictPrice(self, data):
        inputs = {
            'Area': data['Area'],
            'Location': data['Location'],
            'No. of Bedrooms': data['No. of Bedrooms'],
            'Resale': data['Resale'],
            'MaintenanceStaff': data['MaintenanceStaff'],
            'Gymnasium': data['Gymnasium'],
            'SwimmingPool': data['SwimmingPool'],
            'LandscapedGardens': data['LandscapedGardens'],
            'JoggingTrack': data['JoggingTrack'],
            'RainWaterHarvesting': data['RainWaterHarvesting'],
            'IndoorGames': data['IndoorGames'],
            'ShoppingMall': data['ShoppingMall'],
            'Intercom': data['Intercom'],
            'SportsFacility': data['SportsFacility'],
            'ATM': data['ATM'],
            'ClubHouse': data['ClubHouse'],
            'School': data['School'],
            '24X7Security': data['24X7Security'],
            'PowerBackup': data['PowerBackup'],
            'CarParking': data['CarParking'],
            'StaffQuarter': data['StaffQuarter'],
            'Cafeteria': data['Cafeteria'],
            'MultipurposeRoom': data['MultipurposeRoom'],
            'Hospital': data['Hospital'],
            'WashingMachine': data['WashingMachine'],
            'Gasconnection': data['Gasconnection'],
            'AC': data['AC'],
            'Wifi': data['Wifi'],
            "Children'splayarea": data["Children'splayarea"],
            'LiftAvailable': data['LiftAvailable'],
            'BED': data['BED'],
            'VaastuCompliant': data['VaastuCompliant'],
            'Microwave': data['Microwave'],
            'GolfCourse': data['GolfCourse'],
            'TV': data['TV'],
            'DiningTable': data['DiningTable'],
            'Sofa': data['Sofa'],
            'Wardrobe': data['Wardrobe'],
            'Refrigerator': data['Refrigerator'],
        }
        inputs["Location"] = le.transform([inputs["Location"]])[0]
        X_input = pd.DataFrame([inputs])
        y_pred = model.predict(X_input)
        return format(round(y_pred[0]))