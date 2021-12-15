from config import Config as cfg

import json
import requests as req
import time


authUrl = "https://www.strava.com/oauth/token"
activitiesUrl = "https://www.strava.com/api/v3/athlete/activities"

class Connect:
    
    def __init__(self, clientSecret, clientID, refreshToken):
        self.accessToken = ""
        self.refreshToken = refreshToken
        self.clientSecret = clientSecret
        self.clientID = clientID

    # One time authorization with read_all code
    def authorize(self):
        url = "https://www.strava.com/oauth/token?"
        params = {"client_id" : self.clientID, "client_secret" : self.clientSecret, "code" : cfg.CODE, "grant_type": "authorization_code", "f" : "json"}
        res = req.post(url,params)
        # print(res.json())
        self.refreshToken = res.json()['refresh_token']
        self.accessToken = res.json()['access_token']
        

    def refresh_token(self, url, payload):
        res = req.post(url, params=payload)
        accessToken = res.json()['access_token']
        self.accessToken = accessToken

    def get_activities(self, url, page):
        print(f'Requesting : {url}/{page}')
        header = {'Authorization': 'Bearer ' + self.accessToken}
        param = {'per_page': 200, 'page': page}
        data = req.get(url, headers=header, params=param).json()
        return json.dumps(data,indent=2)


def main():
    conn = Connect(cfg.CLIENT_SECRET,
                    cfg.CLIENT_ID,
                    cfg.REFRESH_TOKEN)
                
    payload = {
        'client_id': conn.clientID,
        'client_secret': conn.clientSecret,
        'refresh_token': conn.refreshToken,
        'grant_type': "refresh_token",
        'f': 'json' 
    }         
    # conn.authorize()  
    conn.refresh_token(authUrl,payload)
    page = 0
    if conn.accessToken != "":
        data  = conn.get_activities(activitiesUrl,page)

    # Paginate and sleep due to request limits set by Strava API
    file = open('sol.json', 'w')
    while data[0] != None:
        page = page + 1
        data  = conn.get_activities(activitiesUrl,page)
        file.write(data)
        time.sleep(1)
    file.close()


if __name__=="__main__":
    main()
