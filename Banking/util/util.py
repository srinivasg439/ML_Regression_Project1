import yaml
from Banking.exception import BankingException
import os,sys


def read_yaml_file(file_path:str) ->dict:
    """
    read YAML file and returns the contents as dictionary.
    file_path:str
    """
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise BankingException(e,sys) from e