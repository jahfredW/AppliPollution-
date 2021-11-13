import requests

url = 'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={API key}'
lat = 51.049999
lon = 2.36667
api_key = "de344c900509e22467e79e19be02d6bb"

def get_pollution_forecast(api_key,lat,lon):
    url = f'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={lon}&appid={api_key}'
    global response
    response = requests.get(url).json()

def get_date_j5():
    date = []
    tranche_24h = 0
    # Boucler sur les previsions à 5 jours
    for jours in range(0, 5):
        # --- On ajoute à la liste date les previsions à n +
        date.append(response['list'][tranche_24h]['dt'])
        # On incrémente la tranche de 24h
        tranche_24h = tranche_24h + 24
    print(date)
        # On retourne une liste contenant les dates + 24
    return date

def get_indice_j5():
    indice = []
    tranche_24h = 0

    for jours in range(0, 5):
        # --- On ajoute à la liste date les previsions à n +
        indice.append(response['list'][tranche_24h]['main'])
        # On incrémente la tranche de 24h
        tranche_24h = tranche_24h + 24
    print(indice)
        # On retourne une liste contenant les dates + 24
    return indice

def get_pm25_j5():
    pm25= []
    tranche_24h = 0

    for jours in range(0, 5):
        # --- On ajoute à la liste date les previsions à n +
        pm25.append(response['list'][tranche_24h]['components']['pm2_5'])
        # On incrémente la tranche de 24h
        tranche_24h = tranche_24h + 24
    print(pm25)
        # On retourne une liste contenant les dates + 24
    return pm25

def get_pm10_j5():
    pm10= []
    tranche_24h = 0

    for jours in range(0, 5):
        # --- On ajoute à la liste date les previsions à n +
        pm10.append(response['list'][tranche_24h]['components']['pm10'])
        # On incrémente la tranche de 24h
        tranche_24h = tranche_24h + 24
    print(pm10)
        # On retourne une liste contenant les dates + 24
    return pm10

def get_nh3():
    nh3= []
    tranche_24h = 0

    for jours in range(0, 5):
        # --- On ajoute à la liste date les previsions à n +
        nh3.append(response['list'][tranche_24h]['components']['nh3'])
        # On incrémente la tranche de 24h
        tranche_24h = tranche_24h + 24
    print(nh3)
        # On retourne une liste contenant les dates + 24
    return nh3


get_pollution_forecast(api_key,lat,lon)
get_indice_j5()
get_date_j5()
get_pm25_j5()
get_pm10_j5()
get_nh3()



"""
city_name = "Dunkerque,FR"
api_key = "de344c900509e22467e79e19be02d6bb"
lat = 50.8333
lon = 2.5

def get_pollution(api_key, lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat=%7Blat%7D&lon=%7Blon%7D&appid=%7Bapi_key%7D"

    pollution = {}

    response = requests.get(url).json()
    co = response['list'][0]['components']['co']
    pollution['co'] = co

    response = requests.get(url).json()
    o3 = response['list'][0]['components']['o3']
    pollution['o3'] = o3

    response = requests.get(url).json()
    so2 = response['list'][0]['components']['so2']
    pollution['so2'] = so2

    response = requests.get(url).json()
    pm2_5 = response['list'][0]['components']['pm2_5']
    pollution['pm2_5'] = pm2_5

    response = requests.get(url).json()
    pm10 = response['list'][0]['components']['pm10']
    pollution['pm10'] = pm10

    return pollution


pollution = get_pollution(api_key, lat, lon)

print(pollution)
"""


