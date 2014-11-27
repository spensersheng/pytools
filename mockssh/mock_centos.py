#!/usr/bin/env python
#Author : Spenser Sheng

import sys
import MockSSH

import linux.commands 

from twisted.python import log


#init mock server command list
def getlist_mocksrv_commands():
    
    #get command callback
    cmd_exit=linux.commands.getcmd_exit()
    
    #init fake command list 
    command_list = [cmd_exit]
    
    return command_list


   

#main function
if __name__ == "__main__":
    try:
        #init commands
        command_list=getlist_mocksrv_commands()
        
        #set user name
        users = {'ec2-user': 'spenser'}
        log.startLogging(sys.stderr)
        MockSSH.runServer(command_list,
                      prompt="[ec2-user@ip-127-0-0-1 ~]$",
                      interface='127.0.0.1',
                      port=2333,
                      **users)
        
    except KeyboardInterrupt:
        print "User interrupted"
        sys.exit(1)
