
import sys
import os
import datetime
import git
import html
import subprocess
import commands
#########################################################################################
if len(sys.argv) != 5:
	print("")
	print("Please provide GIT Repo Path and OUTPUT Release Note Path")
	print("e.g: python create_releaseNote.py <PATH_OF_REPO> <RELEASE_NOTE_PATH>")
	print("")
	exit(1)
else:
	LAST_KNOW_TAG_IWEDIA  = str(sys.argv[1])
	LAST_KNOW_TAG_JIOAPPS  = str(sys.argv[2])
	FIRST_REPO_PATH = str(sys.argv[3])
	OUTPUT_RELEASE_NOTE = str(sys.argv[4])
##########################################################################################


IW_FILE = '/scripts_p2/weekly_iwedia_tags.txt'

'''
def last_known():
	
	with open("last_know",'w') as know:
'''	

	
def tags_info():


	os.chdir('/scripts_p2')
	with open('weekly_iwedia_tags.txt','r') as wk:
	last = wk.readlines()
	last_tag = last[-1].rstrip()
	print last_tag
	os.chdir('/var/STB/JHSD200/')
	latest_tag = subprocess.check_output('git ls-remote --exit-code --tags  sh://git@blrgithub.radisys.com:7999/alm/de/jhsd200.git',shell=True)
	print latest
	
	get_git_info(jio_iwedia,jio_apps)

def get_git_info(iwedia,jio_apps):




    #os.chdir('/stb/CISTB/STB_Sync/rjio-hybrid-amlogic-bluebank')
    #jio_changed = subprocess.check_output('git log --format=%H:%s --since=\"24 hours ago\"',shell=True)
    #print jio_changed
    #jio_history = []
    #jio_history = jio_changed.splitlines()
    #if len(jio_history) == 0:
#		apps_git_diff = "No changes found"
    #else:
#		pass 

    jio_history = iwedia
    #what_changed = commands.getstatusoutput("git log --oneline --format=%H%s")	
    rjio_commit = subprocess.check_output("git rev-parse HEAD~1",shell=True)
    rjio_msg = subprocess.check_output("git show -s --format=%s",shell=True)
    last_commit = subprocess.check_output("git rev-parse HEAD~2",shell=True)
    latest_commit = subprocess.check_output("git rev-parse HEAD~1",shell=True)
    rjio_git_diff = subprocess.check_output("git diff --name-only HEAD^ HEAD",shell=True)

    #os.chdir('/stb/CISTB/STB_Sync/jio-apps')

    #apps_changed = subprocess.check_output('git log --format=%H%s --since=\"24 hours ago\"',shell=True)
    #apps_history = []
    #apps_history = apps_changed.splitlines()	

    #if len(apps_history) == 0:
#		apps_history = "No changes found"
    #else:
#		pass 
    apps_history = jio_apps
    apps_commit = subprocess.check_output("git rev-parse HEAD~1",shell=True)
    apps_msg = subprocess.check_output("git show -s --format=%s",shell=True)
    last_commit = subprocess.check_output("git rev-parse HEAD~2",shell=True)
    latest_commit = subprocess.check_output("git rev-parse HEAD~1",shell=True)
    apps_git_diff = subprocess.check_output("git diff --name-only HEAD^ HEAD",shell=True)


    internal_changed = subprocess.check_output('git log --format=%H%s --since=\"24 hours ago\"',shell=True)
    int_history = []
    int_history = internal_changed.splitlines()	

    if len(int_history) == 0:
		int_history = "No changes found"
    else:
		pass 
    os.chdir('/stb/CISTB/STB_Sync/internal')
    internal_commit = subprocess.check_output("git rev-parse HEAD~1",shell=True)
    last_commit = subprocess.check_output("git rev-parse HEAD~2",shell=True)
    last_commit = last_commit.rstrip()
    print last_commit
    latest_commit = subprocess.check_output("git rev-parse HEAD~1",shell=True)
    latest_commit = latest_commit.rstrip()
    print latest_commit
    internal_git_diff = subprocess.check_output('git diff --name-only '+last_commit+" "+latest_commit,shell=True)
    int_history = internal_git_diff 
   

    write_html(str(rjio_commit),str(rjio_git_diff),str(apps_commit),str(apps_git_diff),str(internal_commit),str(jio_history),apps_history,str(int_history))




