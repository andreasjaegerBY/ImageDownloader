#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module takes a plain file of urls as an argument and downloads all images, storing them on the local hard disk.

Within the following conditions this module supposed to work:
The module is to be used to sequentially downlowed files of a size about 10MB each. 
The module is NOT designed to nandle huge files or huge list of files ot to split op this process in threads.
Also the available disk space is not considered. More exceptions are not handled.
This details can be further implemented or added to this class if required.
"""

from __future__ import division, print_function, absolute_import

import os.path
from urllib2 import Request, urlopen, URLError, HTTPError

from image_downloader import __version__

__author__ = "Andreas Jaeger"
__copyright__ = "Andreas Jaeger"
__license__ = "none"

class ImageDownloader:
    """
    Class for downloading images using an url list and storing them in a local folder.
	
    :Attributes
        __N_stored_files:          Number of stored files
        __N_files_onlist:          Number of requested files 
        __replace_existing_files:  Replace if the file already exist, set to True by default
        __url_list:                list of urls
        __urls_file_name:          file name containing the urls
    """
    __N_stored_files = 0
    __N_files_onlist = 0
    __replace_existing_files = True
    __url_list = []
    __urls_file_name=""

    def __init__(self, urls_file_name):
        """
        Constructor with the plain file, that contains the url list, as parameter is used.
	
	:param urls_file_name: file containing list of urls separated by new lines  
        """
        self.__urls_file_name= urls_file_name
        self.__read_inputfile(self.__urls_file_name) 

    def __read_inputfile(self,urls_file_name):
        """
        Read a plain file (e.g. *.txt),
	
        :param urls_file_name: file containing list of urls separated by new lines  
        
        Every line should contain a valid url.
        Universal newlines is used with text streams in which all of the following are recognized as ending a line: 
        The Unix end-of-line convention '\n', the Windows convention '\r\n', and the old Macintosh convention '\r'. 
        """
        links_file = open(urls_file_name, 'r')
        lines = links_file.read().splitlines()
        __N_files_onlist=0
        for link in lines:
           self.__N_files_onlist+=1
           self.__url_list.append(link);
           links_file.close()

    def __download_url(self, url, output):
        """
        Download a single image from url and write it into a valid output file.
        
	:param url: a valid url
	:param output: full name of the output file, where the image is stored

        The exceptions for HTTPError and  URLError are handeled: 
        in this case the image is not downloaded, but the remaining downloads will continue.
        Often URLError is raised because there is no network connection
        and if a server is unable to fulfil the request a HTTPError is raised.
        E.g. see https://docs.python.org/2/howto/urllib2.html
        """
        try:
           response = urlopen(url)
        except HTTPError as e:
           print('The server couldn\'t fulfill the request.')
           print('Error code: ', e.code)
        except URLError as e:
           print('Connection to the server failed.')
           print('Reason: ', e.reason)
        else:
        # everything is fine
           if (self.__replace_existing_files==True):
              new_file = open(output, "w")
              new_file.write(response.read())
              self.__N_stored_files+=1
              new_file.close()

    def print_statistics(self):
        """
        Prints information about requested and downloaded images.
        """
        N_num=self.__N_stored_files
        N_den=self.__N_files_onlist
        print(N_num,"/",N_den,"=",N_num/N_den*100,"% of images downloaded")

    def execute(self, path):
        """
        Downloads images to the path folder.
        
        :param path: path name of the folder, where to store the downloaded images

        For the naming: input list file name is used as a new image file name 
        and the additional number corresponds to the line number in the url-list file. 
        The new file is stored in path/<name>_<number>.jpg 
        """
        self.__N_stored_files=0
        count=0
        for url_name in self.__url_list:
           count+=1
           base_name=os.path.basename(self.__urls_file_name)
           valid_name=os.path.splitext(base_name)[0]
           output_file_string="{0}_{1}.jpg".format(valid_name,count)
           output_file_name = os.path.join(path,output_file_string)
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


