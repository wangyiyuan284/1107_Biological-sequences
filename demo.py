# -*- coding: utf-8 -*-
import requests
import re
import openpyxl
from bs4 import BeautifulSoup

# Get user's inputet

# proteinFamily = str(input("Please enter the specified protein family:"))
# taxonomicGroup = str(input("Please enter the specified taxonomic group:"))

with open("input_data/user_specified.txt","r") as file:
    for line in file:
        print (line)