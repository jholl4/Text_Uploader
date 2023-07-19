#! /usr/bin/env python3

import os
import requests

ip_address = 
src_dir = "/data/feedback"
data_keys = ['title', 'name', 'date', 'feedback']

# List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
# Hint: Use os.listdir() method for this, which returns a list of all files and directories in the specified path.
def make_file_list():
    feedback_list = []
    for file in os.listdir(src_dir):
        feedback_list.append(file)
    return(feedback_list)

# You should now have a list that contains all of the feedback files from the path /data/feedback. Traverse over each file and, from
# the contents of these test files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
def make_dict():
    data_dict = {}
    for file in make_file_list():
        with open(src_dir + file, 'r') as f:
            lines = f.readlines()
            for key, line in zip(data_keys, lines):
                data_dict.update({key: line})
    return data_dict
                


# Now, you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.
# Use the Python requests module to post the dictionary to the company's website. Use the request.post() method to make a POST request to:
# http://<corpweb-external-IP>/feedback. Replace <corpweb-external-IP> with corpweb's external IP address.
def post()
    resp = requests.post("http://" + ip_address + "/feedback/", json = make_dict())
    # Make sure an error message isn't returned. You can print the status_code and text of the response objects to check out what's going on.
    # You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.
    print(resp.raise_for_status())
    print(resp.status_code)

if __name__ == "__main__":
    post()
