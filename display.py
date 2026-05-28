import json
#load json file
def load_data(filename):
    with open(filename,"r")as f:
        data=json.load(f)
    return data

data=load_data("data.json")
# print(data)

#display user and their connections
def display_users(data):
    print("Users and their connection:\n")
    for user in data["users"]:
        print(f"{user['name']} (ID: {user['id']}) - Friends :{user['friends']} - Liked pages :{user['liked_pages']}")
    print("\nPages:\n") 
    for page in data["pages"]:
        print(f"{page['id']}:{page['name']}")
    

display_users(data)

