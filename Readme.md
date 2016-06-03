## Description
RESTful service created in order to show how to interact with the Slack API and GoogleSheet API. 
Basically we are using a web hook to create more commands in the channels of Slack and modify the Google Sheet based on commands.

## Installation
 You only need to run the setup.py file in order to get all the required libraries
  ```sh
  python setup.py install
  ```
  Maybe you should run it as root user
  
  Also, you can create a virtual env in order to keep everything clean, you can refer to this link:
  https://realpython.com/blog/python/python-virtual-environments-a-primer/
  
## Configuration
  In the package source, you will find a YAML file called config, there you have to complete using your SLACK TOKEN, 
  SLACK WEBHOOK TOKEN and the ID or you Google Spreadsheet. Check this:
  https://realpython.com/blog/python/getting-started-with-the-slack-api-using-python-and-flask/
  
  In the package gSheet, you will find a JSON file called service_key, you have to complete it using your SERVICE TOKEN
  of your GOOGLE DEVELOPER ACCOUNT. Check this link:
  http://gspread.readthedocs.io/en/latest/oauth2.html
  

## References

Using SLACK API - https://realpython.com/blog/python/getting-started-with-the-slack-api-using-python-and-flask/

Using Google Sheet API - https://github.com/burnash/gspread

Getting OAuth2 token in Google Developers Console - http://gspread.readthedocs.io/en/latest/oauth2.html

Exposing a internal address externally - https://ngrok.com/

VirtualEnv - https://realpython.com/blog/python/python-virtual-environments-a-primer/
