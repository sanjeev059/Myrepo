import os
import xml.etree.ElementTree as et
import argparse
import subprocess

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser



def branch_cut(var_arg1,var_arg2):
    base_path = '/Users/sanjeev.d/workspace/test_paths'
    clone_path = os.path.join(base_path,var_arg1)
    print var_arg1
    print clone_path
    branch = 'rel/branch_cut'
    #print branch

    #git_b = 'git checkout develop  && git pull origin develop && git checkout -b {branch}'2

    if (os.path.exists(clone_path)):
        os.chdir(clone_path)
        os.system('git checkout develop  && git pull origin develop')
        subprocess.check_output("git checkout -b "+branch, shell=True)
        subprocess.check_output("git push -u origin "+branch+':'+branch, shell=True)
        #os.system('git push -u origin test_2019.03.27:test_2019.03.27')
    else:
        os.chdir(base_path)
        os.system('git clone '+var_arg2)
        os.chdir(var_arg1)
        subprocess.check_output("git checkout -b "+branch, shell=True)
        subprocess.check_output("git push -u origin "+branch+':'+branch, shell=True)

def read_urls():
    config = ConfigParser()
    config.read("urls.ini")
    read_recs = ['api','core','http','bdi','edi','presence','notify','orders','items','contracts','unity']
    for rec in read_recs:
        url = config.get('url',rec)
        #print rec+":"+url
        branch_cut(rec,url)


def main():

    #parser = argparse.ArgumentParser()
    #parser.add_argument('component',type=str,help="branch cut ")
    #parser.add_argument('branch',type=str,help="branch cut release/xxxx.xx.xx")
    #args = parser.parse_args()
    #print_agrs(args.component,args.branch)

    read_urls()
if __name__ == "__main__":
    main()
