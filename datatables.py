import json
import requests

#Historical Weather API

# api_key = '777134bd57cb4678b1e144946211404'
# location = "Honolulu, Hawaii"
# date = '2015-01-21'
# api_result = requests.get('http://api.worldweatheronline.com/premium/v1/past-weather.ashx'.format(api_key,location,date))
# api_response = api_result.json()
# print(api_response)

#Another Weather API
# api = requests.get("http://api.weatherapi.com/v1/current.json?key=1fe175ea71524c4691144044211604&q=Charleston")
# r = api.json()
# print(r)


#COVID STATES DAILY
# api_3 = requests.get("https://covidtracking.com/api/states/daily")
# api_r= api_3.json()
# for d in api_r[:5]:
#     print(d)

#By single state by date


# api = requests.get('https://api.covidtracking.com/v1/states/ca/20210101.json')
# print(api.text)




####THESE BOTTOM TWO WORK EVERYTHING ELSE IS JUST AN OPTION#####



#COVID DATA for Specific County



# api_result_covid_county = requests.get("https://disease.sh/v3/covid-19/nyt/counties/Washtenaw?lastdays=10")
# api_response_covid_county = api_result_covid_county.json()
# #print(api_response_covid_county)

# #the apple one has mobility data too 
# #https://corona.lmao.ninja/docs/#/COVID-19%3A%20NYT/get_v3_covid_19_nyt_counties__county_

# api_mobility = requests.get('https://disease.sh/v3/covid-19/apple/countries/US/Ann%20Arbor')
# r = api_mobility.json()
# print(r)