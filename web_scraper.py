"""

Main script for interacting with BeautifulSoup and web page navigatio

"""

import os
import sys
import numpy as np

import pandas as pd

import urllib.request
import lxml.etree as ET

# Add in the links for the movies late
main_links = {
    "base_site":"https://www.st-minutiae.com/resources/scripts/",
    "TheNextGeneration":"#thenextgeneration",
    "TheOriginalSeries":"#theoriginalseries",
    "DeepSpaceNine":"#deepspacenine"

}

# somehow get access to the html file for each one of the above links
# there is a search function on the website but it doesn't narrow down to a particular
# line in the script, just whole episodes


try:
   with urllib.request.urlopen('http://www.python.org/') as f:
      print(f.read().decode('utf-8'))
except urllib.error.URLError as e:
   print(e.reason)











