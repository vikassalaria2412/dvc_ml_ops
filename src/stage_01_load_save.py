from typing import Mapping
from src.utils.all_utils import create_directory, read_yaml
import argparse
import os
import pandas as pd

def get_data(config_path):
    config = read_yaml(config_path)

    #print(config)
    remote_data_path = config["data_source"]
    df = pd.read_csv(remote_data_path, sep=";")

    #print(df.head())

    # save dataset in the local directory
    # crete path to directory: artifacts/raw_local_dir/data.csv

    artifacts_dir = config["artifacts"] ['artifacts_dir']
    raw_local_dir = config["artifacts"] ['raw_local_dir']
    raw_local_file = config["artifacts"] ['raw_local_file']

    raw_local_dir_path = os.path.join(artifacts_dir,raw_local_dir)

    create_directory(dirs = [raw_local_dir_path,raw_local_file])

    raw_local_file_path = os.path.join(raw_local_dir_path,raw_local_file)

    df.to_csv(raw_local_file_path, sep = ",",index =False)
    print(raw_local_file_path)


if __name__ == '__main__' :
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    #print(args)

    parsed_args = args.parse_args()
    print(parsed_args)

    get_data(parsed_args.config)

