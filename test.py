import os
import sys
import argparse
import subprocess
import datetime

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser


path  = os.environ['HOME']
user_path = os.path.join(path,'workspace')
clon_path = os.path.join(user_path,'test_paths')
pom = os.path.join(clon_path,'api/saahas-maven/pom.xml')
print pom
