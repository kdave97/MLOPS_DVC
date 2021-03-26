import click
import os
import pandas as pd
import numpy as np
import joblib
import json
from get_data import read_params

from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def evaluate_metrics(test_Y,predictions):
    rmse=np.sqrt(mean_squared_error(test_Y,predictions))
    mae=mean_absolute_error(test_Y,predictions)
    r2=r2_score(test_Y,predictions)

    return (rmse,mae,r2)


def train_evaluate(config_file):
    config=read_params(config_file)
    train_path=config['split_data']['train_path']
    test_path=config['split_data']['test_path']
    target=config['base']['target_col']

    train=pd.read_csv(train_path)
    test=pd.read_csv(test_path)

    train_X,train_Y=train.loc[:, train.columns!=target], train[target]
    test_X,test_Y=test.loc[:, test.columns!=target], test[target]


    random_state=config['base']['random_state']
    alpha=config['estimators']['ElasticNet']['params']['alpha'] 
    l1_ratio=config['estimators']['ElasticNet']['params']['l1_ratio']    

    model=ElasticNet(alpha=alpha,l1_ratio=l1_ratio,random_state=random_state)
    model.fit(train_X,train_Y)
    predictions=model.predict(test_X)

    model_dir=config['model_dir']
    joblib.dump(model,os.path.join(model_dir,'model.joblib'))

    (rmse, mae, r2)= evaluate_metrics(test_Y,predictions)

    print ("RMSE: ",rmse)
    print ("MAE: ",mae)
    print ("R2: ",r2)

    scores_file=config['report']['scores']
    with open(scores_file,"w") as f:
        scores={
            "RMSE": rmse,
            "MAE": mae,
            "R2_Score": r2
        }
        json.dump(scores, f, indent=4)









    
    





@click.command()
@click.option('--config_file', required=True, default='params.yaml', help="Enter the path for configuration file")

def main(config_file):
    train_evaluate(config_file)


if __name__=='__main__':
    main()