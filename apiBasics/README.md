# Authentication

1. Get authorization code from authorization page. This is a one time, manual step.
   Paste the below code in a browser, hit enter then copy the "code" part from the resulting url and
   record this value so that you may use it in the next step. Note activity:read_all scope is very important.

https://www.strava.com/oauth/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=http://localhost&response_type=code&scope=activity:read_all

2. Exchange authorization code for access token & refresh token. This is done via post request in connect.py (see Connect.authorize()). Once
   this is done, you may get rid of the code from the previous step and use the refresh_token to continuously refresh your access_token (since the access_token expires occasionally). This is done in Connect.refresh_token(). Note this is a POST request.

https://www.strava.com/oauth/token?client_id=your_client_id&client_secret=your_client_secret&code=your_code_from_previous_step&grant_type=authorization_code

3. View your activities using the access token just received, this is a GET request and you may use the URL below. Make sure to not
   exceed the request limits of 600 request per 15 minutes or 30000 daily.

https://www.strava.com/api/v3/athlete/activities?access_token=access_token_from_previous_step

4. Use refresh token to refresh new access tokens before you make any GET requests for activities.

https://www.strava.com/oauth/token?client_id=your_client_id&client_secret=your_client_secret&refresh_token=your_refresh_token_from_previous_step&grant_type=refresh_token
