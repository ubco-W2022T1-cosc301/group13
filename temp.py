import pandas as pd
import glob
import os
import pathlib

file_path_dir = "data/raw/housing-supply-and-rental/"
file_path = os.listdir(file_path_dir)
file_path

main_df = pd.DataFrame()

for file in file_path:
    if(os.path.splitext(file)[1] == ".csv"):
        temp = pd.read_csv(str(file_path_dir) + str(file))
        main_df = main_df.append(temp, ignore_index=True)
main_df.to_csv("data/processed/")