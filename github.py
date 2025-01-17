import requests
import json

file_path = "data.json"

templates = {
    "CommitCommentEvent" : "f'- commented on commit(s) in {repo}'",
    "CreateEvent" : "f'- created a {ref_type} named {repo}'",
    "DeleteEvent" : "f'- deleted a {ref_type} in {repo}'",
    "ForkEvent" : "f'- forked {repo}'",
    "GollumEvent" : "f'- created {createNum} and edited {editNum} wiki pages in {repo}'",
    "IssueCommentEvent" : "f'- {action} an issue comment in {repo}'",
    "IssuesEvent" : "f'- {action} an issue in {repo}'",
    "MemberEvent" : "f'- {action} {memberName} in {repo}'",
    "PublicEvent" : "f'- made {repo} public!'",
    "PullRequestEvent" : "f'- {action} pull request in {repo}'",
    "PullRequestReviewEvent" : "f'- {action} pull request review in {repo}'",
    "PullRequestReviewCommentEvent" : "f'- {action} pull request review comment in {repo}'",
    "PullRequestReviewThreadEvent" : "f'- {action} pull request review comment in {repo}'",
    "PushEvent" : "f'- pushed {size} commits to {repo}'",
    "ReleaseEvent" : "f'- {action} release {releaseName} for {repo}'",
    "SponsorshipEvent" : "f'- {action} a sponsorship listing'",
    "WatchEvent" : "f'- starred {repo}'"
}

def main():
    # Intro Message
    print("\n********* Welcome To The GitHub User Activity CLI *********\n")
    print("A quick how to:")
    print("  1. Enter in the username who's activity you want to see.")
    print("  2. Enter 'q' or 'quit' when you want to exit the program.\n")

    run = True
    while run:
        # User input + fetching data
        username = input("github-activity ")
        data = requests.get( "https://api.github.com/users/" + username + "/events")
        
        # Error Handling
        if data.status_code == 404:
            print("User does not exist, please try again.")
            break

        # Get dictionary data
        jsonData = data.json()

        for event in jsonData:
            payload = event["payload"]
            eventName = event["type"]
            repo = event["repo"]["name"]

            if "action" in payload:
                action = payload["action"]
            if "size" in payload:
                size = payload["size"]
            if "member" in payload:
                memberName = payload["member"]["name"]
            if "release" in payload:
                releaseName = payload["release"]["name"]
            if "ref_type" in payload:
                ref_type = payload["ref_type"]

            createNum = 0
            editNum = 0

            if eventName == "GollumEvent":
                for page in payload["pages"]:
                    if page["action"] == "created":
                        createNum += 1
                    if page["action"] == "edited":
                        editNum += 1

            print(eval(templates[eventName]))

        if username == 'q' or username == 'quit':
            break

if __name__ == '__main__':
    main()