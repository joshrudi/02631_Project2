import csv
from pathlib import Path


def dataLoad(filename):

    if not Path(filename).is_file():

        print("Error: Invalid File Name/Path!")
        return []

    f = open(filename)
    csv_f = csv.reader(f)

    data = []

    for row in csv_f: data.append(row)

    f.close()
    return data
