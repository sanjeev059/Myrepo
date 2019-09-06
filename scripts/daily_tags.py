import os
import datetime
import git
import html
import commands 
import subprocess

JIO_REPO_PATH = '/stb/CISTB/STB_Sync/rjio-hybrid-amlogic-bluebank'
IWEDIA = "/scripts/daily_iwedia_tags.txt"
JIO_APPS = "/scripts/daily_jioapps_tags.txt"
APPS_REPO_PATH = '/stb/CISTB/STB_Sync/jio-apps'
#JIO_REPO_PATH = '/root/Sanjeev_Works/Apps'


def get_iwedia_tag_info():
	os.chdir(JIO_REPO_PATH)
	#os.system("git pull origin")
	#latest_tag = subprocess.check_output("git describe --tags",shell=True)
	latest_tag = subprocess.check_output("git describe --tags $(git rev-list --tags --max-count=1)",shell=True)
	with open(IWEDIA,'a') as file:
              	file.write(latest_tag)
	file.close()

def get_jioapps_tag_info():

	os.chdir(APPS_REPO_PATH)
	#latest_tag = subprocess.check_output("git describe --tags",shell=True)
	latest_tag = subprocess.check_output("git describe --tags $(git rev-list --tags --max-count=1)",shell=True)
	with open(JIO_APPS,'a') as file:
                file.write(latest_tag)
	file.close()

def remove_duplicates():
	os.system("uniq /scripts/daily_iwedia_tags.txt /scripts/output.txt")
	os.system("mv /scripts/output.txt /scripts/daily_iwedia_tags.txt")
	os.system("uniq /scripts/daily_jioapps_tags.txt /scripts/output.txt")
	os.system("mv /scripts/output.txt /scripts/daily_jioapps_tags.txt")

def main():
	get_iwedia_tag_info()	
	get_jioapps_tag_info()	
	remove_duplicates()

if __name__ == "__main__":
    main()

