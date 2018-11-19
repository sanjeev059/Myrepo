#!/usr/bin/python

import json
import os

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

config = ConfigParser()
'''
list= [
    {"ParameterKey":"Environment", "ParameterValue": "Production" },
    {"ParameterKey":"Stack", "ParameterValue": "Charlie" },
    {"ParameterKey":"PublicDomain", "ParameterValue": "turvo.com" },
    {"ParameterKey":"PrivateDomain", "ParameterValue": "turvo.net" },
    {"ParameterKey":"Alerts", "ParameterValue": "arn:aws:sns:us-west-2:140539094451:OpsAlerts" },
    {"ParameterKey":"Pager", "ParameterValue": "arn:aws:sns:us-west-2:140539094451:OpsGenie" },
    {"ParameterKey":"EncryptionKey", "ParameterValue": "TurvoProductionKey" },

    {"ParameterKey":"Size", "ParameterValue": "medium" },
    {"ParameterKey":"HomeVersion", "ParameterValue": "1.0.0" },
    {"ParameterKey":"AppVersion", "ParameterValue": "2.86.1" },
    {"ParameterKey":"PreviewVersion", "ParameterValue": "2.86.1" },
    {"ParameterKey":"LobbyVersion", "ParameterValue": "1.1.1" },
    {"ParameterKey":"ApiVersion", "ParameterValue": "2018.10.17.3" },
    {"ParameterKey":"EventVersion", "ParameterValue": "2018.10.17.3" },
    {"ParameterKey":"SocketVersion", "ParameterValue": "2018.10.17.3" },
    {"ParameterKey":"TrackVersion", "ParameterValue": "2018.10.17.3" },
    {"ParameterKey":"PresenceVersion", "ParameterValue": "2018.10.17.0" }
]
'''


#config.read("Paths_to_version.ini")
#path = config.get('common_paths','production')
#abs_path = os.path.abspath(path)
#print abs_path

def edit_Production_parms(alist):
    config = ConfigParser()
    config.read("Paths_to_version.ini")
    path = config.get('platform-paths','Production')
    abs_path = os.path.abspath(path)
    print "Platform Production pathi=",abs_path
    with open (abs_path ,'w') as json_file:
      json.dump(alist,json_file,sort_keys=True, indent=4, separators=(',', ': '))

def edit_learn_parms(alist):

    config.read("Paths_to_version.ini")
    path = config.get('platform-paths','Learn')
    abs_path = os.path.abspath(path)
    print "Platform Learn path=",abs_path
    with open (abs_path ,'w') as json_file:
        json.dump(alist,json_file,indent=4, separators=(',', ': '))


def edit_demo_parms(alist):

    config.read("Paths_to_version.ini")
    path = config.get('platform-paths','Demo')
    abs_path = os.path.abspath(path)
    print "Platform demo path=",abs_path
    with open (abs_path ,'w') as json_file:
        json.dump(alist,json_file,indent=4, separators=(',', ': '))

def modify_list(my_list):
    my_learn_modify_list = []
    my_demo_modify_list = []
    my_prod_modify_list = []
    my_learn_modify_list = my_list
    my_demo_modify_list = my_list
    my_prod_modify_list = my_list

    #print my_modify_list