"""
{'coord': {'lon': 2.3667, 'lat': 51.05},
 'list': [{'main': {'aqi': 2}, 'components': {'co': 230.31, 'no': 0, 'no2': 3.47, 'o3': 92.98, 'so2': 2.06, 'pm2_5': 5.03, 'pm10': 10.58, 'nh3': 0}, 'dt': 1636743600},
        {'main': {'aqi': 2}, 'components': {'co': 236.99, 'no': 0, 'no2': 2.91, 'o3': 92.98, 'so2': 1.82, 'pm2_5': 5.01, 'pm10': 12.36, 'nh3': 0.01}, 'dt': 1636747200},
        {'main': {'aqi': 2}, 'components': {'co': 240.33, 'no': 0, 'no2': 2.74, 'o3': 82.25, 'so2': 1.61, 'pm2_5': 5.08, 'pm10': 13.98, 'nh3': 0.02}, 'dt': 1636750800},
        {'main': {'aqi': 1}, 'components': {'co': 240.33, 'no': 0, 'no2': 2.66, 'o3': 76.53, 'so2': 1.48, 'pm2_5': 4.99, 'pm10': 15.47, 'nh3': 0.04}, 'dt': 1636754400},
        {'main': {'aqi': 1}, 'components': {'co': 236.99, 'no': 0, 'no2': 2.64, 'o3': 74.39, 'so2': 1.46, 'pm2_5': 5.23, 'pm10': 17.63, 'nh3': 0.07}, 'dt': 1636758000},
        {'main': {'aqi': 1}, 'components': {'co': 240.33, 'no': 0, 'no2': 2.79, 'o3': 72.24, 'so2': 1.54, 'pm2_5': 5.43, 'pm10': 18.23, 'nh3': 0.12}, 'dt': 1636761600},
        {'main': {'aqi': 1}, 'components': {'co': 240.33, 'no': 0, 'no2': 3.04, 'o3': 70.1, 'so2': 1.62, 'pm2_5': 5.41, 'pm10': 17.6, 'nh3': 0.2}, 'dt': 1636765200},
        {'main': {'aqi': 1}, 'components': {'co': 240.33, 'no': 0, 'no2': 3.26, 'o3': 67.23, 'so2': 1.58, 'pm2_5': 5.47, 'pm10': 16.33, 'nh3': 0.24}, 'dt': 1636768800},
        {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0, 'no2': 3.34, 'o3': 62.94, 'so2': 1.39, 'pm2_5': 5.19, 'pm10': 13.76, 'nh3': 0.26}, 'dt': 1636772400},
        {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0, 'no2': 3.43, 'o3': 59.37, 'so2': 1.39, 'pm2_5': 4.81, 'pm10': 10.78, 'nh3': 0.24}, 'dt': 1636776000},
        {'main': {'aqi': 1}, 'components': {'co': 247, 'no': 0, 'no2': 4.58, 'o3': 55.79, 'so2': 2.03, 'pm2_5': 4.56, 'pm10': 8.24, 'nh3': 0.21}, 'dt': 1636779600},
          {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0, 'no2': 5.23, 'o3': 52.93, 'so2': 2.5, 'pm2_5': 4.01, 'pm10': 6.5, 'nh3': 0.23}, 'dt': 1636783200},
          {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0, 'no2': 4.67, 'o3': 53.64, 'so2': 2.5, 'pm2_5': 3.34, 'pm10': 5.58, 'nh3': 0.27}, 'dt': 1636786800},
          {'main': {'aqi': 1}, 'components': {'co': 240.33, 'no': 0, 'no2': 3.3, 'o3': 57.94, 'so2': 1.88, 'pm2_5': 2.71, 'pm10': 4.88, 'nh3': 0.31}, 'dt': 1636790400},
          {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0.06, 'no2': 2.57, 'o3': 60.8, 'so2': 1.28, 'pm2_5': 2.22, 'pm10': 4.05, 'nh3': 0.31}, 'dt': 1636794000},
          {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0.15, 'no2': 2.64, 'o3': 59.37, 'so2': 1.12, 'pm2_5': 1.89, 'pm10': 3.48, 'nh3': 0.3}, 'dt': 1636797600},
          {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0.17, 'no2': 2.87, 'o3': 58.65, 'so2': 1.06, 'pm2_5': 1.63, 'pm10': 3.26, 'nh3': 0.31}, 'dt': 1636801200},
          {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0.1, 'no2': 3.17, 'o3': 57.94, 'so2': 1.04, 'pm2_5': 1.46, 'pm10': 3.12, 'nh3': 0.33}, 'dt': 1636804800},
          {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0.08, 'no2': 3.6, 'o3': 55.79, 'so2': 1.15, 'pm2_5': 1.44, 'pm10': 2.83, 'nh3': 0.31}, 'dt': 1636808400},
          {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0.06, 'no2': 4.37, 'o3': 52.93, 'so2': 1.3, 'pm2_5': 1.56, 'pm10': 2.78, 'nh3': 0.28}, 'dt': 1636812000},
          {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0.02, 'no2': 5.14, 'o3': 49.35, 'so2': 1.43, 'pm2_5': 1.69, 'pm10': 2.81, 'nh3': 0.26}, 'dt': 1636815600},
          {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0, 'no2': 5.83, 'o3': 46.49, 'so2': 1.57, 'pm2_5': 1.86, 'pm10': 2.91, 'nh3': 0.24}, 'dt': 1636819200},
          {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0, 'no2': 6.26, 'o3': 44.35, 'so2': 1.68, 'pm2_5': 2.01, 'pm10': 3.04, 'nh3': 0.22}, 'dt': 1636822800},
          {'main': {'aqi': 1}, 'components': {'co': 240.33, 'no': 0, 'no2': 5.66, 'o3': 44.35, 'so2': 1.65, 'pm2_5': 2.01, 'pm10': 3.05, 'nh3': 0.18}, 'dt': 1636826400},
          {'main': {'aqi': 1}, 'components': {'co': 240.33, 'no': 0, 'no2': 4.37, 'o3': 47.21, 'so2': 1.43, 'pm2_5': 2.08, 'pm10': 3.27, 'nh3': 0.13}, 'dt': 1636830000},
          {'main': {'aqi': 1}, 'components': {'co': 240.33, 'no': 0, 'no2': 3.38, 'o3': 50.78, 'so2': 1.25, 'pm2_5': 2.45, 'pm10': 3.86, 'nh3': 0.06}, 'dt': 1636833600},
          {'main': {'aqi': 1}, 'components': {'co': 243.66, 'no': 0, 'no2': 3, 'o3': 53.64, 'so2': 1.24, 'pm2_5': 2.84, 'pm10': 4.5, 'nh3': 0.02}, 'dt': 1636837200},
          {'main': {'aqi': 1}, 'components': {'co': 247, 'no': 0, 'no2': 2.87, 'o3': 53.64, 'so2': 1.31, 'pm2_5': 3.17, 'pm10': 5.06, 'nh3': 0}, 'dt': 1636840800},
          {'main': {'aqi': 1}, 'components': {'co': 250.34, 'no': 0, 'no2': 2.91, 'o3': 52.21, 'so2': 1.4, 'pm2_5': 3.68, 'pm10': 5.83, 'nh3': 0}, 'dt': 1636844400},
          {'main': {'aqi': 1}, 'components': {'co': 250.34, 'no': 0, 'no2': 2.91, 'o3': 52.21, 'so2': 1.43, 'pm2_5': 4.11, 'pm10': 6.6, 'nh3': 0}, 'dt': 1636848000},
          {'main': {'aqi': 1}, 'components': {'co': 250.34, 'no': 0, 'no2': 2.83, 'o3': 51.5, 'so2': 1.42, 'pm2_5': 4.31, 'pm10': 6.88, 'nh3': 0}, 'dt': 1636851600},
          {'main': {'aqi': 1}, 'components': {'co': 250.34, 'no': 0, 'no2': 2.87, 'o3': 50.78, 'so2': 1.4, 'pm2_5': 4.61, 'pm10': 7.17, 'nh3': 0}, 'dt': 1636855200},
          {'main': {'aqi': 1}, 'components': {'co': 257.02, 'no': 0, 'no2': 3, 'o3': 47.92, 'so2': 1.43, 'pm2_5': 5.3, 'pm10': 7.6, 'nh3': 0}, 'dt': 1636858800},
          {'main': {'aqi': 1}, 'components': {'co': 270.37, 'no': 0, 'no2': 3.77, 'o3': 42.2, 'so2': 1.54, 'pm2_5': 6.64, 'pm10': 8.94, 'nh3': 0}, 'dt': 1636862400},
          {'main': {'aqi': 1}, 'components': {'co': 287.06, 'no': 0, 'no2': 4.54, 'o3': 40.05, 'so2': 1.59, 'pm2_5': 6.89, 'pm10': 9.32, 'nh3': 0}, 'dt': 1636866000},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0, 'no2': 3.3, 'o3': 49.35, 'so2': 1.52, 'pm2_5': 4.55, 'pm10': 6.63, 'nh3': 0}, 'dt': 1636869600},
          {'main': {'aqi': 1}, 'components': {'co': 253.68, 'no': 0, 'no2': 2.27, 'o3': 57.94, 'so2': 1.55, 'pm2_5': 3.79, 'pm10': 5.18, 'nh3': 0}, 'dt': 1636873200},
          {'main': {'aqi': 1}, 'components': {'co': 247, 'no': 0, 'no2': 2.38, 'o3': 57.94, 'so2': 1.83, 'pm2_5': 3.96, 'pm10': 4.96, 'nh3': 0}, 'dt': 1636876800},
          {'main': {'aqi': 1}, 'components': {'co': 253.68, 'no': 0.13, 'no2': 4.41, 'o3': 50.78, 'so2': 1.83, 'pm2_5': 4.17, 'pm10': 5.66, 'nh3': 0.01}, 'dt': 1636880400},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0.56, 'no2': 6.86, 'o3': 45.06, 'so2': 1.76, 'pm2_5': 4.06, 'pm10': 5.43, 'nh3': 0.17}, 'dt': 1636884000},
          {'main': {'aqi': 1}, 'components': {'co': 297.07, 'no': 1.2, 'no2': 7.63, 'o3': 37.91, 'so2': 1.76, 'pm2_5': 6.59, 'pm10': 7.61, 'nh3': 0.37}, 'dt': 1636887600},
          {'main': {'aqi': 2}, 'components': {'co': 300.41, 'no': 1.36, 'no2': 7.37, 'o3': 40.77, 'so2': 1.68, 'pm2_5': 10.53, 'pm10': 11.64, 'nh3': 0.39}, 'dt': 1636891200},
          {'main': {'aqi': 1}, 'components': {'co': 287.06, 'no': 0.69, 'no2': 6.17, 'o3': 55.08, 'so2': 1.37, 'pm2_5': 9.91, 'pm10': 11.48, 'nh3': 0.5}, 'dt': 1636894800},
          {'main': {'aqi': 1}, 'components': {'co': 283.72, 'no': 0.23, 'no2': 5.27, 'o3': 61.51, 'so2': 1.28, 'pm2_5': 8.8, 'pm10': 10.89, 'nh3': 0.54}, 'dt': 1636898400},
          {'main': {'aqi': 1}, 'components': {'co': 287.06, 'no': 0.05, 'no2': 5.83, 'o3': 55.79, 'so2': 1.34, 'pm2_5': 9.11, 'pm10': 11.18, 'nh3': 0.52}, 'dt': 1636902000},
          {'main': {'aqi': 2}, 'components': {'co': 300.41, 'no': 0, 'no2': 7.88, 'o3': 44.35, 'so2': 1.52, 'pm2_5': 11.21, 'pm10': 12.98, 'nh3': 0.52}, 'dt': 1636905600},
          {'main': {'aqi': 2}, 'components': {'co': 310.42, 'no': 0, 'no2': 11.14, 'o3': 33.62, 'so2': 1.88, 'pm2_5': 13.67, 'pm10': 14.83, 'nh3': 0.49}, 'dt': 1636909200},
          {'main': {'aqi': 2}, 'components': {'co': 323.77, 'no': 0, 'no2': 14.91, 'o3': 23.6, 'so2': 2.24, 'pm2_5': 14.54, 'pm10': 15.25, 'nh3': 0.44}, 'dt': 1636912800},
          {'main': {'aqi': 2}, 'components': {'co': 327.11, 'no': 0, 'no2': 17.65, 'o3': 17.35, 'so2': 2.15, 'pm2_5': 14.18, 'pm10': 14.69, 'nh3': 0.47}, 'dt': 1636916400},
          {'main': {'aqi': 2}, 'components': {'co': 320.44, 'no': 0, 'no2': 15.94, 'o3': 20.56, 'so2': 1.68, 'pm2_5': 12.44, 'pm10': 12.9, 'nh3': 0.57}, 'dt': 1636920000},
          {'main': {'aqi': 2}, 'components': {'co': 310.42, 'no': 0, 'no2': 13.54, 'o3': 27.18, 'so2': 1.54, 'pm2_5': 11.86, 'pm10': 12.34, 'nh3': 0.56}, 'dt': 1636923600},
          {'main': {'aqi': 2}, 'components': {'co': 307.08, 'no': 0, 'no2': 11.48, 'o3': 32.54, 'so2': 1.61, 'pm2_5': 11.18, 'pm10': 11.67, 'nh3': 0.54}, 'dt': 1636927200},
          {'main': {'aqi': 2}, 'components': {'co': 303.75, 'no': 0, 'no2': 10.28, 'o3': 34.69, 'so2': 1.8, 'pm2_5': 10.07, 'pm10': 10.58, 'nh3': 0.53}, 'dt': 1636930800},
          {'main': {'aqi': 1}, 'components': {'co': 303.75, 'no': 0, 'no2': 9.85, 'o3': 34.69, 'so2': 2.12, 'pm2_5': 9.09, 'pm10': 9.62, 'nh3': 0.5}, 'dt': 1636934400},
          {'main': {'aqi': 1}, 'components': {'co': 303.75, 'no': 0, 'no2': 9.43, 'o3': 34.33, 'so2': 2.35, 'pm2_5': 8.61, 'pm10': 9.16, 'nh3': 0.44}, 'dt': 1636938000},
          {'main': {'aqi': 1}, 'components': {'co': 300.41, 'no': 0, 'no2': 8.65, 'o3': 34.69, 'so2': 2.35, 'pm2_5': 8.77, 'pm10': 9.37, 'nh3': 0.4}, 'dt': 1636941600},
          {'main': {'aqi': 1}, 'components': {'co': 300.41, 'no': 0, 'no2': 7.8, 'o3': 35.76, 'so2': 2.21, 'pm2_5': 9.15, 'pm10': 9.78, 'nh3': 0.36}, 'dt': 1636945200},
          {'main': {'aqi': 1}, 'components': {'co': 297.07, 'no': 0, 'no2': 6.94, 'o3': 37.91, 'so2': 2, 'pm2_5': 9.3, 'pm10': 9.96, 'nh3': 0.35}, 'dt': 1636948800},
          {'main': {'aqi': 1}, 'components': {'co': 293.73, 'no': 0, 'no2': 6.08, 'o3': 40.41, 'so2': 1.67, 'pm2_5': 9.4, 'pm10': 10.05, 'nh3': 0.34}, 'dt': 1636952400},
          {'main': {'aqi': 1}, 'components': {'co': 290.39, 'no': 0, 'no2': 5.44, 'o3': 43.63, 'so2': 1.42, 'pm2_5': 9.07, 'pm10': 9.7, 'nh3': 0.36}, 'dt': 1636956000},
          {'main': {'aqi': 1}, 'components': {'co': 287.06, 'no': 0, 'no2': 5.44, 'o3': 46.49, 'so2': 1.51, 'pm2_5': 8.6, 'pm10': 9.23, 'nh3': 0.35}, 'dt': 1636959600},
          {'main': {'aqi': 1}, 'components': {'co': 283.72, 'no': 0, 'no2': 5.91, 'o3': 49.35, 'so2': 1.79, 'pm2_5': 7.94, 'pm10': 8.57, 'nh3': 0.31}, 'dt': 1636963200},
          {'main': {'aqi': 1}, 'components': {'co': 280.38, 'no': 0.03, 'no2': 6.77, 'o3': 50.78, 'so2': 1.97, 'pm2_5': 7.22, 'pm10': 7.84, 'nh3': 0.26}, 'dt': 1636966800},
          {'main': {'aqi': 1}, 'components': {'co': 280.38, 'no': 0.1, 'no2': 7.03, 'o3': 53.64, 'so2': 1.91, 'pm2_5': 6.21, 'pm10': 6.8, 'nh3': 0.31}, 'dt': 1636970400},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0.16, 'no2': 6.68, 'o3': 57.22, 'so2': 1.71, 'pm2_5': 5.35, 'pm10': 5.93, 'nh3': 0.35}, 'dt': 1636974000},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0.19, 'no2': 6.77, 'o3': 59.37, 'so2': 1.59, 'pm2_5': 5.42, 'pm10': 6.04, 'nh3': 0.39}, 'dt': 1636977600},
          {'main': {'aqi': 1}, 'components': {'co': 277.04, 'no': 0.16, 'no2': 7.03, 'o3': 62.23, 'so2': 1.49, 'pm2_5': 6.11, 'pm10': 6.79, 'nh3': 0.42}, 'dt': 1636981200},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0.1, 'no2': 7.2, 'o3': 64.37, 'so2': 1.39, 'pm2_5': 6.41, 'pm10': 7.16, 'nh3': 0.43}, 'dt': 1636984800},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0.04, 'no2': 7.71, 'o3': 65.8, 'so2': 1.37, 'pm2_5': 6.22, 'pm10': 6.98, 'nh3': 0.44}, 'dt': 1636988400},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0.01, 'no2': 7.97, 'o3': 65.8, 'so2': 1.39, 'pm2_5': 5.93, 'pm10': 6.69, 'nh3': 0.42}, 'dt': 1636992000},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0, 'no2': 7.37, 'o3': 66.52, 'so2': 1.37, 'pm2_5': 5.67, 'pm10': 6.43, 'nh3': 0.4}, 'dt': 1636995600},
          {'main': {'aqi': 1}, 'components': {'co': 270.37, 'no': 0, 'no2': 6.51, 'o3': 67.95, 'so2': 1.37, 'pm2_5': 5.35, 'pm10': 6.1, 'nh3': 0.35}, 'dt': 1636999200},
          {'main': {'aqi': 1}, 'components': {'co': 270.37, 'no': 0, 'no2': 5.91, 'o3': 69.38, 'so2': 1.43, 'pm2_5': 4.9, 'pm10': 5.59, 'nh3': 0.3}, 'dt': 1637002800},
          {'main': {'aqi': 1}, 'components': {'co': 270.37, 'no': 0, 'no2': 6, 'o3': 67.95, 'so2': 1.55, 'pm2_5': 4.39, 'pm10': 5.02, 'nh3': 0.28}, 'dt': 1637006400},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0, 'no2': 6.51, 'o3': 64.37, 'so2': 1.65, 'pm2_5': 4.19, 'pm10': 4.79, 'nh3': 0.27}, 'dt': 1637010000},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0, 'no2': 7.97, 'o3': 57.94, 'so2': 1.8, 'pm2_5': 4.14, 'pm10': 4.69, 'nh3': 0.26}, 'dt': 1637013600},
          {'main': {'aqi': 1}, 'components': {'co': 277.04, 'no': 0, 'no2': 10.45, 'o3': 51.5, 'so2': 2.06, 'pm2_5': 4.48, 'pm10': 4.95, 'nh3': 0.2}, 'dt': 1637017200},
          {'main': {'aqi': 1}, 'components': {'co': 280.38, 'no': 0, 'no2': 13.54, 'o3': 47.21, 'so2': 2.3, 'pm2_5': 4.59, 'pm10': 4.98, 'nh3': 0.19}, 'dt': 1637020800},
          {'main': {'aqi': 1}, 'components': {'co': 280.38, 'no': 0, 'no2': 14.74, 'o3': 47.21, 'so2': 2.24, 'pm2_5': 4.81, 'pm10': 5.17, 'nh3': 0.2}, 'dt': 1637024400},
          {'main': {'aqi': 1}, 'components': {'co': 277.04, 'no': 0, 'no2': 13.71, 'o3': 49.35, 'so2': 2, 'pm2_5': 5.42, 'pm10': 5.78, 'nh3': 0.17}, 'dt': 1637028000},
          {'main': {'aqi': 1}, 'components': {'co': 277.04, 'no': 0, 'no2': 12.34, 'o3': 50.78, 'so2': 2, 'pm2_5': 6.1, 'pm10': 6.52, 'nh3': 0.17}, 'dt': 1637031600},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0, 'no2': 11.65, 'o3': 50.78, 'so2': 2.21, 'pm2_5': 6.75, 'pm10': 7.22, 'nh3': 0.18}, 'dt': 1637035200},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0, 'no2': 10.97, 'o3': 50.78, 'so2': 2.3, 'pm2_5': 6.52, 'pm10': 6.98, 'nh3': 0.19}, 'dt': 1637038800},
          {'main': {'aqi': 1}, 'components': {'co': 277.04, 'no': 0, 'no2': 9.94, 'o3': 50.78, 'so2': 2.06, 'pm2_5': 5.65, 'pm10': 6.05, 'nh3': 0.18}, 'dt': 1637042400},
          {'main': {'aqi': 1}, 'components': {'co': 277.04, 'no': 0, 'no2': 8.74, 'o3': 51.5, 'so2': 1.74, 'pm2_5': 4.86, 'pm10': 5.22, 'nh3': 0.19}, 'dt': 1637046000},
          {'main': {'aqi': 1}, 'components': {'co': 280.38, 'no': 0, 'no2': 7.71, 'o3': 51.5, 'so2': 1.58, 'pm2_5': 4.64, 'pm10': 4.99, 'nh3': 0.2}, 'dt': 1637049600},
          {'main': {'aqi': 1}, 'components': {'co': 280.38, 'no': 0.02, 'no2': 7.45, 'o3': 52.93, 'so2': 1.54, 'pm2_5': 4.71, 'pm10': 5.06, 'nh3': 0.22}, 'dt': 1637053200},
          {'main': {'aqi': 1}, 'components': {'co': 277.04, 'no': 0.1, 'no2': 7.45, 'o3': 56.51, 'so2': 1.52, 'pm2_5': 4.79, 'pm10': 5.16, 'nh3': 0.26}, 'dt': 1637056800},
          {'main': {'aqi': 1}, 'components': {'co': 277.04, 'no': 0.16, 'no2': 7.37, 'o3': 60.8, 'so2': 1.51, 'pm2_5': 4.76, 'pm10': 5.16, 'nh3': 0.31}, 'dt': 1637060400},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0.19, 'no2': 7.37, 'o3': 64.37, 'so2': 1.54, 'pm2_5': 4.56, 'pm10': 4.98, 'nh3': 0.35}, 'dt': 1637064000},
          {'main': {'aqi': 1}, 'components': {'co': 273.71, 'no': 0.18, 'no2': 7.71, 'o3': 65.09, 'so2': 1.64, 'pm2_5': 4.37, 'pm10': 4.84, 'nh3': 0.39}, 'dt': 1637067600},
          {'main': {'aqi': 1}, 'components': {'co': 277.04, 'no': 0.12, 'no2': 8.31, 'o3': 63.66, 'so2': 1.82, 'pm2_5': 4.26, 'pm10': 4.8, 'nh3': 0.42}, 'dt': 1637071200},
          {'main': {'aqi': 1}, 'components': {'co': 280.38, 'no': 0.06, 'no2': 9.17, 'o3': 59.37, 'so2': 2.03, 'pm2_5': 4.19, 'pm10': 4.74, 'nh3': 0.44}, 'dt': 1637074800},
          {'main': {'aqi': 1}, 'components': {'co': 283.72, 'no': 0.01, 'no2': 9.43, 'o3': 55.08, 'so2': 2.12, 'pm2_5': 4.11, 'pm10': 4.63, 'nh3': 0.42}, 'dt': 1637078400},
          {'main': {'aqi': 1}, 'components': {'co': 287.06, 'no': 0, 'no2': 9.17, 'o3': 50.78, 'so2': 2, 'pm2_5': 3.92, 'pm10': 4.39, 'nh3': 0.39}, 'dt': 1637082000},
          {'main': {'aqi': 1}, 'components': {'co': 290.39, 'no': 0, 'no2': 8.82, 'o3': 47.21, 'so2': 1.88, 'pm2_5': 3.8, 'pm10': 4.26, 'nh3': 0.36}, 'dt': 1637085600},
          {'main': {'aqi': 1}, 'components': {'co': 297.07, 'no': 0, 'no2': 8.82, 'o3': 44.35, 'so2': 2.03, 'pm2_5': 3.85, 'pm10': 4.31, 'nh3': 0.33}, 'dt': 1637089200},
          {'main': {'aqi': 1}, 'components': {'co': 307.08, 'no': 0, 'no2': 9.6, 'o3': 41.84, 'so2': 3.58, 'pm2_5': 4.36, 'pm10': 4.86, 'nh3': 0.31}, 'dt': 1637092800},
          {'main': {'aqi': 1}, 'components': {'co': 320.44, 'no': 0, 'no2': 11.31, 'o3': 40.05, 'so2': 6.38, 'pm2_5': 5.53, 'pm10': 6.11, 'nh3': 0.33}, 'dt': 1637096400},
          {'main': {'aqi': 1}, 'components': {'co': 337.12, 'no': 0, 'no2': 14.22, 'o3': 37.55, 'so2': 9.18, 'pm2_5': 7.79, 'pm10': 8.59, 'nh3': 0.38}, 'dt': 1637100000},
          {'main': {'aqi': 2}, 'components': {'co': 343.8, 'no': 0, 'no2': 16.11, 'o3': 35.05, 'so2': 9.54, 'pm2_5': 10.32, 'pm10': 11.42, 'nh3': 0.37}, 'dt': 1637103600},
          {'main': {'aqi': 2}, 'components': {'co': 327.11, 'no': 0, 'no2': 14.4, 'o3': 36.84, 'so2': 7.45, 'pm2_5': 11.75, 'pm10': 13.09, 'nh3': 0.32}, 'dt': 1637107200}]}
"""







"""
La ville de Paris a les coordonnées lon=2.3486 et lat=48.853401>
"""