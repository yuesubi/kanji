import os, csv


data = []

with open("database.csv", 'r', encoding='utf-8') as f:
    data = list(csv.reader(f, delimiter=';'))
    data.pop(0)  # Delete descriptors

data.sort(key=lambda e: int(e[5]) + int(e[6]), reverse=True)

for elem in range(5):
    print(data[elem])


class Data:
    CURR_DIR = os.path.dirname(__file__)

    ACHIVEMENT_DATA = os.path.join(CURR_DIR, "data", "achive.json")
    RAW_DATA = os.path.join(CURR_DIR, "data", "database.csv")

    @classmethod
    def get_kanji(cls):
        pass
