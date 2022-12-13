import json
import requests

# Replace with the name of the repository you want to check
repository = input("Enter ther repository name:")

# Make a request to the GitHub API to get the list of versions for the repository
response = requests.get(f"https://api.github.com/repos/{repository}/tags")

# Check the status code of the response to make sure the request was successful
if response.status_code != 200:
    print(f"Error: Request to GitHub API failed with status code {response.status_code}")
    exit(1)

# Parse the response to get the list of versions
versions = response.json()

# create the list
a = []

# Print the list of versions
for version in versions:
    a.append(version["name"])

name = input("Enter the version: ")
flag = False

# Loop over the elements in the list
for element in a:
    # Check if the condition is met
    if element == name:
        # Set the flag to True
        flag = True
        break

# Print the result
if flag:
    print("Yes")
else:
    print("No")
