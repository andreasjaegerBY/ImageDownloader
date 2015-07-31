#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module takes urls from a file and downloads them to a local path.

It has following limitations:
-Files are downloaded sequentially (no threads are used)
-Only files of relatively small size are guaranteed to be downloaded in a certain time limit. 
-Following exceptions are not handled: 
        -Invalid urls raise ValueError
	-Url-list file needs to be valid and urls separated by new lines
	-Accessing and downloading the url needs to be further handled.
	-Exceptions when creating and accessing files need to be handled.
-New files are stored under path/<url_file_name>_<url_list_number>.jpg
	This guarantees correct matching, without loss of information.

-This limitations can be further extended and new requirements added and implemented in this class.
"""

from __future__ import  print_function, absolute_import
from image_downloader import __version__
from urllib2 import urlopen, URLError, HTTPError
import os.path

__author__ = "Andreas Jaeger"
__copyright__ = "Andreas Jaeger"
__license__ = "none"

class ImageDownloader:
    """
    Class for downloading images using an url list and storing them in a local folder.

    :Attributes
        :__N_stored_files:          Number of stored files
        :__url_list:                list of urls
        :__url_file_name:           file name containing the urls
    """
    __N_stored_files = 0
    __url_list = []
    __url_file_name=""

    def __init__(self, url_file_name):
        """
        Constructor.

        :param url_file_name: file containing list of urls separated by new lines  
        """
        self.__url_file_name= url_file_name
        self.__read_url_file() 

    def __read_url_file(self):
        """
        Read the url file
	
        """
        url_file = open(self.__url_file_name, 'r')
        self.__url_list = url_file.read().splitlines()
        self.__url_list = filter(None, self.__url_list)
        url_file.close()

    def __download_url(self, url, output):
        """
        Download one url file and write it into output.
        
        :param url: a valid url
        :param output: full name of the output file, where the file is will be stored

        """
        try:
           response = urlopen(url)
        except HTTPError as e:
           pass
           #The server couldn't fulfill the request.
        except URLError as e:
           pass
           #Connection to the server failed
        else:
           new_file = open(output, "w")
           new_file.write(response.read())
           self.__N_stored_files+=1
           new_file.close()

    def print_statistics(self):
        """
        Prints information about requested and downloaded images.
        """
        N_num=self.__N_stored_files
        N_den=len(self.__url_list)
        print(N_num,"/",N_den,"=",N_num/N_den*100,"% of images downloaded")

    def execute(self, path):
        """
        Downloads file to the path folder.
        
        :param path: path name of the folder, where to store the downloaded images

        Following naming definition is used: input list file name is used as a new image file name
        and the additional number corresponds to the line number in the url-list file.
        The new file is stored in path/<name>_<number>.jpg
        """
        self.__N_stored_files=0
        count=0
        for url_name in self.__url_list:
	   count+=1
           base_name=os.path.basename(self.__url_file_name)
           base_name_noextention=os.path.splitext(base_name)[0]
           output_file_name = os.path.join(path,"{0}_{1}.jpg".format(base_name_noextention,count))
           self.__download_url(url_name, output_file_name)


def download(urls="list.txt",path="./"):
    """
    Download images using the url list and store them into the path folder.
    
    :param urls: plain text file containing urls separated by new lines.
    :param path: folder path, where the images should be stored
    """
    downloader=ImageDownloader(urls)
    downloader.execute(path)
    downloader.print_statistics()

