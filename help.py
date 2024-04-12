import mlflow
mlflow.set_tracking_uri("http:/localhost:5000")


exp_id = mlflow.create_experiment('Loan_Prediction')

with mlflow.start_run(run_name='DecisionTreeClass') as run:
    pass

mlflow.end_run()
n_estimators=10
criterion='gini'

mlflow.log_params('n_estimators':n_estimators)