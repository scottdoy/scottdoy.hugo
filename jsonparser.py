#!/usr/bin/env python
# coding=utf-8

import os
import json 
import sys 
import codecs 
import re

import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--input', help="Path to the JSON file exported from Zotero")
parser.add_argument('--output_dir', default='output_mds', help="Output directory for the saved md files")

def load_json_file(json_path):
    """Correctly handles loading strings from disk into JSON object."""
    pass

def fix_datestring(d):
    """Checks string d against various date formats, returns a warning if it doesn't find a match.

    Hugo requires the date yaml field to be of the form yyyy-mm-dd.
    """

    # Construct a map for text-based months
    monthdict = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }

    # yyyy-mm-dd - This is the target format -- just return the string
    p = re.match(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', d)
    if p is not None:
        return d
    
    # yyyy - No month or date available, so just fill in a dummy month and day
    p = re.match(r'[0-9]{4}$',d)
    if p is not None:
        return d + '-01-01'
    
    # mm/dd/yyyy - month, date, and year separated by forward slashes. 
    # Sometimes this appears as m/d/yyyy, or grossly, m/d/yy
    p = re.match(r'([0-9]+)\/([0-9]+)\/([0-9]+)', d)
    if p is not None:
        # pull out the parts and modify according to their lengths
        month = p.group(1)
        day = p.group(2)
        year = p.group(3)
        if len(month) < 2:
            month = '0' + month
        if len(day) < 2:
            day = '0' + day
        if len(year) < 4:
            # This is a massive error because we don't know which century the paper is from. Let's assume that if the paper is published before "30", it's probably from the 2000's.
            if int(year) < 30:
                year = '20' + year
            else:
                year = '19' + year
        return year + '-' + month + '-' + day

    # December 19, 2019 - Month written out, then date, then year. Sometimes there's a comma between day and year, sometimes not. Sometimes the month is abbreviated, which may lead to a period after the month.
    p = re.match(r'([A-Za-z\.]*)\s([0-9]+),\s([0-9]{1,4})', d)
    if p is not None:
        # Take the first three letters of the month name
        # Hopefully the date isn't written with a single letter
        month = p.group(1)[0:3]
        day = p.group(2)
        year = p.group(3)

        # Convert the month to a numeric
        month = str(monthdict[month.lower()])

        return year + '-' + month + '-' + day

    # If none of those match, then simply pass the date back unchanged
    return d

def parse_citation_item(item):
    """Parse the JSON-formatted citation"""
    # First create the filename by pulling the citation key
    file_name = item['citekey']+'.md'

    print('Creating {}'.format(file_name))

    # Check to make sure that the file name is populated (BBT should have taken care of this)
    if file_name == "":
        print('Warning: item ID {} has no citation key, so generating a false one for now.'.format(item['itemID']))
        file_name = item['itemID']+'.md'

    # Check each of the keys we'll use below and add them if they don't exist
    # Put in a blank line here, we'll fix specific ones later
    req_keys = ['title', 'itemType', 'publicationTitle', 'volume', 'issue', 'date', 'DOI', 'abstractNote']

    for req_key in req_keys:
        if req_key not in item.keys():
            item[req_key] = "&nbsp;"

    # Fix annoying inconsistencies with title capitalization
    item['title'] = item['title'].title()

    # Fix for missing DOIs
    if item['DOI'] == "&nbsp;":
        item['DOI'] = "none"

    # Change the item type to be appropriate for Hugo
    if item['itemType'] == 'conferencePaper':
        item['itemType'] = 'conference'
    elif item['itemType'] == 'journalArticle':
        item['itemType'] = 'journal'

    # Create a string list of authors
    authors = []
    author_list = item['creators']
    for author in author_list:
        authors.append('{}, {}.'.format(author['lastName'], author['firstName'][0]))
    item['authors'] = ', '.join(authors)

    # fix the date with our custom date parser! FANCY
    item['date'] = fix_datestring(item['date'])

    # Create a custom citation key that formats based on what data is available
    citestr = ''
    if not item['title'] == "&nbsp;":
        citestr = citestr + item['title'].title()
    if not item['publicationTitle'] == "&nbsp;":
        citestr = citestr + ', <em>' + item['publicationTitle'] + '</em>'
    if not item['volume'] == "&nbsp;":
        citestr = citestr + ', <b>' + item['volume'] + '</b>'
    if not item['issue'] == "&nbsp;":
        citestr = citestr + '(' + item['issue'] + ')'
    if not item['date'] == "&nbsp;":
        # Assume the date has already been fixed above; thus change this to the first four characters (just the year)
        citestr = citestr + ', ' + item['date'][0:4]

    item['citestr'] = citestr
    
    # Construct MD file content based on the type of item we have
    file_content = """---
title: "{title:s}"
author: {authors:s}
status: Published
type: {itemType:s}
citation: "{citestr:s}"
comments: no
doi: {DOI:s}
date: {date:s}
publishdate: {date:s}
---

{abstractNote:s}
""".format(**item)

    return file_name, file_content

if __name__ == '__main__':
    args = parser.parse_args()
    json_path = args.input
    output_dir = args.output_dir

    # Confirm that the JSON file is present
    assert os.path.isfile(json_path), "No JSON file found at {}".format(json_path)

    # If the output dir doesn't exist, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Load the JSON file
    with open(json_path, 'rb') as json_file:
        try:
            citationdata = json.load(json_file)
        except:
            # Try calling our new function
            raise Exception("An error occurred with loading the JSON file. Probably weird quotation marks in one of the citations.")

    
    # Pull out the citation items
    items = citationdata['items']

    # cycle through each item
    for item in items:
        # Send this item to the parser function
        # Receive back a filename and a file content string
        file_name, file_string = parse_citation_item(item)

        # Create the file and dump the contents into it
        with codecs.open(os.path.join(output_dir, file_name), 'w', 'utf-8-sig') as output:
            output.write(file_string)