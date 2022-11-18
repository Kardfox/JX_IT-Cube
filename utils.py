import matplotlib.pyplot as plt
import pandas as pd
import io


def simplest_render(csv_file):
    csv_file = io.BytesIO(csv_file)
    dataframe = pd.read_csv(csv_file)

    x = dataframe["DATE"]
    y = dataframe["Auckland"]

    plt.scatter(x,y)
    figure = plt.gcf()

    buffer = io.BytesIO()
    figure.savefig(buffer, format='png')
    buffer.seek(0)

    return buffer