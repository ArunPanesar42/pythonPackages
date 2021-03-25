# python requests package
# lets connect to live web using python requests api
# we will connect to www.bbc.com and check if web is live
import requests

# responses = requests.get("http://www.bbc.co.uk")
# if responses.status_code == 200:    # Status 200 is the code for when a website is running
#     print(f"The website is up and running and the status code is {responses.status_code}")
# else:
#     print(f"Something went wrong, status code is {responses.status_code}")

response = requests.get("http://www.bbc.co.uk")
if response:
    print(f"success and the status code is {response.status_code}")
elif response:
    print("Failure ")
else:
    print("Something has gone wrong")

# requests go one step further in simplifying this process for us
# if you use response instance

# create a function called status code check
# function should return status code with appropriate message
# DRY
def status_code_check():
    website = input("Enter a Website? include the http:// ")
    responses = requests.get(website)
    if responses.status_code == 200:
        print(f"The website is up and running and the status code is {responses.status_code}")
    else:
        print(f"Something went wrong, status code is {responses.status_code}")

status_code_check()