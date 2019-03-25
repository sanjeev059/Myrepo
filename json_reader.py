#!/usr/bin/python


import json
import os

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

config = ConfigParser()
config.read("fusion.ini")
path = config.get('path','union_path')
base_path ="/Users/sanjeev.d/workspace"
corrected_path = os.path.join(base_path,path)
#print corrected_path

def read_json_data(old_data):
    with open (corrected_path ,'r') as json_file:
        data_old = json.load(json_file)
        return old_data


def write_modify_data():



def main():
    old_data = []
    read_json_data(old_data)


if __name__ == '__main__':
        main()
