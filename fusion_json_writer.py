#!/usr/bin/python

import json
import os

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

config = ConfigParser()


def edit_rehearsal_parms(alist):

    config.read("fusion.ini")
    path = config.get('path','union_path')
    base_path ="/Users/sanjeev.d/workspace"
    corrected_path = os.path.join(base_path,path)
    #abs_path = os.path.abspath(path)
    #print "Platform Learn path=",corrected_path
    with open (corrected_path ,'w') as json_file:
        json.dump(alist,json_file,indent=4, separators=(',', ': '))

def modify_list(my_list):
    rehearsal_list = my_list

    config = ConfigParser()
    config.read("fusion.ini")

    for data in rehearsal_list:
       for key,value in data.items():
           #print key+":"+value

           if data["ParameterKey"] == "AutomateVersion":
               ParamValue = config.get('params','AutomateVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "AppVersion":
               ParamValue = config.get('params','AppVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "ApiVersion":
               ParamValue = config.get('params','ApiVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "EventVersion":
               ParamValue = config.get('params','EventVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "TrackVersion":
               ParamValue = config.get('params','TrackVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "VitalVersion":
               ParamValue = config.get('params','VitalVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "OrdersVersion":
               ParamValue = config.get('params','OrdersVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "ContractsVersion":
               ParamValue = config.get('params','ContractsVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "UnityVersion":
               ParamValue = config.get('params','UnityVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "ItemsVersion":
               ParamValue = config.get('params','ItemsVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "LobbyVersion":
               ParamValue = config.get('params','LobbyVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "PresenceVersion":
               ParamValue = config.get('params','PresenceVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "CoreVersion":
               ParamValue = config.get('params','CoreVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "HttpVersion":
               ParamValue = config.get('params','HttpVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "BdiVersion":
               ParamValue = config.get('params','BdiVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "EdiVersion":
               ParamValue = config.get('params','EdiVersion')
               data["ParameterValue"] = ParamValue

           if data["ParameterKey"] == "NotifyVersion":
               ParamValue = config.get('params','NotifyVersion')
               data["ParameterValue"] = ParamValue

               return rehearsal_list
               #edit_rehearsal_parms(rehearsal_list)

def read_json():
    

def main():


    fusion_list = [
    	{ "ParameterKey": "Environment", "ParameterValue": "rehearsal" },
    	{ "ParameterKey": "Stack", "ParameterValue": "bravo" },
    	{ "ParameterKey": "Size", "ParameterValue": "small" },
    	{ "ParameterKey": "EncryptionKey", "ParameterValue": "TurvoPracticeKey" },
    	{ "ParameterKey": "VpcId", "ParameterValue": "vpc-31f08854" },
      { "ParameterKey": "PublicSubnets", "ParameterValue": "subnet-0fbce1ad6a28346f9,subnet-055374021d15fcb17,subnet-0db3e9627e2570361" },
      { "ParameterKey": "PrivateSubnets", "ParameterValue": "subnet-062684528d74564dd,subnet-0cd75249e988a0132,subnet-0c238f9ecf9492859" },
    	{ "ParameterKey": "AutomateVersion", "ParameterValue": "release/2019-02-20" },
    	{ "ParameterKey": "AppVersion", "ParameterValue": "2.105.1" },
    	{ "ParameterKey": "ApiVersion", "ParameterValue": "2019.03.13.5" },
    	{ "ParameterKey": "EventVersion", "ParameterValue": "2019.03.13.5" },
    	{ "ParameterKey": "TrackVersion", "ParameterValue": "2019.03.13.5" },
    	{ "ParameterKey": "VitalVersion", "ParameterValue": "2019.03.13.5" },
    	{ "ParameterKey": "OrdersVersion", "ParameterValue": "2019.03.13.0" },
    	{ "ParameterKey": "ContractsVersion", "ParameterValue": "2019.03.13.0" },
    	{ "ParameterKey": "UnityVersion", "ParameterValue": "2019.03.13.1" },
    	{ "ParameterKey": "ItemsVersion", "ParameterValue": "2019.03.13.0" },
    	{ "ParameterKey": "LobbyVersion", "ParameterValue": "2.0.0" },
    	{ "ParameterKey": "PresenceVersion", "ParameterValue": "2019.01.30.1" },
    	{ "ParameterKey": "CoreVersion", "ParameterValue": "2019.03.13.2" },
    	{ "ParameterKey": "HttpVersion", "ParameterValue": "2019.03.13.0" },
    	{ "ParameterKey": "BdiVersion", "ParameterValue": "2019.03.13.0" },
    	{ "ParameterKey": "EdiVersion", "ParameterValue": "2019.03.13.0" },
    	{ "ParameterKey": "NotifyVersion", "ParameterValue": "2019.02.20.0" }
    ]
    modify_list(fusion_list)
    edit_rehearsal_parms(fusion_list)
    #for data in fusion_list:
       #for key,value in data.items():
           #print key+":"+value

if __name__ == '__main__':
    main()