######################################## Learn  modification list ends !!!!############################
    config = ConfigParser()
    config.read("Paths_to_version.ini")
    #ParamValue = config.get('learn','Environment')
    #ParamValue = config.get('learn','TrackVersion')
    #ParamValue = config.get('learn','AppVersion')
    #ParamValue = config.get('learn','PreviewVersion')
    #ParamValue = config.get('learn','LobbyVersion')
    #ParamValue = config.get('learn','EventVersion')
    #ParamValue = config.get('learn','SocketVersion')
    #ParamValue = config.get('learn','PresenceVersion')
    #ParamValue = config.get('learn','Stack')
    #ParamValue = config.get('learn','ApiVersion')

    for data in my_learn_modify_list:
       for key,value in data.items():
                #print key,value
                if data["ParameterKey"] == "TrackVersion":
                    ParamValue = config.get('learn','TrackVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "AppVersion":
                    ParamValue = config.get('learn','AppVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "PreviewVersion":
                    ParamValue = config.get('learn','PreviewVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "LobbyVersion":
                    ParamValue = config.get('learn','LobbyVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "EventVersion":
                    ParamValue = config.get('learn','EventVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "SocketVersion":
                    ParamValue = config.get('learn','SocketVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "PresenceVersion":
                    ParamValue = config.get('learn','PresenceVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "Stack":
                    ParamValue = config.get('learn','Stack')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "Environment":
                    ParamValue = config.get('learn','Environment')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "ApiVersion":
                    ParamValue = config.get('learn','ApiVersion')
                    data["ParameterValue"] = ParamValue


    #print my_modify_list
    edit_learn_parms(my_learn_modify_list)

######################################## Learn  modification list ends !!!!############################
########################################Demo modification list !############################
    config = ConfigParser()
    config.read("Paths_to_version.ini")
    #ParamValue = config.get('demo','Environment')
    #ParamValue = config.get('demo','TrackVersion')
    #ParamValue = config.get('demo','AppVersion')
    #ParamValue = config.get('demo','PreviewVersion')
    #ParamValue = config.get('demo','LobbyVersion')
    #ParamValue = config.get('demo','EventVersion')
    #ParamValue = config.get('demo','SocketVersion')
    #ParamValue = config.get('demo','PresenceVersion')
    #ParamValue = config.get('demo','Stack')
    #ParamValue = config.get('demo','ApiVersion')

    for data in my_demo_modify_list:
       for key,value in data.items():
                #print key,value
                if data["ParameterKey"] == "TrackVersion":
                    ParamValue = config.get('demo','TrackVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "AppVersion":
                    ParamValue = config.get('demo','AppVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "PreviewVersion":
                    ParamValue = config.get('demo','PreviewVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "LobbyVersion":
                    ParamValue = config.get('demo','LobbyVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "EventVersion":
                    ParamValue = config.get('demo','EventVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "SocketVersion":
                    ParamValue = config.get('demo','SocketVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "PresenceVersion":
                    ParamValue = config.get('demo','PresenceVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "Stack":
                    ParamValue = config.get('demo','Stack')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "Environment":
                    ParamValue = config.get('demo','Environment')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "ApiVersion":
                    ParamValue = config.get('demo','ApiVersion')
                    data["ParameterValue"] = ParamValue

    #print my_modify_list
    edit_demo_parms(my_demo_modify_list)
########################################Demo modification list ends !!!!############################
#########################################Production List Modifications ##########################

    config = ConfigParser()
    config.read("Paths_to_version.ini")
    #ParamValue = config.get('Production','Environment')
    #ParamValue = config.get('Production','TrackVersion')
    #ParamValue = config.get('Production','AppVersion')
    #ParamValue = config.get('Production','PreviewVersion')
    #ParamValue = config.get('Production','LobbyVersion')
    #ParamValue = config.get('Production','ApiVersion')
    #ParamValue = config.get('Production','EventVersion')
    #ParamValue = config.get('Production','SocketVersion')
    #ParamValue = config.get('Production','PresenceVersion')
    #ParamValue = config.get('Production','Stack')

    for data in my_prod_modify_list:
       for key,value in data.items():
                #print key,value

                if data["ParameterKey"] == "TrackVersion":
                    ParamValue = config.get('Production','TrackVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "AppVersion":
                    ParamValue = config.get('Production','AppVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "PreviewVersion":
                    ParamValue = config.get('Production','PreviewVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "LobbyVersion":
                    ParamValue = config.get('Production','LobbyVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "EventVersion":
                    ParamValue = config.get('Production','EventVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "SocketVersion":
                    ParamValue = config.get('Production','SocketVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "PresenceVersion":
                    ParamValue = config.get('Production','PresenceVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "Stack":
                    ParamValue = config.get('Production','Stack')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "Environment":
                    ParamValue = config.get('Production','Environment')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "ApiVersion":
                    ParamValue = config.get('Production','ApiVersion')
                    data["ParameterValue"] = ParamValue


    edit_Production_parms(my_prod_modify_list)
    #print my_modify_list

#########################################Production List Modifications ends !! ##########################a

##########################################Writting it to Utility Parameters ##############################################


def edit_production_app_parms(alist):

    config.read("Paths_to_version.ini")
    path = config.get('application-paths','app_production')
    abs_path = os.path.abspath(path)
    print "application production path=",abs_path
    with open (abs_path ,'w') as json_file:
        json.dump(alist,json_file,indent=4, separators=(',', ': '))


def edit_learn_app_parms(alist):

    config.read("Paths_to_version.ini")
    path = config.get('application-paths','app_learn')
    abs_path = os.path.abspath(path)
    print "application learn path=",abs_path
    with open (abs_path ,'w') as json_file:
        json.dump(alist,json_file,indent=4, separators=(',', ': '))


def edit_demo_app_parms(alist):

    config.read("Paths_to_version.ini")
    path = config.get('application-paths','app_demo')
    abs_path = os.path.abspath(path)
    print "application demo path = ",abs_path
    with open (abs_path ,'w') as json_file:
        json.dump(alist,json_file,indent=4, separators=(',', ': '))


def modify_utility_list(my_utility_list):
    utility_learn_env = []
    utility_demo_env = []
    utility_prod_env = []

    utility_learn_env = my_utility_list
    utility_demo_env = my_utility_list
    utility_prod_env = my_utility_list

    config = ConfigParser()
    config.read("Paths_to_version.ini")
    #ParamValue = config.get('utility_demo','Environment')
    #ParamValue = config.get('utility_demo','Stack')
    #ParamValue = config.get('utility_demo','CoreVersion')
    #ParamValue = config.get('utility_demo','HttpVersion')
    #ParamValue = config.get('utility_demo','BdiVersion')
    #ParamValue = config.get('utility_demo','EdiVersion')

    for data in utility_demo_env:
       for key,value in data.items():
                #print key,value
                if data["ParameterKey"] == "Environment":
                    ParamValue = config.get('app-demo','Environment')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "Stack":
                    ParamValue = config.get('app-demo','Stack')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "CoreVersion":
                    ParamValue = config.get('app-demo','CoreVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "HttpVersion":
                    ParamValue = config.get('app-demo','HttpVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "BdiVersion":
                    ParamValue = config.get('app-demo','BdiVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "EdiVersion":
                    ParamValue = config.get('app-demo','EdiVersion')
                    data["ParameterValue"] = ParamValue

    edit_demo_app_parms(utility_demo_env)


    config = ConfigParser()
    config.read("Paths_to_version.ini")
    #ParamValue = config.get('utility-learn','Environment')
    #ParamValue = config.get('utility-learn','Stack')
    #ParamValue = config.get('utility-learn','CoreVersion')
    #ParamValue = config.get('utility-learn','HttpVersion')
    #ParamValue = config.get('utility-learn','BdiVersion')
    #ParamValue = config.get('utility-learn','EdiVersion')

    for data in utility_learn_env:
       for key,value in data.items():
                #print key,value
                if data["ParameterKey"] == "Environment":
                    ParamValue = config.get('app-demo','Environment')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "Stack":
                    ParamValue = config.get('app-demo','Stack')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "CoreVersion":
                    ParamValue = config.get('app-demo','CoreVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "HttpVersion":
                    ParamValue = config.get('app-demo','HttpVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "BdiVersion":
                    ParamValue = config.get('app-demo','BdiVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "EdiVersion":
                    ParamValue = config.get('app-demo','EdiVersion')
                    data["ParameterValue"] = ParamValue
    edit_learn_app_parms(utility_learn_env)


    config = ConfigParser()
    config.read("Paths_to_version.ini")
    #ParamValue = config.get('utility_demo','Environment')
    #ParamValue = config.get('utility_demo','Stack')
    #ParamValue = config.get('utility_demo','CoreVersion')
    #ParamValue = config.get('utility_demo','HttpVersion')
    #ParamValue = config.get('utility_demo','BdiVersion')
    #ParamValue = config.get('utility_demo','EdiVersion')

    for data in utility_prod_env:
       for key,value in data.items():
                #print key,value
                if data["ParameterKey"] == "Environment":
                    ParamValue = config.get('app-demo','Environment')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "Stack":
                    ParamValue = config.get('app-demo','Stack')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "CoreVersion":
                    ParamValue = config.get('app-demo','CoreVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "HttpVersion":
                    ParamValue = config.get('app-demo','HttpVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "BdiVersion":
                    ParamValue = config.get('app-demo','BdiVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "EdiVersion":
                    ParamValue = config.get('app-demo','EdiVersion')
                    data["ParameterValue"] = ParamValue

    edit_production_app_parms(utility_prod_env)
###########################################################utility Paths#############################
def edit_prod_utility_parms(alist):

    config.read("Paths_to_version.ini")
    path = config.get('utility-paths','util_prod__paths')
    abs_path = os.path.abspath(path)
    print "utility production path = ",abs_path
    with open (abs_path ,'w') as json_file:
        json.dump(alist,json_file,indent=4, separators=(',', ': '))


def edit_learn_utility_parms(alist):

    config.read("Paths_to_version.ini")
    path = config.get('utility-paths','util_learn_paths')
    abs_path = os.path.abspath(path)
    print "utility learn path = ",abs_path
    with open (abs_path ,'w') as json_file:
        json.dump(alist,json_file,indent=4, separators=(',', ': '))


def edit_demo_utility_parms(alist):

    config.read("Paths_to_version.ini")
    path = config.get('utility-paths','util_demo_paths')
    abs_path = os.path.abspath(path)
    print "utility demo path = ",abs_path
    with open (abs_path ,'w') as json_file:
        json.dump(alist,json_file,indent=4, separators=(',', ': '))




def modify_utility_list_array(my_utility_list):
    utility_learn_env = []
    utility_demo_env = []
    utility_prod_env = []

    utility_learn_env = my_utility_list
    utility_demo_env = my_utility_list
    utility_prod_env = my_utility_list

    config = ConfigParser()
    config.read("Paths_to_version.ini")
    #ParamValue = config.get('utility_demo','Environment')
    #ParamValue = config.get('utility_demo','Stack')
    #ParamValue = config.get('utility_demo','CoreVersion')
    #ParamValue = config.get('utility_demo','HttpVersion')
    #ParamValue = config.get('utility_demo','BdiVersion')
    #ParamValue = config.get('utility_demo','EdiVersion')

    for data in utility_prod_env:
       for key,value in data.items():
                #print key,value
                if data["ParameterKey"] == "Environment":
                    ParamValue = config.get('utility-production','Environment')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "NotifyVersion":
                    ParamValue = config.get('utility-production','SchedulerVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "SchedulerVersion":
                    ParamValue = config.get('utility-production','NotifyVersion')
                    data["ParameterValue"] = ParamValue


    edit_prod_utility_parms(utility_prod_env)


    config = ConfigParser()
    config.read("Paths_to_version.ini")
    #ParamValue = config.get('utility-learn','Environment')
    #ParamValue = config.get('utility-learn','Stack')
    #ParamValue = config.get('utility-learn','CoreVersion')
    #ParamValue = config.get('utility-learn','HttpVersion')
    #ParamValue = config.get('utility-learn','BdiVersion')
    #ParamValue = config.get('utility-learn','EdiVersion')

    for data in utility_learn_env:
       for key,value in data.items():
                #print key,value
                if data["ParameterKey"] == "Environment":
                    ParamValue = config.get('utility-learn','Environment')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "Stack":
                    ParamValue = config.get('utility-learn','NotifyVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "CoreVersion":
                    ParamValue = config.get('utility-learn','SchedulerVersion')
                    data["ParameterValue"] = ParamValue

    edit_learn_utility_parms(utility_learn_env)


    config = ConfigParser()
    config.read("Paths_to_version.ini")
    #ParamValue = config.get('utility_demo','Environment')
    #ParamValue = config.get('utility_demo','Stack')
    #ParamValue = config.get('utility_demo','CoreVersion')
    #ParamValue = config.get('utility_demo','HttpVersion')
    #ParamValue = config.get('utility_demo','BdiVersion')
    #ParamValue = config.get('utility_demo','EdiVersion')

    for data in utility_demo_env:
       for key,value in data.items():
                #print key,value
                if data["ParameterKey"] == "Environment":
                    ParamValue = config.get('utility-demo','Environment')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "Stack":
                    ParamValue = config.get('utility-demo','NotifyVersion')
                    data["ParameterValue"] = ParamValue

                if data["ParameterKey"] == "CoreVersion":
                    ParamValue = config.get('utility-demo','SchedulerVersion')
                    data["ParameterValue"] = ParamValue

    edit_demo_utility_parms(utility_demo_env)

#sections = config.sections()
#print sections

#sections = config.sections()
#print sections


#for section in sections:
#    options = config.options(section)
#    for option in options:
#        value = config.get(section, option)
#        print option,value



#if __name__ == "__main__":
def main():

    parms_list= [
    {"ParameterKey":"Environment", "ParameterValue": "Production" },
    {"ParameterKey":"Stack", "ParameterValue": "Charlie" },
    {"ParameterKey":"PublicDomain", "ParameterValue": "turvo.com" },
    {"ParameterKey":"PrivateDomain", "ParameterValue": "turvo.net" },
    {"ParameterKey":"Alerts", "ParameterValue": "arn:aws:sns:us-west-2:140539094451:OpsAlerts" },
    {"ParameterKey":"Pager", "ParameterValue": "arn:aws:sns:us-west-2:140539094451:OpsGenie" },
    {"ParameterKey":"EncryptionKey", "ParameterValue": "TurvoProductionKey" },

    {"ParameterKey":"Size", "ParameterValue": "short" },
    {"ParameterKey":"HomeVersion", "ParameterValue": "1.0.0" },
    {"ParameterKey":"AppVersion", "ParameterValue": "2.86.1" },
    {"ParameterKey":"PreviewVersion", "ParameterValue": "2.86.1" },
    {"ParameterKey":"LobbyVersion", "ParameterValue": "1.1.1" },
    {"ParameterKey":"ApiVersion", "ParameterValue": "2018.10.17.3" },
    {"ParameterKey":"EventVersion", "ParameterValue": "2018.10.17.3" },
    {"ParameterKey":"SocketVersion", "ParameterValue": "2018.10.17.3" },
    {"ParameterKey":"TrackVersion", "ParameterValue": "2018.10.17.3" },
    {"ParameterKey":"PresenceVersion", "ParameterValue": "2018.10.17.0" }
]

    #modify_list(list)
    #print mst

    #edit_Production_Params(parms_list)
    modify_list(parms_list)
    #edit_learn_Params(list)
    #edit_Demo_Params(list)
#######################################Utility Arrya#####################################

    utility_list=[
    { "ParameterKey": "PublicDomain", "ParameterValue": "turvo.com" },
    { "ParameterKey": "PrivateDomain", "ParameterValue": "turvo.net" },
    { "ParameterKey": "OpsFoundation", "ParameterValue": "ami-01d8b5bac92c47e63" },
    { "ParameterKey": "OpsAutomate", "ParameterValue": "master" },
    { "ParameterKey": "OpsAlerts", "ParameterValue": "arn:aws:sns:us-west-2:140539094451:OpsAlerts" },
    { "ParameterKey": "OpsPager", "ParameterValue": "arn:aws:sns:us-west-2:140539094451:OpsGenie" },
    { "ParameterKey": "EncryptionKey", "ParameterValue": "TurvoPracticeKey" },
    { "ParameterKey": "Environment", "ParameterValue": "production" },
    { "ParameterKey": "Stack", "ParameterValue": "alpha" },
    { "ParameterKey": "Size", "ParameterValue": "small" },
    { "ParameterKey": "CoreVersion", "ParameterValue": "2018.10.04.0" },
    { "ParameterKey": "HttpVersion", "ParameterValue": "2018.10.04.0" },
    { "ParameterKey": "BdiVersion", "ParameterValue": "2018.09.26.1" },
    { "ParameterKey": "EdiVersion", "ParameterValue": "2018.10.04.1" }
  ]

    #edit_production_utility_parms(utility_list)
    modify_utility_list(utility_list)
############################################Utility Array################################
    utility_array_list= [
    { "ParameterKey": "Environment", "ParameterValue": "Production" },
    { "ParameterKey": "PublicDomain", "ParameterValue": "turvo.com" },
    { "ParameterKey": "PrivateDomain", "ParameterValue": "turvo.net" },
    { "ParameterKey": "Alerts", "ParameterValue": "arn:aws:sns:us-west-2:140539094451:OpsAlerts" },
    { "ParameterKey": "Pager", "ParameterValue": "arn:aws:sns:us-west-2:140539094451:OpsGenie" },
    { "ParameterKey": "EncryptionKey", "ParameterValue": "TurvoProductionKey" },
    { "ParameterKey": "Size", "ParameterValue": "medium" },
    { "ParameterKey": "NotifyVersion", "ParameterValue": "2018.10.31.0" },
    { "ParameterKey": "SchedulerVersion", "ParameterValue": "2018.10.31.1" }
  ]
    modify_utility_list_array(utility_array_list)
##################################3########Utility array end#############################
if __name__ == '__main__':
    main()
