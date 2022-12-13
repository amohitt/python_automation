# Import the requests library
import requests

# Set the access token
access_token = "use_your_github_tocken"

# Set the username
username = input("Enter the user name:")

# Set the API endpoint
endpoint = "https://api.github.com/users/{}/repos".format(username)

# Set the request headers
headers = {
    "Authorization": "token {}".format(access_token),
    "Accept": "application/vnd.github+json",
}

# Send the GET request
response = requests.get(endpoint, headers=headers)

# Print the response status code
print(response.status_code)

# Print the list of repositories
print(response.json())
