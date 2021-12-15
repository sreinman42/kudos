## API Basics

Some notes on how to manually request data from Strava. This is all transcribed or paraphrased from [Strava's API docs](https://developers.strava.com/docs/getting-started/).

### Basic cURL request

Get `YOURACCESSTOKEN` from the [Strava API page](https://www.strava.com/settings/api)

Execute the following: 

	curl -X GET \
	https://www.strava.com/api/v3/athlete \
	-H 'Authorization: Bearer YOURACCESSTOKEN'

### Authentication

Here's an example of getting an authorization code.

1. Go to <https://www.strava.com/settings/api> and copy your Client ID.
2. Paste your Client ID into this URL: `http://www.strava.com/oauth/authorize?client_id=[REPLACE_WITH_YOUR_CLIENT_ID]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read_all`
3. Go to a browser.
4. Paste the URL into the browser (changing [REPLACE_WITH_YOUR_CLIENT_ID])
5. Hit enter.
6. When you see the authorization page, click "Authorize"
7. You'll probably get to a site that can't be reached.
8. Check out the URL.
9. Copy the authorization code after `code=` and before `&scope`
10. Make a cURL request:

		curl -X POST https://www.strava.com/oauth/token \
		-F client_id=YOURCLIENTID \
		-F client_secret=YOURCLIENTSECRET \
		-F code=AUTHORIZATIONCODE \
		-F grant_type=authorization_code

