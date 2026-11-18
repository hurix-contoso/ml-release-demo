import argparse
import pathlib
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("--out", required=True)
args = parser.parse_args()

out = pathlib.Path(args.out)
out.mkdir(parents=True, exist_ok=True)
shutil.copy("train.py", out / "train.py")
(out / "environment.yml").write_text(
    "$schema: https://azuremlschemas.azureedge.net/latest/environment.schema.json\n"
    "name: churn-serving-env\n"
    "image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest\n"
)
print("artifact built in", out)
