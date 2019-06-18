import requests
import json

import os
import sys
import argparse
import subprocess
import datetime
import re
import urllib2

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser


config = ConfigParser()
headers = {'content-type': 'application/json'}

auth_req = ('sanjeev.d','kindJ3lly81')
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
    api_path = os.path.join(clon_path,"api/saahas-maven")
    os.chdir(api_path)
    print api_path
    subprocess.check_output("sed s/%var/2.0.37-SNAPSHOT/ pom.xml > pom1.xml mv pom1.xml pom.xml", shell=True)

    #subprocess.check_output("sed 's/$var/$var1/' api/saahas-maven/pom.xml > api/saahas-maven/pom1.xml",shell=True)
    #subprocess.check_output('mv api/saahas-maven/pom1.xml api/saahas-maven/pom.xml',shell=True)

#mv api/saahas-maven/pom1.xml api/saahas-maven/pom.xml

def raise_pull_req_common():

    headers = {'content-type': 'application/json'}
    config = ConfigParser()
    config.read("rest_urls.ini")
    rest_url = config.get('common','common-config')
    print rest_url
    with open('pull_request.json','rw') as json_file:
        data1 = json.load(json_file)
        #r = requests.post(url=rest_url, data=json.dumps(data1), headers=headers,auth=pyload)
        response = requests.request("POST", rest_url, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

def raise_pull_req_platform():

    config.read("rest_urls.ini")
    rest_api = config.get('platform','api')
    print rest_api

    with open('pull_request_platform.json','r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_api, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text


    old_slug = "api"
    project_slug = "notify"
    json_modifier(old_slug,project_slug)

    config.read("rest_urls.ini")
    rest_notify = config.get('platform','notify')

    with open('pull_request_platform.json','r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_notify, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "notify"
    project_slug = "scheduler"
    json_modifier(old_slug,project_slug)

    config.read("rest_urls.ini")
    rest_notify = config.get('platform','scheduler')

    with open('pull_request_platform.json','r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_notify, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "scheduler"
    project_slug = "presence"
    json_modifier(old_slug,project_slug)

    config.read("rest_urls.ini")
    rest_presence = config.get('platform','presence')

    with open('pull_request_platform.json','r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_presence, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "presence"
    project_slug = "api"
    json_modifier(old_slug,project_slug)


def raise_pull_req_connect():

    config.read("rest_urls.ini")
    rest_core = config.get('connect','core')

    with open('pull_request_platform.json','r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_core, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "core"
    project_slug = "http"
    json_modifier_connect(old_slug,project_slug)

    config.read("rest_urls.ini")
    rest_http = config.get('connect','http')

    with open('pull_request_platform.json','r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_http, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "http"
    project_slug = "edi"
    json_modifier_connect(old_slug,project_slug)

    config.read("rest_urls.ini")
    rest_edi = config.get('connect','edi')

    with open('pull_request_platform.json','r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_edi, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "edi"
    project_slug = "bdi"
    json_modifier_connect(old_slug,project_slug)

    config.read("rest_urls.ini")
    rest_bdi = config.get('connect','bdi')

    with open('pull_request_platform.json','r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_bdi, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "bdi"
    project_slug = "core"
    json_modifier_connect(old_slug,project_slug)


def json_modifier(old_slug,project_slug):
        f = open('pull_request_platform.json','r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace(old_slug,project_slug)
        f = open('pull_request_platfor.json','w')
        f.write(newdata)
        f.close()

def json_modifier_connect(old_slug,project_slug):

    f = open('pull_request_connect.json','r')
    filedata = f.read()
    f.close()
    newdata = filedata.replace(old_slug,project_slug)
    f = open('pull_request_connect.json','w')
    f.write(newdata)
    f.close()

def json_modifier_v2():

    f = open('pull_request_V2.json','r')
    filedata = f.read()
    f.close()
    newdata = filedata.replace(old_slug,project_slug)
    f = open('pull_request_V2.json','w')
    f.write(newdata)
    f.close()


def raise_pull_req_v2():

    config.read("rest_urls.ini")
    rest_config = config.get('v2','config')

    with open('pull_request_V2.json','r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_config, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "config"
    project_slug = "orders"
    json_modifier_connect(old_slug,project_slug)

    config.read("rest_urls.ini")
    rest_orders = config.get('v2','orders')

    with open('pull_request_V2.json','r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_orders, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "orders"
    project_slug = "contracts"
    json_modifier_connect(old_slug,project_slug)

    config.read("rest_urls.ini")
    rest_contracts = config.get('v2','contracts')

    with open('pull_request_V2.json','r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_contracts, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "contracts"
    project_slug = "unity"
    json_modifier_connect(old_slug,project_slug)

    config.read("rest_urls.ini")
    rest_unity = config.get('v2','unity')

    with open('pull_request_V2.json','r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_unity, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "unity"
    project_slug = "items"
    json_modifier_connect(old_slug,project_slug)

    config.read("rest_urls.ini")
    rest_items = config.get('v2','items')

    with open('pull_request_V2.json','r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_items, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "items"
    project_slug = "config"
    json_modifier_connect(old_slug,project_slug)



#def raise_pull_req_connect():


#def raise_pull_req_V2():

#def raise_pull_request():

def main():

    parser = argparse.ArgumentParser()
    rel = parser.add_argument('rel',help='enter valid release branch')
    tc = parser.add_argument('tc',help='turvo config should be version')
    args = parser.parse_args()
    print args.rel
    print args.tc
    checkout_release(args.rel)
    #raise_pull_req_platform()
'''
    #ver = store_turvo_config_version()

    print "completed in checking out release branch"
#    get_path = set_common_paths()
    for ref_path in set_path:
        v1_merge_changes("2.0.38",ref_path)
'''

#commit_version()

if __name__ == "__main__":
    main()
