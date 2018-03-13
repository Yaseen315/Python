import pandas as pd
import numpy as np
import glob
import os

filenames = ["nc_nat_1933.csv", "nc_nat_1939.csv", "ny_nat_1933.csv", "ny_nat_1939.csv",
"oh_nat_1933.csv", "oh_nat_1939.csv", "tx_nat_1933.csv", "tx_nat_1933.csv", "wi_nat_1933.csv", "wi_nat_1939.csv"]

combined = pd.concat( [ pd.read_csv(f) for f in filenames ] )
combined.to_csv( "combined.csv", index=False )

combined = pd.read_csv( "combined.csv")

def creatCombinedCsv():
    filenames = ["nc_nat_1933.csv", "nc_nat_1939.csv", "ny_nat_1933.csv", "ny_nat_1939.csv",
    "oh_nat_1933.csv", "oh_nat_1939.csv", "tx_nat_1933.csv", "tx_nat_1933.csv", "wi_nat_1933.csv", "wi_nat_1939.csv"]

    combined = pd.concat( [ pd.read_csv(f) for f in filenames ] )
    combined.to_csv( "combined.csv", index=False )


def countRows():
    city = ["nc", "ny", "oh", "tx", "wi"]
    year = ["1933", "1939"]
    row_count = 0
    for c in city:
        for y in year:
            yes = (pd.read_csv(c + "_nat_" + y + ".csv"))
            row_count += (len(yes))
    print (row_count)

def loanAssetRatio1939():
    only1939 = (combined[combined['year'] == 1939])
    only1939["loanAssetRatio"] = (only1939['loans'] / only1939['assets'])
    print (only1939)
    only1939.to_csv( "only1939.csv", index=False )  
    

def loanAssetRatio1933():
    only1933 = (combined[combined['year'] == 1933])
    only1933["loanAssetRatio"] = (only1933['loans'] / only1933['assets'])
    only1933.to_csv( "only1933.csv", index=False )
    print (only1933.tail(10))

loanAssetRatio1933()



