Basecamp-Campfire-Hook
======================

A super simple python script that links a Basecamp Project with a campfire chat room. Just run the scipt and it will poll your basecamp project for "events" and then send them directly into your campfire.

Setup
-----

This script can run on your server or locally as long as you can run python and install the prerequisites. Simple fork or download the repository rename config.ini.defaults to config.ini and fill in with your data:

```
[defaults]
username            : email@email.com  # The email address you use to login to basecamp (this is just using simple  access so consider that)
password            : password
campfire_key        : 321654           #   this is your campfire api key. You can find it under 'My Info' in fire
subdomain           : sample           #   Campfire subdomain   *sample*.campfirenow.com
room_id             : 123456           #   Campfire Room Id sample.campfirenow.com/room/*123456*
basecamp_project_id : 123-proj         #   Basecamp project to track basecamp.com/1234567/projects/*123-proj*
basecamp_id         : 123456           #   Base camp account id - https://basecamp.com/*123546*/api/v1/projects/123-proj/
```

Prerequisites
-------------

You will need the following things to run

* [Python](http://www.python.org/)
* [Pinder](https://github.com/rhymes/pinder)
* [Requests](http://docs.python-requests.org/en/latest/)
 

Running
-------

Just run

`python backcamp.py`

