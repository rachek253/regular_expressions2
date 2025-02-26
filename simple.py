"""
This script extracts data from a simple HTML file and saves it in a JSON file.
Regular expressions are used to extract the table data, and the ordered and unordered lists.
Author: Rachel Newman 
Student ID: 2562294
"""
import re
import json

file_path = '/Users/rachi/OneDrive - Embry-Riddle Aeronautical University/Spring 2025/DS 244/Homework/HW 5/simple.html'
try:
    with open(file_path, encoding="utf-8") as file:
        html = file.read()

        # extract the table data
        regex = re.compile(r"<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*</tr>", re.DOTALL)
        dict_ = {}
        for key, val in regex.findall(html):
            dict_[key] = val

        # extract 1st list - ordered list:
        list_ = re.findall(r"<ol.*?>(.*?)</ol>", html, re.DOTALL)
        ordered_items = re.findall(r"<li>(.*?)</li>", list_[0], re.DOTALL)

        # extract 2nd list - unordered list:
        list_ = re.findall(r"<ul.*?>(.*?)</ul>", html, re.DOTALL)
        ordered_items = re.findall(r"<li>(.*?)</li>", list_[0], re.DOTALL)

        result = {
            "dict": dict_,
            "ordered": ordered_items,
            "unordered": ordered_items
        }
        with open("simple.json", "w", encoding="utf-8") as file:
            json.dump(result, file)
except OSError as e:
    print(e)
