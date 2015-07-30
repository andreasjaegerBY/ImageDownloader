"""
This module image_downloader takes a plaintext file as an argument and downloads all images, storing them on the local hard disk.
This main function is called as script and uses the module image_downloader.
"""

from downloadimg import download_img
import sys, getopt

def main(argv=None):
   if argv is None:
        argv = sys.argv[1:]
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","opath="])
   except getopt.GetoptError:
      print('imagedownloader -i <inputfile> -o <outputpath>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('imagedownloader -i <inputfile> -o <outputpath>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         url_list_file = arg
      elif opt in ("-o", "--opath"):
         download_path = arg
      else:
         assert False, "unhandled option"
   try:
        url_list_file, download_path
   except UnboundLocalError, u: 
        usage()
   download_img.run(url_list_file,download_path)

def usage():
    print(__doc__)
    sys.exit(2)