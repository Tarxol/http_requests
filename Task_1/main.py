import requests

list_name = 'Hulk', 'Captain America', 'Thanos'

def best_intelligence(list_name):
    intelligence = 0
    best_name = None
    for name in list_name:
        url = "https://superheroapi.com/api/2619421814940190/search/" + name
        response = requests.get(url)
        if intelligence < int(response.json()['results'][0]['powerstats']['intelligence']):
            intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
            best_name = name
        else:
            pass
    return (print(f"\nСамый умный супергерой: {best_name}"))

best_intelligence(list_name)


