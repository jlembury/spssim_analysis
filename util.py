# Jessica Embury, San Diego State University, Fall 2022
# General functions that support the SpSSIM analysis

import pandas as pd
import os

def Diff(li1, li2):
    """
    Find differences between 2 list objects
    :param li1: list object 1
    :param li2: list object 2
    :return: list object with items that are not in both li1 and li2
    """
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif


def combine_csv_files(csv_dir, combo_csv_out=False, combo_csv=None):
    files = os. listdir(csv_dir)
    df = pd.read_csv(csv_dir + files[0])
    for f in files[1:]:
        tmp = pd.read_csv(csv_dir + f)
        df = pd.concat([df, tmp], ignore_index=True)

    if combo_csv_out:
        df.to_csv(combo_csv, index=False)

    return df
