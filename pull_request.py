import requests
import json

import os
import sys
import argparse
import subprocess
import datetime
import re
import urllib2
import time

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser



headers = {'content-type': 'application/json'}

#auth_req = ('kasipathi.n','kindJ3lly81')
auth_req = ('kasipathi.n','hotKit320')
path  = os.environ['HOME']

user_path = os.path.join(path,'workspace')
clon_path = os.path.join(user_path,'test_paths')

api_commit = os.path.join(clon_path,'api')
core_commit = os.path.join(clon_path,'core')
http_commit = os.path.join(clon_path,'http')
edi_commit = os.path.join(clon_path,'edi')
bdi_commit = os.path.join(clon_path,'bdi')
notify_commit = os.path.join(clon_path,'notify')
scheduler_commit = os.path.join(clon_path,'scheduler')

commit_arr = [api_commit,core_commit,http_commit,edi_commit,bdi_commit,notify_commit,scheduler_commit]
#commit_arr = [api_commit,core_commit]



api_path= os.path.join(clon_path,'api/saahas-maven/pom.xml')
core_path= os.path.join(clon_path,'core/pom.xml')
http_path= os.path.join(clon_path,'http/pom.xml')
edi_path= os.path.join(clon_path,'edi/pom.xml')
bdi_path= os.path.join(clon_path,'bdi/pom.xml')
notify_path= os.path.join(clon_path,'notify/pom.xml')
scheduler_path= os.path.join(clon_path,'scheduler/pom.xml')

set_path = [api_path,core_path,http_path,edi_path,bdi_path,notify_path,scheduler_path]

def store_turvo_config_version():
    common_conf = os.path.join (clon_path,'common-config/pom.xml')
    #print common_conf
    m = subprocess.check_output("grep -w '<version>2.0.*</version>' /Users/sanjeev.d/workspace/test_paths/common-config/pom.xml", shell=True)
    str = m[13:19]
    return str

#def copy_version():

def v1_merge_changes(vers,path,):
    var = vers
    var1 = var+"-SNAPSHOT"
    f = open(path,'r')
    filedata = f.read()
    f.close()
    newdata = filedata.replace(var,var1)
    f = open(path,'w')
    f.write(newdata)
    f.close()
    commit_version(path)


def commit_version(path):
    #commit_arr = [api_commit,core_commit,http_commit,edi_commit,bdi_commit,notify_commit,scheduler_commit]
    #commit_arr = [bdi_commit]

    #str(commit)
    r_path = os.path.dirname(path)
    print r_path
    os.chdir(r_path)
    os.system("git add  .")
    print "add"
    time.sleep(5)
    #subprocess.check_output("git commit -m merge_from_release_to_develop",shell=True)
    os.system("git commit -m merger_from_release")
    print "commit"
    time.sleep(5)
    os.system("git push origin")
    print "push"
    time.sleep(5)
    os.chdir(clon_path)
    #print "completd with pom xml merge"
    #api_path = os.path.join(clon_path,"api/saahas-maven")
    #os.chdir(api_path)
    #print api_path
    #subprocess.check_output("sed s/%var/2.0.37-SNAPSHOT/ pom.xml > pom1.xml mv pom1.xml pom.xml", shell=True)

    #subprocess.check_output("sed 's/$var/$var1/' api/saahas-maven/pom.xml > api/saahas-maven/pom1.xml",shell=True)
    #subprocess.check_output('mv api/saahas-maven/pom1.xml api/saahas-maven/pom.xml',shell=True)

#mv api/saahas-maven/pom1.xml api/saahas-maven/pom.xml

