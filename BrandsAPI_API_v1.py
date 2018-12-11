import requests
 
#date_after="2018//09//01"
#date_before="2018/12/01"
# Sample Basic Auth Url with login values as username and password

url = "URL LINK"
user = "USER"
passwd = "PWD"

# Make a request to the endpoint using the correct auth values
auth_values = (user, passwd)
response = requests.get(url, auth=auth_values)
print(response) 
# Convert JSON to dict and print
#print(response.json())
data = response.json()
print(data)

#import pandas as pd
data.to_csv("myfile.csv")