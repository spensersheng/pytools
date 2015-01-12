#!/usr/bin/env python
# Author: Spenser Sheng

import unittest
import filestructor


class TestFileStructor(unittest.TestCase):

    def setUp(self):
        self.filestrutor=filestructor.FileStructor()

    def test_set_filename(self):
        filename='test.example'
        self.filestrutor.set_src_filename(filename)
        expect_filename=self.filestrutor.get_src_filename()
        self.assertEqual(filename, expect_filename)
        
    def test_verify(self):
        #false
        filename='abce.txt'
        self.filestrutor.set_src_filename(filename)
        self.assertFalse(self.filestrutor.verify())
        
        #true
        filename='utdata/sample.txt'
        self.filestrutor.set_src_filename(filename)
        self.assertTrue(self.filestrutor.verify())
    
    def test_generate_result_file(self):
        filename='utdata/sample.txt'
        target_file='utdata/sample.txt.ut'
        self.filestrutor.set_src_filename(filename)
        self.filestrutor.generate_result_file(target_file)
        
    def tearDown(self):
        pass