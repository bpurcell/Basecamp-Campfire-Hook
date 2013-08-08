import requests, pinder, datetime, time, json, ConfigParser

Config = ConfigParser.RawConfigParser()
Config.read("config.ini")

username            = Config.get('defaults','username')
password            = Config.get('defaults','password')
campfire_key        = Config.get('defaults','campfire_key')
subdomain           = Config.get('defaults','subdomain')
room_id             = Config.get('defaults','room_id')
basecamp_project_id = Config.get('defaults','basecamp_project_id')
basecamp_id         = Config.get('defaults','basecamp_id')


from pinder.campfire import Campfire

def notify_camp(todo):
    c = Campfire(subdomain,campfire_key)
    room = c.room(room_id)
    room.speak(todo)


polling_interval = 1 # (100 requests in 3600 seconds)
running= True
while running:
    since = datetime.datetime.now().isoformat()

    time.sleep( polling_interval)
    r = requests.get('https://basecamp.com/'+basecamp_id+'/api/v1/projects/'+basecamp_project_id+'/events.json?since='+since+'-04:00', auth=(username, password))
    if r.json()  :
        for item in r.json():
            notify_camp('['+basecamp_project_id+'] '+item['creator']['name']+' '+item['summary'].replace('<span>:</span>','').replace('&quot;',"`")+' - '+item['html_url'])

    print('.')
        
    since = datetime.datetime.now().isoformat()

