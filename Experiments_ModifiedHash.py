import xlrd
from time import time
from Modified_probe_hash_map import ChainHashMap
from random import randint



for i in range(6):
    if i == 0 or i == 1:
        file_location = 'UNDATA.xlsx'
    elif i == 1 or i == 2:
        file_location = 'UNSTATE.xlsx'
    else:
        file_location = 'FedSchoolCodeList.xlsx'

    work_book = xlrd.open_workbook(file_location)

    sheet = work_book.sheet_by_index(0)
    v = sheet.cell_value(1,1)

    key=[]
    val = []

    for i in range(50):
        key.append(int(sheet.cell_value(i+1, 0)))




    for i in range(50):
        val.append(sheet.cell_value(i+1, 1))


    vl =ChainHashMap()

    start =time()
    for i in range(len(key)):

        vl.__setitem__(key[i],val[i])

    end = time()
    t = (end - start)
    print()
    print("Modified Probe Hash Map using seperate chaining - Experiment on ", file_location)
    print()
    print("Time for set item for Modified Probe Hash Map {0:.8f} ".format(t))
    print()
    i = randint(0, len(key) - 1)
    start = time()

    vl.get(i)

    end = time()
    t = (end - start)
    print("Time for get item for Modified Probe Hash Map {0:.8f} ".format(t))