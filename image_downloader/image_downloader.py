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
