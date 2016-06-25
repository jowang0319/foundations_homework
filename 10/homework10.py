import requests
import datetime

response = requests.get("https://api.forecast.io/forecast/apikey/40.7128,-74.0059")
data = response.json()['currently']
data_day = response.json()['daily']['data'][0]


# In[39]:

temp_feeling = ""
if data_day['temperatureMax'] >= 75:
    temp_feeling = "hot"
elif 68 <= data_day['temperatureMax'] < 75:
    temp_feeling = 'warm'
elif 60 <= data_day['temperatureMax'] < 68:
    temp_feeling = 'moderate'
else:
    temp_feeling = 'cold'

rain_w = ""
if data_day['precipProbability'] > 0.5:
    rain_w = '. Bring your umbrella!'
else:
    rain_w = "."

output = "Right now it is",str(data['temperature']),"degrees out and",data['summary'].lower(),". Today will be",temp_feeling,"with a high of",str(data_day['temperatureMax']),'and a low of',str(data_day['temperatureMin']),rain_w
weather = " ".join(output)
today = datetime.datetime.fromtimestamp(int(data['time'])).strftime('%B %d,%Y')
default = "8AM Weather forecast: "
subject = default + today

key = 'key-f3c034a3639d2e64add338456a9758da'
sandbox = 'sandbox98c5a07cbdeb46aca95983991a84c575.mailgun.org'
recipient = 'jowang0319@outlook.com'

request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
request = requests.post(request_url, auth=('api', key), data={
    'from': 'weather@example.com',
    'to': recipient,
    'subject': subject,
    'text': weather
})

print ('Status: {0}'.format(request.status_code))
print ('Body:   {0}'.format(request.text))
