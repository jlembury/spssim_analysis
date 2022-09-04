# Jessica Embury, San Diego State University, Fall 2022
# General functions that support the SpSSIM analysis

def Diff(li1, li2):
    """
    Find differences between 2 list objects
    :param li1: list object 1
    :param li2: list object 2
    :return: list object with items that are not in both li1 and li2
    """
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif
