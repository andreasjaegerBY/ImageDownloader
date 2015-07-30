#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module takes a plaintext file as an argument and downloads all images, storing them on the local hard disk.
"""

from __future__ import division, print_function, absolute_import

import os.path
import urllib2

from image_downloader import __version__

__author__ = "Andreas Jaeger"
__copyright__ = "Andreas Jaeger"
__license__ = "none"

class ImageDownloader:
    """
    define parameters
    """
    __N_stored_files = 0
    __N_files_onlist = 0
    __replace_existing_files = True
    __url_list = []
    __plain_url_file_name=""

    def __init__(self, url_file_name):
        """
            Constructor with the plain file, that contains the url list, as parameter is used.
        """
        self.__plain_url_file_name= url_file_name
        self.__read_urls_inputfile(self.__plain_url_file_name) 

    def __read_urls_inputfile(self,plain_url_file_name):
        """
        Read a plain file (e.g. *.txt),
        Every line should contain a valid url.
        Universal newlines is used with text streams in which all of the following are recognized as ending a line: 
        The Unix end-of-line convention '\n', the Windows convention '\r\n', and the old Macintosh convention '\r'. 
        """
        links_file = open(plain_url_file_name, 'r')
        lines = links_file.read().splitlines()
        __N_files_onlist=0
        for link in lines:
           self.__N_files_onlist+=1
           self.__url_list.append(link);
           links_file.close()

    def __download_url(self, url, output_file_name):
        """
        Download a single image from url and write it into a valid output file
        """
        try:
           response = urllib2.urlopen(url)
        except  URLError:
           print('no URL')
        if (self.__replace_existing_files==True):
           new_file = open(output_file_name, "w")
           new_file.write(response.read())
           self.__N_stored_files+=1
           new_file.close()

    def print_statistics(self):
        """
        Prints information about requested and downloaded images
        """
        N_num=self.__N_stored_files
        N_den=self.__N_files_onlist
        print(N_num,"/",N_den,"=",N_num/N_den*100,"% of images downloaded")

    def execute(self, path):
        """
        Downloads images to the path folder.
        For the naming: input list file name is used as name and the numbering in the list order. 
        The file is stored in path/<name>_<number>.jpg 
        """
        self.__N_stored_files=0
        count=0
        for url_name in self.__url_list:
           count+=1
           base_name=os.path.basename(self.__plain_url_file_name)
           valid_name=os.path.splitext(base_name)[0]
           output_file_string="{0}_{1}.jpg".format(valid_name,count)
           output_file_name = os.path.join(path,output_file_string)
           self.__download_url(url_name, output_file_name)


def download(url_list_file="list.txt",download_path="./"):
    downloader=ImageDownloader(url_list_file)
    downloader.execute(download_path)
    downloader.print_statistics()


