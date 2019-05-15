#! python

# display mission name 
# Launch date
# + one other piece of info
# Tell the user to 'press enter to access'
    #dealers choice to open one link provided by response
''' code to open a link:
import webbrowser
webbrowser.open('http://www.nasa.gov')'''

import requests
import webbrowser
import pprint

spacex = ('https://api.spacexdata.com/v3/launches/latest')
resp = requests.get(spacex)
pprint.pprint(resp)
resp = resp.json()

print(resp['mission_name'], resp['launch_date_local'],
      resp['rocket']['rocket_id'])

nasapic = input('Press Enter to Access: ')
webbrowser.open('https://www.nasa.gov/sites/default/files/atoms/files/spacex_crs-17_mission_overview.pdf')
