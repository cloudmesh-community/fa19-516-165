# E. Cloudmesh.Shell.2 Write a new command with your first name as the command name.

from __future__ import print_function

from cloudmesh import Shell
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand

class ZhiCommand(PluginCommand):

    @command
    def do_zhi(self, args, arguments):
        """
        ::
        Usage:
        zhi -f FILE
        zhi list
        This command does some useful things.
        Arguments:
            FILE a file name
        Options:
        -f specify the file
        """
        print(arguments)
        if arguments.FILE:
            print("You have used file: ", arguments.FILE)
        return ""