def raise_pull_req_common():

    headers = {'content-type': 'application/json'}
    config = ConfigParser()
    config.read("/Users/sanjeev.d/workspace/Myrepo/rest_urls.ini")
    rest_url = config.get('common','common-config')
    print rest_url
    with open('pull_request.json','rw') as json_file:
        data1 = json.load(json_file)
        #r = requests.post(url=rest_url, data=json.dumps(data1), headers=headers,auth=pyload)
        response = requests.request("POST", rest_url, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

def raise_pull_req_platform():
    config = ConfigParser()
    file_ini = os.path.join(user_path,'Myrepo/rest_urls.ini')
    print file_ini
    config.read(file_ini)
    rest_api = config.get('platform','api')
    print rest_api

    platform_json = os.path.join(user_path,'Myrepo/pull_request_platform.json')
    with open(platform_json,'r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_api, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text


    old_slug = "api"
    project_slug = "notify"
    json_modifier(old_slug,project_slug)
    file_ini = os.path.join(user_path,'Myrepo/rest_urls.ini')
    config.read(file_ini)
    rest_notify = config.get('platform','notify')
    platform_json = os.path.join(user_path,'Myrepo/pull_request_platform.json')
    with open(platform_json,'r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_notify, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "notify"
    project_slug = "scheduler"
    json_modifier(old_slug,project_slug)
    file_ini = os.path.join(user_path,'Myrepo/rest_urls.ini')
    config.read(file_ini)
    rest_notify = config.get('platform','scheduler')
    platform_json = os.path.join(user_path,'Myrepo/pull_request_platform.json')
    with open(platform_json,'r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_notify, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "scheduler"
    project_slug = "presence"
    json_modifier(old_slug,project_slug)
    file_ini = os.path.join(user_path,'Myrepo/rest_urls.ini')
    config.read(file_ini)
    rest_presence = config.get('platform','presence')
    platform_json = os.path.join(user_path,'Myrepo/pull_request_platform.json')
    with open(platform_json,'r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_presence, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "presence"
    project_slug = "api"
    json_modifier(old_slug,project_slug)


def raise_pull_req_connect():
    config = ConfigParser()
    file_ini = os.path.join(user_path,'Myrepo/rest_urls.ini')
    config.read(file_ini)
    rest_core = config.get('connect','core')

    connect_json = os.path.join(user_path,'Myrepo/pull_request_connect.json')
    with open(connect_json,'r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_core, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "core"
    project_slug = "http"
    json_modifier_connect(old_slug,project_slug)
    file_ini = os.path.join(user_path,'Myrepo/rest_urls.ini')
    config.read(file_ini)
    rest_http = config.get('connect','http')

    connect_json = os.path.join(user_path,'Myrepo/pull_request_connect.json')
    with open(connect_json,'r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_http, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "http"
    project_slug = "edi"
    json_modifier_connect(old_slug,project_slug)
    file_ini = os.path.join(user_path,'Myrepo/rest_urls.ini')
    config.read(file_ini)
    rest_edi = config.get('connect','edi')
    connect_json = os.path.join(user_path,'Myrepo/pull_request_connect.json')
    with open(connect_json,'r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_edi, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "edi"
    project_slug = "bdi"
    json_modifier_connect(old_slug,project_slug)
    file_ini = os.path.join(user_path,'Myrepo/rest_urls.ini')
    config.read(file_ini)
    rest_bdi = config.get('connect','bdi')
    connect_json = os.path.join(user_path,'Myrepo/pull_request_connect.json')
    with open(connect_json,'r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_bdi, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "bdi"
    project_slug = "core"
    json_modifier_connect(old_slug,project_slug)


def json_modifier(old_slug,project_slug):
        file_ini = os.path.join(user_path,'Myrepo/pull_request_platform.json')
        f = open(file_ini,'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace(old_slug,project_slug)
        f = open(file_ini,'w')
        f.write(newdata)
        f.close()

def json_modifier_connect(old_slug,project_slug):
    file_ini = os.path.join(user_path,'Myrepo/pull_request_connect.json')
    f = open(file_ini,'r')
    filedata = f.read()
    f.close()
    newdata = filedata.replace(old_slug,project_slug)
    f = open(file_ini,'w')
    f.write(newdata)
    f.close()

def json_modifier_v2():
    file_ini = os.path.join(user_path,'Myrepo/pull_request_V2.json')
    f = open(file_ini,'r')
    filedata = f.read()
    f.close()
    newdata = filedata.replace(old_slug,project_slug)
    f = open('pull_request_V2.json','w')
    f.write(newdata)
    f.close()


def raise_pull_req_v2():
    config = ConfigParser()
    file_ini = os.path.join(user_path,'Myrepo/rest_urls.ini')
    config.read(file_ini)
    rest_config = config.get('v2','config')
    connect_v2 = os.path.join(user_path,'Myrepo/pull_request_V2.json')
    with open(connect_v2,'r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_config, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "config"
    project_slug = "orders"
    json_modifier_connect(old_slug,project_slug)
    file_ini = os.path.join(user_path,'Myrepo/rest_urls.ini')
    config.read(file_ini)
    rest_orders = config.get('v2','orders')
    connect_v2 = os.path.join(user_path,'Myrepo/pull_request_V2.json')
    with open(connect_v2,'r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_orders, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "orders"
    project_slug = "contracts"
    json_modifier_connect(old_slug,project_slug)
    file_ini = os.path.join(user_path,'Myrepo/rest_urls.ini')
    config.read(file_ini)
    rest_contracts = config.get('v2','contracts')
    connect_v2 = os.path.join(user_path,'Myrepo/pull_request_V2.json')
    with open(connect_v2,'r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_contracts, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "contracts"
    project_slug = "unity"
    json_modifier_connect(old_slug,project_slug)
    file_ini = os.path.join(user_path,'Myrepo/rest_urls.ini')
    config.read(file_ini)
    rest_unity = config.get('v2','unity')
    connect_v2 = os.path.join(user_path,'Myrepo/pull_request_V2.json')
    with open(connect_v2,'r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_unity, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "unity"
    project_slug = "items"
    json_modifier_connect(old_slug,project_slug)
    file_ini = os.path.join(user_path,'Myrepo/rest_urls.ini')
    config.read(file_ini)
    rest_items = config.get('v2','items')
    connect_v2 = os.path.join(user_path,'Myrepo/pull_request_V2.json')
    with open(connect_v2,'r') as filedata:
        data1 = json.load(filedata)
        response = requests.request("POST", rest_items, data=json.dumps(data1), headers=headers,auth=auth_req)
        print response.text

    old_slug = "items"
    project_slug = "config"
    json_modifier_connect(old_slug,project_slug)

def copy_branch(rel_branch,path):
    test_const = 'testing_pull_req'
    print path
    f = open(path,'r')
    filedata = f.read()
    print filedata
    f.close()
    newdata = filedata.replace(test_const,rel_branch)
    print newdata
    f = open(path,'w')
    f.write(newdata)
    f.close()

def main():

    parser = argparse.ArgumentParser()
    #parser.add_argument('-rel', '--directory', nargs='+' required=True, action='store', dest='directory', default=False, help="provide directory name")
    parser.add_argument('-rel','--rel',action='store', dest='rel',help='enter valid release branch')
    parser.add_argument('-tc','--tc',action='store', dest='tc',help='turvo config should be version')
    args = parser.parse_args()

    connect_v2 = os.path.join(user_path,'Myrepo/pull_request_V2.json')
    platform = os.path.join(user_path,'Myrepo/pull_request_platform.json')
    connect = os.path.join(user_path,'Myrepo/pull_request_connect.json')
    modify_json = [platform,connect,connect_v2]

    for path_modify in modify_json:
        copy_branch(args.rel,path_modify)

    for ref in commit_arr:

        path = os.path.abspath(ref)
        print path
        os.chdir(path)
        cwd = os.getcwd()
        print cwd
        #subprocess.check_output("git checkout origin develop && git remote update")
        os.system("git checkout develop && git pull")
        os.system("git checkout "+args.rel)
        #v1_merge_changes(args.tc,path)


    for ref in set_path:
        lpath = os.path.abspath(ref)
        print lpath
        v1_merge_changes(args.tc,lpath)

    print "raising pull request for platform "
    raise_pull_req_platform()
    print "raising pull request for connect "
    raise_pull_req_connect()
    print "raising pull request for V2 "
    raise_pull_req_v2()



        #subprocess.check_output("git checkout "+args.rel, shell=True)
        #checkout_release(args.rel)

        #raise_pull_req_platform()

    #ver = store_turvo_config_version()
#    get_path = set_common_paths()



if __name__ == "__main__":
    main()
