import requests, pinder, datetime, time, json

from pinder.campfire import Campfire

username = 'bennington@sourcemap.com'
password = 'qwert12345'
campfire_key = '8abd9023a6166b4f7d8584b75134e374708f8816'
subdomain = 'sourcemap'
room_id = '545902'
basecamp_project_id = '1289262-sharkfin'

def notify_camp(todo):
    c = Campfire(subdomain,campfire_key)
    room = c.room(room_id)
    room.speak(todo)


polling_interval = 5.0 # (100 requests in 3600 seconds)
running= True
while running:
    since = datetime.datetime.now().isoformat()

    time.sleep( polling_interval)
    r = requests.get('https://basecamp.com/2025166/api/v1/projects/'+basecamp_project_id+'/events.json?since='+since+'-04:00', auth=(username, password))
    if r.json()  :
        for item in r.json():
            notify_camp('['+basecamp_project_id+'] '+item['creator']['name']+' '+item['summary']+' - '+item['html_url'])

    print('.')
        
    since = datetime.datetime.now().isoformat()