def write_html(jio_commit,jio_diff,apps_commit,apps_diff,int_commit,jio_ch,apps_ch,int_ch):
	
	

	os.chdir('/stb/CISTB/STB_Sync/rjio-hybrid-amlogic-bluebank')
	rjio_tag = subprocess.check_output("git describe --tags $(git rev-list --tags --max-count=1)",shell=True)

	os.chdir('/stb/CISTB/STB_Sync/jio-apps')
	apps_tag = subprocess.check_output("git describe --tags $(git rev-list --tags --max-count=1)",shell=True)
	
	html_line= """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    
    <h1>Release Notes</h1>
    <h3>Product:STB-BlueBank</h3>

    <hr>	
    <title>ReleaseNotes</title>
</head>
<body>
	<table style="solid-color:aliceblue" width="200px"  cellspacing="10" border="0px"  solid ="black" cellpadding="0"  border-collapse ="collapse">
            <tr>
                <td>
                    BuildVersion:
                </td>

                <td>
                    http://jiostbsync:8080/blue/organizations/jenkins/P1-STB%2FSyncVerification/detail/SyncVerification/52/pipeline
                </td>
            </tr>
               <tr>
                <td>
                    ArtifactoryPath:
                </td>
                 <td>
                     https://49.40.2.161/artifactory/webapp/#/artifacts/browse/tree/General/STB-Group/New_Test/ReleaseNotes.html
                 </td>
            </tr>
             </tr>
               <tr>
                <td>
                    Revision History:
                </td>
                 <td>
                    Document-1.0
                 </td>
            </tr>
	</table>	
	<h2>>Changelog</h2>
        <table border="1px" border-collapse="collapse">
            <h2>BlueBank Details</h2>


	    <tr>
                <td><b>Branch</b></td>
                <td>" sdk-15042019"</td>
	   </tr>
            <tr>
                <td><b>Version</b></td>
                <td>"""+rjio_tag+"""</td>
            </tr>
	     <tr>
                <td><b>Changes Since Last Build</b></td>
                <td><p>"""+jio_ch+"""</p></td>
            </tr>
            <tr>
                <td><b>Commit</b></td>
                <td>"""+jio_commit+"""</td>
            </tr>

	</table>
	<table border="1px" border-collapse="collapse">
	<h2>Internals Details</h2>

	    <tr>
                <td><b>Branch</b></td>
                <td>" Branch Not Available"</td>
	   </tr>
	    <tr>
                <td><b>Version</b></td>
                <td>"Tag Not Available"</td>
            </tr>
 	     <tr>
                <td><b>Changes Since Last Build</b></td>
                <td>"""+int_ch+"""<br></td>
            </tr>
            <tr>
                <td><b>Commit</b></td>
                <td>"""+int_commit+"""</td>
            </tr>

	</table>

	<table border="1px" border-collapse="collapse">
	<h2>Jio Apps Details</h2>

	    <tr>
                <td><b>Branch</b></td>
                <td>" Branch Not Available"</td>
	   </tr>
	 <tr>
                <td><b>Version</b></td>
                <td>"""+apps_tag+"""</td>
            </tr>
		 <tr>
                <td><b>Changes Since Last Build</b></td>
                <td>"""+apps_ch+"""<br></td>

            </tr>
            <tr>
                <td><b>Commit</b></td>
                <td>"""+apps_commit+"""</td>
            </tr>

        </table>
</body>
</html>"""
	
	with open(OUTPUT_RELEASE_NOTE,'w') as file:
                file.write(html_line)
	file.close()
	os.system('cp -r /scripts/ReleaseNote.html /stb/script/')
def main():
	tags_info()
	#get_git_info()	

if __name__ == "__main__":
    main()
