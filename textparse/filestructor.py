#!/usr/bin/env python
# Author: Spenser Sheng

import os

class FileUtils:
    def __init__(self):
        pass
        
    def is_file(self,file_path):
        if os.path.isfile(file_path):
            return True
        else:
            return False
    
    def print_info(self,msg):
        print("%s"%msg)


class FileStructor:
    
    def __init__(self):
        self._filename=None
        self._utils=FileUtils()
    
    def set_src_filename(self,filename):
        self._filename=filename
    
    def get_src_filename(self):
        return self._filename
    
    def verify(self):
        #set variable
        filename=self._filename
        
        #process
        if self._utils.is_file(filename):
            self._utils.print_info("Found the source file [%s]!"%filename)
            return True
        else:
            self._utils.print_info("Can NOT Found the source file [%s]!"%filename)
            return False
        
    def structor(self):
        #set variable
        filename=self._filename
        
        
    
    