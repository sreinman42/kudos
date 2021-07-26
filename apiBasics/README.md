## API Basics

Some notes on how to manually request data from Strava.

### Basic cURL request

Get YOURACCESSTOKEN from `https://www.strava.com/settings/api`

Execute the following: 

	curl -X GET \
	https://www.strava.com/api/v3/athlete \
	-H 'Authorization: Bearer YOURACCESSTOKEN'


