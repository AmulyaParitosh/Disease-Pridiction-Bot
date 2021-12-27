from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd

df = pd.read_csv("symptoms-weight.csv", index_col='Disease')
symptoms = df.columns.tolist()
dff = pd.read_csv("Symptom-severity.csv", index_col="Symptom")

stop_words = set(stopwords.words("english"))
ignore = {'.', ',', ';', ':', '?', '/', '!', '$'}
stop_words.update(ignore)


def weightadder(sen):

    filtered_list = word_tokenize(sen)

    lst = []

    for i in symptoms:
        s_symp = i.split("_")
        present = True

        for s in s_symp:
            if s not in filtered_list:
                present = False
                break

        if present:
            weight = dff.loc[i, "weight"]
            lst.append(weight)
        else:
            lst.append(0)

    return lst


print(weightadder("i am a headache adn bloody stool"))
