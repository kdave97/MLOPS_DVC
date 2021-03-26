import click
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params


def train_test(config_file):
    config=read_params(config_file)
    raw_path=config['load_data']['raw_source']
    df=pd.read_csv(raw_path,sep=",")

    train_path=config['split_data']['train_path']
    test_path=config['split_data']['test_path']
    random_state=config['base']['random_state']
    test_size=config['split_data']['test_size']

    train,test=train_test_split(df,test_size=test_size,random_state=random_state)

    train.to_csv(train_path,sep=",",index=False)
    test.to_csv(test_path,sep=",",index=False)


@click.command()
@click.option('--config_file', required=True, default='params.yaml', help="Enter the path for configuration file")

def main(config_file):
    train_test(config_file)


if __name__=='__main__':
    main()