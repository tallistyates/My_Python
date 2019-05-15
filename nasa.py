#! python3

# API to Retrieve a list of Asteroids based on their closest approach date to Earth.

import requests
import pprint

# define my api key (read from file)
with open('nasaapikey') as keyfile:
    mykey = keyfile.read()

# Add in a start_date = START DATE YYYY-MM-DD
#START_DATE = '2019-04-01'
START_DATE = input('Please enter a start date (YYYY-MM-DD):')


# also add in end_date = END DATE
#END_DATE = '2019-04-07'
END_DATE = input('Please enter a end date (YYYY-MM-DD):')

''' look up nasa api Retrieve a list of Asteroids based on their closest approach date to Earth.
GET https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key=API_KEY'''

bigrocks = requests.get(r"https://api.nasa.gov/neo/rest/v1/feed?start_date=" + START_DATE + "&end_date="+END_DATE + "&api_key="+mykey)


#  dump initial data to screen
pprint.pprint(bigrocks.json())


