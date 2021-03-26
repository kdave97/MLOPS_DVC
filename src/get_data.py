import os
import yaml
import pandas as pd
import click

def read_params(config_path):
    with open(config_path) as file:
        config=yaml.safe_load(file)
    return config


def get_data(config_path):
    config=read_params(config_path)
    data_path=config["data_source"]['s3_source']
    df=pd.read_csv(data_path, sep=",")
    return df



@click.command()
@click.option('--config_file', required=True, default='params.yaml', help="Enter the path for configuration file")

def main(config_file):
    get_data(config_file)


if __name__=='__main__':
    main()



