import json
import requests

stop_time = 1535235134
all_data = []

def get_url(sub,start):
    return 'https://api.pushshift.io/reddit/search/submission/?sort=asc&size=1000&after='+str(start)+'&subreddit='+str(sub)

def get_all(subs):
    for sub in subs:
        d = []
        time, len_ = 0, 999
        url = get_url(sub,time)
        while(len_ == 999):
            data = requests.get(url).json()
            d = data['data']
            len_ = len(data['data'])-1
            with open('c:/Users/mayet/Documents/GA-DSI/project-3/mud_mayet_la/data/'+str(sub)+'/data_'+str(data['data'][len_]['created_utc'])+'.json', 'w') as f:
                json.dump(data, f,indent=4)
            all_data.append(data)
            time = d[len_]['created_utc']
            last_id = d[len_]['id']
            url = get_url(sub,time)
            print(time,last_id)
            
get_all(['mildlyinteresting','mildlyinfuriating'])