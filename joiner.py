import requests

link = input('Discord Invite Link: ')
if len(link) > 6:
    link = link[19:]
apilink = "https://discord.com/api/v8/invites/" + str(link)

print('Wait...')

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            headers={
                'Authorization': token
                }
            requests.post(apilink, headers=headers)
        print ("Tokens have joined!")