================
image_downloader
================

This module takes an url file as an argument and downloads all images, storing them on the local hard disk.


Usage
===========

The module can be excecuted as console skript.
For execution run: 
       image_downloader -i <inputfile> -o <outputpath>


Examples
===========
Run:
       image_downloader -i image_downloader/list.txt -o image_downloader/
This will create the following images:
       image_downloader/list_1.jpg, image_downloader/list_2.jpg, image_downloader/list_3.jpg, image_downloader/list_3.jpg

Requirements to run the console script
===========
Requires virtualenv before cloning the repository:
	virtualenv venv

To make the command script available, execute this inside the cloned repository:
       python setup.py install 

       
Limitations
===========

It has following limitations:
	Files are downloaded sequentially (no threads are used)
	Only files of relatively small size are guaranteed to be downloaded in a certain time limit. 
	Following exceptions are not handled: 
        	-Invalid urls raise ValueError
		-Url-list file needs to be valid and urls separated by new lines
		-Accessing and downloading the url needs to be further handled
		-Exceptions when creating and accessing files need to be handled
	New files are stored under path/<url_file_name>_<url_list_number>.jpg
		-This guarantees correct matching, without loss of information

	This limitations can be further extended and new requirements added and implemented in this class.


Note
====

This project has been set up using PyScaffold 2.3rc11. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.
