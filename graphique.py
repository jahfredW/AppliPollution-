import numpy as np
import matplotlib.pyplot as plt
import pollution
import datetime






def draw_graph(ville, pol):

    data = []
    data2 = []

    a = len(pollution._get_pollution_ville(ville))
    print(a)

    if pol == 1:
        for x in range(0, 97, 24):
            data.append(pollution.get_pm10_j5(ville, x))
        data.append(pollution.get_pm10_j5(ville, a-1))
        title = "Previsions Pm10 sur 5 jours"

    if pol == 2:
        for x in range(0, 97, 24):
            data.append(pollution.get_pm25_j5(ville, x))
        data.append(pollution.get_pm25_j5(ville, 98))
        title = "Previsions Pm2.5 sur 5 jours"

    columns = ('J0', 'J+1', 'J+2', 'J+3', 'J+4', 'J+5')
    values = np.arange(0,12,1) #crée une liste de 0 à 12 de 1 en 1
    y_offset = np.zeros(len(columns)) #crée une liste de 5 0
    index = np.arange(0,len(columns)) #crée une liste de 0 au nombre de colonnes de 1 en 1

    today = datetime.date.today()
    j_1 = today + datetime.timedelta(days=1)
    j_2 = today + datetime.timedelta(days=2)
    j_3 = today + datetime.timedelta(days=3)
    j_4 = today + datetime.timedelta(days=4)
    j_5 = today + datetime.timedelta(days=5)

    days = ['lundi', 'mardi', 'mercredi', 'jeudi','vendredi','samedi','dimanche']

    bar_width = 0.4
    n_rows = len(data)

    colors = plt.cm.BuPu(np.linspace(0.3, 0.8, 6))
    cell_text = []
    for row in range(n_rows):
        plt.bar(index[row], data[row], bar_width, bottom=y_offset, color='darkorange')

    plt.xlabel("J+5")
    plt.ylabel("Concentrations (µg/m3)")
    plt.grid()
    plt.title(title)
    plt.xticks([0, 1, 2, 3, 4, 5], ["Ce jour", days[j_1.isoweekday() - 1]
        , days[j_2.isoweekday() - 1], days[j_3.isoweekday()-1] , days[j_4.isoweekday() - 1],
                                                                 days[j_5.isoweekday() - 1]])

    plt.show()
