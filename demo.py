import os
import mlflow 
import argparse
import time

def eval(inp1,inp2):
    output_metric = inp1**2 + inp2**2
    return output_metric

def main(inp1,inp2):
    mlflow.set_experiment("Demo-Experiment")
    with mlflow.start_run(run_name='Example Demo'):
        mlflow.log_param("param1",inp1)
        mlflow.log_param("param2",inp2)
        metric = eval(inp1=inp1, inp2=inp2)
        mlflow.log_metric("Eval Metric", metric)
        os.makedirs("dummy", exist_ok=True)

        with open("dummy/example.txt", "wt") as f:
            f.write(f"Artifact Created By {time.asctime()}")

        mlflow.log_artifacts("dummy")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p1", "--param1", type=int, default=5)
    parser.add_argument("-p2", "--param2", type=int, default=5)
    parsed_args = parser.parse_args()

    main(parsed_args.param1, parsed_args.param2)
