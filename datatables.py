import json
import requests
import sqlite3
import os

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



# #https://corona.lmao.ninja/docs/#/COVID-19%3A%20NYT/get_v3_covid_19_nyt_counties__county_

####THESE BOTTOM TWO WORK EVERYTHING ELSE IS JUST AN OPTION#####



#COVID DATA for Specific County


def get_countydata(county, days):
    api_result_covid_county = requests.get(f"https://disease.sh/v3/covid-19/nyt/counties/{county}?lastdays={days}")
    data = api_result_covid_county.json()
    
    return data

#COVID Mobility Data 

# def get_mobilitydata(country, subregion):
#     api_mobility = requests.get('https://disease.sh/v3/covid-19/apple/countries/US/Ann%20Arbor')
#     mobility_data = api_mobility.json()
#     print(mobility_data)
#     return mobility_data

#DataBases
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def setUpCountyTable(cur,conn):
    counties = [
        "Washtenaw",
        "Cuyahoga",
        "Hennepin",
        "Broward"
    ]
    cur.execute("DROP TABLE IF EXISTS County")
    cur.execute("CREATE TABLE County (id INTEGER PRIMARY KEY, county TEXT)")
    for i in range(len(counties)):
        cur.execute("INSERT INTO County (id,county) VALUES (?,?)",(i,counties[i]))
    conn.commit()

def setUpCovidCountyTable(cur, conn):
     cur.execute("DROP TABLE IF EXISTS Covid")
     cur.execute("CREATE TABLE Covid (id INTEGER, date TEXT, cases INTEGER, deaths INTEGER)")
     counties = [
        "Washtenaw",
        "Cuyahoga",
        "Hennepin",
        "Broward"
    ]
     for c in counties:
        data = get_countydata(c, 30)
        
        for day in data:
            
        
            cur.execute('SELECT id FROM County WHERE county = ?', (day['county'],))
            county_id = cur.fetchone()[0]
            
            cur.execute('INSERT INTO Covid (id, date, cases, deaths) VALUES (?,?,?,?)', (county_id, day['date'], int(day['cases']), int(day['deaths']))) 
           
     conn.commit()



cur, conn = setUpDatabase('covid.db')
setUpCountyTable(cur,conn)
setUpCovidCountyTable(cur, conn)
