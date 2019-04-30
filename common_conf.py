import os
import xml.etree.ElementTree as et
import argparse
import subprocess
import datetime

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser



def branch_cut(var_arg1,var_arg2,rel_date):
    base_path = '/Users/sanjeev.d/workspace/test_paths'
    clone_path = os.path.join(base_path,var_arg1)
    print var_arg1
    print clone_path
    branch = 'release/'+rel_date
    print branch
    #print branch

    #git_b = 'git checkout develop  && git pull origin develop && git checkout -b {branch}'2

    if (os.path.exists(clone_path)):
        os.chdir(clone_path)
        os.system('git checkout develop  && git pull origin develop')
        subprocess.check_output("git checkout -b "+branch, shell=True)
        #change_turvo_config(base_path)
        subprocess.check_output("git push -u origin "+branch+':'+branch, shell=True)
        #os.system('git push -u origin test_2019.03.27:test_2019.03.27')
    else:
        os.chdir(base_path)
        os.system('git clone '+var_arg2)
        os.chdir(var_arg1)
        subprocess.check_output("git checkout -b "+branch, shell=True)
        subprocess.check_output("git push -u origin "+branch+':'+branch, shell=True)

def read_urls(wed):
    release_date = wed
    config = ConfigParser()
    config.read("urls.ini")
    read_recs = ['api','core','http','bdi','edi','presence','notify','orders','items','contracts','unity','config']
    for rec in read_recs:
        url = config.get('url',rec)
        #print rec+":"+url
        branch_cut(rec,url,release_date)


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


#def change_turvo_config(base_path):
#    pom_path = ['api/saahas-maven/pom.xml',]
#    api_pom = os.join(base_path, 'api/saahas-maven/pom.xml')
#    subprocess.check_output("sed 's/2.0.24-SNAPSHOT/2.0.25/g' api_pom > new.xml")
#    subprocess.check_output(" mv new.xml api_pom")



def main():

    #parser = argparse.ArgumentParser()
    #parser.add_argument('component',type=str,help="branch cut ")
    #parser.add_argument('branch',type=str,help="branch cut release/xxxx.xx.xx")
    #args = parser.parse_args()
    #print_agrs(args.component,args.branch)

    d = datetime.datetime.now()
    next_wednesday = next_weekday(d, 2) # 0 = Monday, 1=Tuesday, 2=Wednesday...
    next_wednesday_str = next_wednesday.strftime('%Y.%m.%d')
    print next_wednesday_str
    wed = next_wednesday_str
    read_urls(wed)

    #change_turvo_config()

if __name__ == "__main__":
    main()
