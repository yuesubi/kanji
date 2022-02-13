import os
import csv
import json
import time
import random


class Kanji:
    def __init__(self, p_id, updated, memorised, known):
        self.id: str = p_id
        self.updated: int = updated
        self.memorised: int = memorised
        self.known: bool = known


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
        to_see = list()

        with open(cls.ACHIVEMENT_DATA, 'r', encoding='utf-8') as file:
            data = json.load(file)

        date = time.time()

        for k in data["kanjis"].keys():
            kanji = data["kanjis"][k]
            if (date - kanji["updated"]) / 225 > pow(2, kanji["memorised"]) and not kanji["known"]:
                to_see.append( Kanji(k, -1, kanji["memorised"], False) )

        # TODO: give data in frequency order

        return to_see

    @classmethod
    def get_kanji_comming_up(cls) -> list:
        data = dict()
        comming_up = list()

        with open(cls.ACHIVEMENT_DATA, 'r', encoding='utf-8') as file:
            data = json.load(file)

        date = time.time()

        for k in data["kanjis"].keys():
            kanji = data["kanjis"][k]
            if not kanji["known"]:
                time_to_wait = (pow(2, kanji["memorised"])) * 225 - (date - kanji["updated"])
                comming_up.append( Kanji(k, time_to_wait, kanji["memorised"], False) )

        # TODO: give data in frequency order
        
        return comming_up

    @classmethod
    def save_achivements(cls, achivements) -> None:
        data = dict()

        with open(cls.ACHIVEMENT_DATA, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for kanji in achivements:
            data["kanjis"][kanji.id] = {
                "updated": kanji.updated,
                "memorised": kanji.memorised,
                "known": kanji.known
            }

        with open(cls.ACHIVEMENT_DATA, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    @classmethod
    def get_kanji_by_id(cls, p_id) -> list:
        with open(cls.RAW_DATA, 'r', encoding='utf-8') as file:
            for line in csv.reader(file, delimiter=';'):
                if line[0] == p_id:
                    return line
        
        return list()

    @classmethod
    def get_new_kanji(cls, amount) -> list:
        existing_ids = list()

        with open(cls.ACHIVEMENT_DATA, 'r', encoding='utf-8') as file:
            existing_ids = json.load(file)["kanjis"].keys()

        new_kanji = []

        with open(cls.RAW_DATA, 'r', encoding='utf-8') as file:
            data = list(csv.reader(file, delimiter=';'))[1:]
            data.sort(key=lambda line: int(line[5]) + int(line[6]) , reverse=True)

            i = 0
            while len(new_kanji) < amount and i < 10e4:  # i < 10e5 condition is for if one day i go threw all 2K+ kanji
                if data[i][0] not in existing_ids:
                    new_kanji.append(
                        Kanji(data[i][0], 0, -1, False)
                    )
                i += 1
        
        return new_kanji

    @classmethod
    def save_time(cls) -> None:
        data = dict()
        with open(cls.ACHIVEMENT_DATA, 'r', encoding='utf-8') as file:
            data = json.load(file)

        data["params"]["last_time"] = f"{time.asctime().split(sep=' ')[1]} {time.asctime().split(sep=' ')[2]}" 
        with open(cls.ACHIVEMENT_DATA, 'w', encoding='utf-8') as file:
            json.dump(data, file)

    @classmethod
    def get_last_time(cls) -> str:
        with open(cls.ACHIVEMENT_DATA, 'r', encoding='utf-8') as file:
            return json.load(file)["params"]["last_time"]

    @classmethod
    def get_random_kanji(cls) -> str:
        with open(cls.RAW_DATA, 'r', encoding='utf-8') as file:
            data = list(csv.reader(file, delimiter=';'))[1:]
            return data[random.randint(0, len(data) - 1)][1]


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
