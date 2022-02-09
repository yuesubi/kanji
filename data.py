import os, csv, json


class Data:
    CURR_DIR = os.path.dirname(__file__)

    ACHIVEMENT_DATA = os.path.join(CURR_DIR, "data", "achive.json")
    RAW_DATA = os.path.join(CURR_DIR, "data", "database.csv")

    @classmethod
    def get_kanji(cls) -> list:
        data = list()

        with open(cls.RAW_DATA, 'r', encoding='utf-8') as file:
            # Get all the lines of data exept for the first
            data = list(csv.reader(file, delimiter=';'))[1:]

        # Sort the kanji by frequency
        data.sort(key=lambda line: int(line[5]) + int(line[6]) , reverse=True)

        return data

    @classmethod
    def get_kanji_to_see(cls) -> list:
        data = dict()

        with open(cls.ACHIVEMENT_DATA, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for kanji in data["kanjis"]:
            pass


# Format of the "achivement data"
# this data is the information on the kanji that are
# currently being leard
#
# JSON {
#     "params": {
#         "confirm_amount": 2,
#         "amount": 0
#     },
# 
# // All the kanji learned
#     "kanjis": {
#         "19": {
#             "updated": "2021-01-19",  // The date when the kanji was last seen
#             "memorised": 0,  // The "level" of *memorisation* of the kanji
#             "known": false  // If the kanji is already perfectly known
#         }
#     }
# }
