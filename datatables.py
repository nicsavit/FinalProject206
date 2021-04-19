import json
import requests
import sqlite3
import os

# Weather API
def get_county_weather(lat, lon, start_date, end_date):
    api_result = requests.get(f'https://api.weatherbit.io/v2.0/history/daily?&lat={lat}&lon={lon}&start_date={start_date}&end_date={end_date}&key=ab0294577d37449cb2e5ed6fad640afa')
    data = api_result.json()
    print(data)
    return data


#COVID DATA for Specific County

def get_countydata(county, days):
    api_result_covid_county = requests.get(f"https://disease.sh/v3/covid-19/nyt/counties/{county}?lastdays={days}")
    data = api_result_covid_county.json()
    
    return data

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
get_county_weather(43.308, 83.847, 2021-03-20, 2021-04-18)



