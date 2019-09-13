# encoding:utf-8

import pandas as pd


if __name__ == "__main__":
    pd.read_json("jsonAllComments.json").to_excel("jsonAllComments.xlsx")
    pd.read_json("jsonHotComments.json").to_excel("jsonHotComments.xlsx")