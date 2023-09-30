import os
import yaml
from CNNClassifier import logger
import json
import joblib
from pathlib import Path
from typing import Any
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from box import ConfigBox

@ensure_annotations
def read_yaml(path_to_yaml:Path)-> ConfigBox:
    with open(path_to_yaml) as yaml_file:
        content=yaml.safe_load(yaml_file)
        return ConfigBox(content)

@ensure_annotations
def save_json():
    pass

@ensure_annotations
def load_json():
    pass

@ensure_annotations
def save_model():
    pass

@ensure_annotations
def load_model():
    pass

@ensure_annotations
def get_size():
    pass

@ensure_annotations
def create_directory(path_to_directory:list,verbose=True):
    for path in path_to_directory:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"create directory at : {path}")