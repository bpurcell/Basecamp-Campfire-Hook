import requests, pinder, datetime, time, json
import config

from pinder.campfire import Campfire

def notify_camp(todo):
    c = Campfire(subdomain,campfire_key)
    room = c.room(room_id)
    room.speak(todo)


polling_interval = 5.0 # (100 requests in 3600 seconds)
running= True
while running:
    since = datetime.datetime.now().isoformat()

    time.sleep( polling_interval)
    r = requests.get('https://basecamp.com/'+basecamp_id+'/api/v1/projects/'+basecamp_project_id+'/events.json?since='+since+'-04:00', auth=(username, password))
    if r.json()  :
        for item in r.json():
            notify_camp('['+basecamp_project_id+'] '+item['creator']['name']+' '+item['summary']+' - '+item['html_url'])

    print('.')
        
    since = datetime.datetime.now().isoformat()

