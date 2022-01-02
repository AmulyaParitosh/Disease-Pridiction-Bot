import pickle

with open("./classifire.pkl", "rb") as file:
    classifire = pickle.load(file, errors="ignore")

with open("./regressor.pkl", "rb") as file:
    regressor = pickle.load(file, errors="ignore")
