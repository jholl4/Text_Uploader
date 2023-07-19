#! /usr/bin/env python3

import os
import requests

# ip address of the web server should be added here
ip_address = ""
# This is the directory where all of the text files with the feedback are stored
src_dir = "/data/feedback/"
# Keys to use for the temporary dictionaries in the uploader() function
data_keys = ['title', 'name', 'date', 'feedback']
# Add the files in the source directory to a list to be iterated through in the uploader() function
feedback_list = os.listdir(src_dir)

# Define the post function to send the POST to the server
def post(dict: dict):
    resp = requests.post("http://" + ip_address + "/feedback/", json = dict)
    # Make sure an error message isn't returned. You can print the status_code and text of the response objects to check out what's going on.
    # You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.
    print(resp.raise_for_status())
    print(resp.status_code)

# Define the uploader, which will call the post() function at the end.
def uploader():
    # Iterate through the list of files in the source directory
    for file in feedback_list:
        # Open each file, read the lines of the file and add them into a temporary dictionary, then upload them to the web service vie the post() function
        with open(src_dir + file, 'r') as f:
            data_dict = {}
            lines = f.readlines()
            for key, line in zip(data_keys, lines):
                data_dict.update({key: line})
#                print(f"Data: {data_dict}")
            post(data_dict)


if __name__ == "__main__":
    uploader()
