import bz2
import pandas as pd
import pickle
import os
import glob


def raw(path_to_raw_data: str) -> tuple:
    activity_test = path_to_raw_data + "act_test.csv"
    activity_train = path_to_raw_data + "act_train.csv"
    people = path_to_raw_data + "people.csv"
    return activity_test, activity_train, people


def read_raw_data(data: str) -> pd.DataFrame:
    return pd.read_csv(data)


def remove_csv_files():
    FILE_PATH: str = "../data/raw/"
    os.chdir(FILE_PATH)
    csv_files = glob.glob("*.csv")

    for file in csv_files:
        if file == "sample_submission.csv":
            continue
        os.remove(file)


if __name__ == "__main__":
    print("Starting compression!!!")
    PATH = "../data/raw/"
    for FILE_PATH in raw(PATH):
        data = read_raw_data(FILE_PATH)
        temp1 = FILE_PATH.split("/")[:-1]
        temp2 = FILE_PATH.split("/")[-1]
        name = temp2.split(".")[0]
        out = "/".join(temp1)
        f = bz2.BZ2File(out + f"/{name}.pbz2", "w")
        pickle.dump(data, f)
        print(f"Compressed {name} :)")
    print("Compression successful")

remove_csv_files()
