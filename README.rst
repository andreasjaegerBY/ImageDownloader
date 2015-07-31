================
image_downloader
================

This module takes an url file as an argument and downloads all images, storing them on the local hard disk.


Usage
===========

The module can be excecuted as console skript.
To make the command skript available execute:
       python setup.py install 
For execution run: 
       image_downloader -i <inputfile> -o <outputpath>
Examples
===========
Run:
       image_downloader -i image_downloader/list.txt -o image_downloader/
This will create the following images:
       image_downloader/list_1.jpg, image_downloader/list_2.jpg, image_downloader/list_3.jpg, image_downloader/list_3.jpg

       
Limitations
===========

It has following limitations:
	-Files are downloaded sequentially.
	-Only files of relatively small size are guranteed to be downloaded in a certain time limit. 
	-Exceptions are not handled.
	-New files are stored under path/<name>_<number>.jpg
	-This limitations can be further extended or added to this class if required.


Note
====

This project has been set up using PyScaffold 2.3rc11. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.
