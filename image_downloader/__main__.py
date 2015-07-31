"""
This module takes urls from a file and downloads them to a local path.

This main function is called as script and uses the module image_downloader.

Usage:
       image_downloader -i <inputfile> -o <outputpath>

"""

import image_downloader
import sys, getopt


def main(argv=None):
   if argv is None:
        argv = sys.argv[1:]
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","opath="])
   except getopt.GetoptError:
      print('image_downloader -i <inputfile> -o <outputpath>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('image_downloader -i <inputfile> -o <outputpath>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         url_list_file = arg
      elif opt in ("-o", "--opath"):
         download_path = arg
      else:
         assert False, "Not handled option"
   try:
        url_list_file, download_path
   except UnboundLocalError, u: 
        usage()
   image_downloader.download(url_list_file,download_path)

def usage():
    print(__doc__)
    sys.exit(2)
