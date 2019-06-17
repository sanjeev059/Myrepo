import requests
import json

import os
import sys
import argparse
import subprocess
import datetime
import re

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

path  = os.environ['HOME']
user_path = os.path.join(path,'workspace')
clon_path = os.path.join(user_path,'test_paths')

api_path= os.path.join(clon_path,'api/saahas-maven/pom.xml')
core_path= os.path.join(clon_path,'core/pom.xml')
http_path= os.path.join(clon_path,'http/pom.xml')
edi_path= os.path.join(clon_path,'edi/pom.xml')
bdi_path= os.path.join(clon_path,'bdi/pom.xml')
notify_path= os.path.join(clon_path,'notify/pom.xml')
scheduler_path= os.path.join(clon_path,'scheduler/pom.xml')

set_path = [api_path,
            core_path,
            http_path,
            edi_path,
            bdi_path,
            notify_path,
            scheduler_path]


def checkout_release(release_branch):
    branch = release_branch

    api_commit = os.path.join(clon_path,'api')
    core_commit = os.path.join(clon_path,'core')
    http_commit = os.path.join(clon_path,'http')
    edi_commit = os.path.join(clon_path,'edi')
    bdi_commit = os.path.join(clon_path,'bdi')
    notify_commit = os.path.join(clon_path,'notify')
    scheduler_commit = os.path.join(clon_path,'scheduler')

    commit_arr = [api_commit,core_commit,http_commit,edi_commit,bdi_commit,notify_commit,scheduler_commit]
    for path in commit_arr:
        #str(path)
        os.chdir(path)
        os.system('git checkout develop && git remote update')
        subprocess.check_output("git checkout "+branch, shell=True)

def store_turvo_config_version():
    common_conf = os.path.join (clon_path,'common-config/pom.xml')
    #print common_conf
    m = subprocess.check_output("grep -w '<version>2.0.*</version>' /Users/sanjeev.d/workspace/test_paths/common-config/pom.xml", shell=True)
    str = m[13:19]
    return str

#def copy_version():

def v1_merge_changes(vers,path):
    var = vers
    var1 = var+"-SNAPSHOT"
    f = open(path,'r')
    filedata = f.read()
    f.close()
    newdata = filedata.replace(var,var1)
    f = open(path,'w')
    f.write(newdata)
    f.close()
    commit_version()


def commit_version():
    api_commit = os.path.join(clon_path,"api")
    core_commit = os.path.join(clon_path,"core")
    http_commit = os.path.join(clon_path,"http")
    edi_commit = os.path.join(clon_path,"edi")
    bdi_commit = os.path.join(clon_path,"bdi")
    notify_commit = os.path.join(clon_path,"notify")
    scheduler_commit = os.path.join(clon_path,"scheduler")

    commit_arr = [api_commit,core_commit,http_commit,edi_commit,bdi_commit,notify_commit,scheduler_commit]

    for commit in commit_arr:
        #str(commit)
        os.chdir(commit)
        subprocess.check_output("git status",shell=True)
        subprocess.check_output("git add  .",shell=True)
        subprocess.check_output('git commit -m merge_from_release_to_develop',shell=True)
        subprocess.check_output("git push origin",shell=True)
        os.chdir(clon_path)
print "completd with pom xml merge"
'''

    api_path = os.path.join(clon_path,"api/saahas-maven")
    os.chdir(api_path)
    print api_path
    subprocess.check_output("sed s/%var/2.0.37-SNAPSHOT/ pom.xml > pom1.xml mv pom1.xml pom.xml", shell=True)

    #subprocess.check_output("sed 's/$var/$var1/' api/saahas-maven/pom.xml > api/saahas-maven/pom1.xml",shell=True)
    #subprocess.check_output('mv api/saahas-maven/pom1.xml api/saahas-maven/pom.xml',shell=True)

#mv api/saahas-maven/pom1.xml api/saahas-maven/pom.xml
'''

#def raise_pull_request():
def main():
    #ver = store_turvo_config_version()
    checkout_release("pull_test")
    print "completed in checking out release branch"
#    get_path = set_common_paths()
    for ref_path in set_path:
        v1_merge_changes("2.0.38",ref_path)
#commit_version()

if __name__ == "__main__":
    main()
