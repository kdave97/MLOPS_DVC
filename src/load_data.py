import pandas as pd
import click
from get_data import read_params,get_data

def load_save(config_file):
    config=read_params(config_file)
    df=get_data(config_file)
    new_columns = [col.replace(" ","_") for col in df.columns]
    raw_path = config['load_data']['raw_source']
    df.to_csv(raw_path,sep=",",index=False, header=new_columns)
    

@click.command()
@click.option('--config_file', required=True, default='params.yaml', help="Enter the path for configuration file")

def main(config_file):
    print (load_save(config_file))

if __name__=='__main__':
    main()

