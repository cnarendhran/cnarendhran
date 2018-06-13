import urllib.request

URL = 'https://reverse.geocoder.cit.api.here.com/6.2/reversegeocode.json?prox=%s,%s,250&mode=retrieveAddresses&maxresults=1&gen=8&app_id=ZsYKZLBuY8QOl4o4t0of&app_code=7x3y_gVqiF2DeHpodgoY7w'

req = urllib.request.Request(URL % (51.1, 17.0333))
response = urllib.request.urlopen(req).read()  # .decode('utf-8')
print(response)
print('******************************************')

res = urllib.request.urlopen(URL % (51.1, 17.0333)).read()
print(res)

