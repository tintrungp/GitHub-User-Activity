import requests
import json

file_path = "data.json"

def main():
    run = True
    while run:
        username = input("github-activity ")
        print(username)
        data = requests.get( "https://api.github.com/users/" + username + "/events")

        jsonData = data.json()
        if jsonData:
            with open(file_path, 'w') as file:
                json.dump(jsonData, file, indent=4)

        if username == 'q':
            break

'''
What I would need to do
- go through the jsonData
- look at each event
    - group up events
    - group up repos for each event
- print out filling in the blanks with the tallies

notes:
- each event has its own way of phrasing
- likely make a dictionary to access
'''

if __name__ == '__main__':
    main()