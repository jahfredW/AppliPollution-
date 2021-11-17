import numpy as np
import matplotlib.pyplot as plt
import pollution


def graph_pm10(ville):

    """data = []
    a = pollution.get_pm10_j5(ville, 0)
    b = pollution.get_pm10_j5(ville, 24)
    c = pollution.get_pm10_j5(ville, 48)
    d = pollution.get_pm10_j5(ville, 72)
    e = pollution.get_pm10_j5(ville, 96)

    data = [a, b, c, d, e]
    """
    data = []
    data.append(pollution.get_pm10_j5(ville,0))
    data.append(pollution.get_pm10_j5(ville,24))
    data.append(pollution.get_pm10_j5(ville,48))
    data.append(pollution.get_pm10_j5(ville,72))
    data.append(pollution.get_pm10_j5(ville,96))


    columns = ('un', 'deux', 'trois', 'quatre', 'cinq')
    values = np.arange(0,12,1) #crée une liste de 0 à 12 de 1 en 1
    y_offset = np.zeros(len(columns)) #crée une liste de 5 0
    index = np.arange(1,len(columns) + 1) #crée une liste de 0 au nombre de colonnes de 1 en 1


    print(values, y_offset, index, data)

    n_rows = len(data)

    cell_text = []
    for row in range(n_rows):
        plt.bar(index[row], data[row])
        y_offset = y_offset + data[row]


    plt.xlabel("Jours")
    plt.ylabel("Concentrations")
    plt.grid()
    plt.title("Previsions Pm10")

    plt.show()

