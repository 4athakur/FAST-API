import requests,json
headers = {
  'Accept': 'application/json'
}
r = requests.get('https://api.india.delta.exchange/v2/tickers', params={'contract_types':"perpetual_futures"

}, headers = headers)
data_delta_exchange=r.json()
# with open("aaaa.json",'w')as f:
#     json.dump(data_delta_exchange,f)
c=0
res={}

for k in data_delta_exchange['result']:
    c=c+1
    res.update({'B-'+k['symbol'][:-3]+'_USDT':k["funding_rate"]})
    if float(k['funding_rate']) > 0.2 or float(k['funding_rate'])< -0.2:
     print(k['symbol']+" fundig rate is "+ k['funding_rate'])
print(f"Total items for fr status from delta exchane is: {c}")
print(res.items())
