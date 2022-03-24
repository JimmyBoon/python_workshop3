from os import path
# from turtle import position
import os

# file_name = "square_positions.txt"


def GetPositionsFromFile(file_name):
    positions_list = []
    data = []

    if path.exists(file_name):
        print("file exists")
        myfile = open(file_name, "r")
        data = myfile.readlines()

    myfile.close()

    for line in data:
        # remove white space:
        line = line.strip()

        # separate at the ,
        x_y_list = line.split(",")

        # convert to ints
        x = int(x_y_list[0])
        y = int(x_y_list[1])

        # if time show error checking

        positions_list.append([x, y])

    return positions_list


print(GetPositionsFromFile("level1/demo.txt"))
