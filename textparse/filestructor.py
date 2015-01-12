#!/usr/bin/env python
# Author: Spenser Sheng

import os
import re

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
        
    def generate_result_file(self,target_file):
        #set variable
        filename=self._filename
        
        #set regularexp
        re_div_title=re.compile(r'(Division\s+\d+)\s+(.*)')
        re_div_second=re.compile('(\d\d\s\d\d\s\d\d)\s+(.*?)\s+(Division\s+\d+)')
        re_div_third=re.compile('(\d\d\s\d\d\s\d\d)\s+(.*?)\s+(\d\d\s\d\d\s\d\d)')
        re_div_forth=re.compile('(\d\d\s\d\d\s\d\d.\w\d+)\s+(.*?)\s+(\d\d\s\d\d\s\d\d)')
        re_empty_line=re.compile('^\\s+$')
                
        #process
        self._utils.print_info("Now doing the restructing work on the file [%s]..."%filename)
        src_file_handle=open(filename)
        target_lines=[]
                
        src_lines=src_file_handle.readlines()
        
        for line in src_lines:       
            
            #match empty line
            mat_empty_line=re_empty_line.match(line)
            if mat_empty_line:
                continue
                        
            #match title
            mat_div_title=re_div_title.match(line)
            if mat_div_title:
                div_number=mat_div_title.group(1)
                conent=mat_div_title.group(2)
                new_line="%s-%s"%(div_number,conent)
                target_lines.append(new_line)
                
            #match second
            mat_div_second=re_div_second.match(line)
            if mat_div_second:
                head_number=mat_div_second.group(1)
                conent=mat_div_second.group(2)
                new_line="|%s-%s"%(head_number,conent)
                target_lines.append(new_line)
                
            #match third
            mat_div_third=re_div_third.match(line)
            if mat_div_third:
                head_number=mat_div_third.group(1)
                conent=mat_div_third.group(2)
                new_line="|%s-%s"%(head_number,conent)
                target_lines.append(new_line)
                
            #match forth
            mat_div_forth=re_div_forth.match(line)
            if mat_div_forth:
                head_number=mat_div_forth.group(1)
                conent=mat_div_forth.group(2)
                new_line="||%s|%s"%(head_number,conent)
                target_lines.append(new_line)
                
        
        target_contents='\n'.join(target_lines)
        
        target_file_handle=open(target_file, 'w')
        target_file_handle.write(target_contents)
        
        #close file handle
        src_file_handle.close()
        target_file_handle.close()
        
        self._utils.print_info("Generated the restructing file [%s]..."%target_file)
        
        
        
    
    