# pip install pyyaml
import yaml
import os

with open('data.yml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    print(data)