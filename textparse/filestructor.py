#!/usr/bin/env python
# Author: Spenser Sheng

class FileUtils:
    def __init__(self):
        pass
        
    def is_file_check(file_path):
        if os.path.isfile(file_path):
            return True
        else:
            return False



class FileStructor:
    
    def __init__(self):
        self._filename=None
        self._utils=FileUtils()
    
    def set_src_filename(self,filename):
        self._filename=filename
    
    def get_src_filename(self):
        return self._filename
    
    def verify(self):
        pass
        
    def structor(self):
        pass
    
    