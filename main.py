import pickle
import pandas as pd
from pandas.core.frame import DataFrame

with open('./model.pkl', 'rb') as file:
    model = pickle.load(file, errors='ignore')
dis_df = pd.read_csv('./data.csv', index_col='disease')


def predict(data: list):

    lst = pd.DataFrame(data).transpose()
    col = df.columns.tolist()
    lst.columns = col
    data = lst

    prediction = model.predict(data)[0]
    out = dis_df.loc[prediction]

    print('\n' + prediction.capitalize(), "-\n" + out['discription'])

    precautions = out['precautions'].split(",")

    print("\nPrecautions", "-")
    for i, preco in enumerate(precautions):
        print(i, ")", preco.lstrip())


if __name__ == "__main__":

    df = pd.read_csv('./symptoms-weight.csv')
    df.set_index('Disease', inplace=True)

    n = 458

    t1 = df.iloc[n]

    print('\nActual - ', dis_df.loc[t1.name].name)

    t1 = pd.DataFrame(t1)
    t1 = t1.transpose()

    lst = t1.iloc[0].to_list()

    predict(lst)
