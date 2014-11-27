#!/usr/bin/env python

#Autohor: Spenser Sheng


import MockSSH


#
# command: exit
#
def exit_command_success(instance):
    instance.protocol.call_command(
        instance.protocol.commands['_exit'])

def exit_command_failure(instance):
    instance.writeln("MockSSH: supported usage: exit")

def getcmd_exit():
    command_exit = MockSSH.ArgumentValidatingCommand(
        'exit',
        [exit_command_success],
        [exit_command_failure],
        *[])
    return command_exit