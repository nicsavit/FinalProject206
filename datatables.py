import json
import requests
import sqlite3
import os
import matplotlib.pyplot as plt
import numpy as np


#COVID DATA for Specific County

def get_countydata(county, days):
	api_result_covid_county = requests.get(f"https://disease.sh/v3/covid-19/nyt/counties/{county}?lastdays={days}")
	data = api_result_covid_county.json()
	
	return data
#COVID Mobility Data

def get_mobilitydata(subregion):
	 api_mobility = requests.get(f'https://disease.sh/v3/covid-19/apple/countries/US/{subregion}')
	 mobility_data = api_mobility.json()
	 #print(mobility_data)
	 return mobility_data

#Vaccine Data
def get_vaccinedata(state, days):
	api_vaccine = requests.get(f'https://disease.sh/v3/covid-19/vaccine/coverage/states/{state}?lastdays={days}')
	vaccine_data = api_vaccine.json()
	
	return vaccine_data

#DataBases
def setUpDatabase(db_name):
	path = os.path.dirname(os.path.abspath(__file__))
	conn = sqlite3.connect(path+'/'+db_name)
	cur = conn.cursor()
	return cur, conn

def setUpLocationTable(cur,conn):
	states = [
		"Michigan",
		"Ohio",
		"Minnesota",
		"Arizona"
	]
	counties = [
		"Washtenaw",
		"Cuyahoga",
		"Hennepin",
		"Maricopa"
	]
	subregions = [
		"Ann Arbor",
		"Cleveland",
		"Minneapolis",
		"Phoenix"
	]
	#cur.execute("DROP TABLE IF EXISTS Locations")
	cur.execute("CREATE TABLE IF NOT EXISTS Locations (id INTEGER PRIMARY KEY, state TEXT, county TEXT, subregion TEXT)")
	for i in range(len(states)):
		cur.execute("SELECT state FROM Locations WHERE state = ?", (states[i],))
		if cur.fetchone() == None:
			cur.execute("INSERT OR IGNORE INTO Locations (id, state, county, subregion) VALUES (?,?,?,?)",(i,states[i], counties[i], subregions[i]))
			location_tup = (states[i], counties[i], subregions[i])
			conn.commit()
			return location_tup
	

def setUpCovidCountyTable(county, cur, conn):
	#cur.execute("DROP TABLE IF EXISTS Covid")
	cur.execute("CREATE TABLE IF NOT EXISTS Covid (id INTEGER, date TEXT, cases INTEGER, deaths INTEGER)")
	
	
	data = get_countydata(county, 25)

	for day in data:
		cur.execute('SELECT id FROM Locations WHERE county = ?', (day['county'],))
		county_id = cur.fetchone()[0]

		cur.execute('INSERT OR IGNORE INTO Covid (id, date, cases, deaths) VALUES (?,?,?,?)', (county_id, day['date'], int(day['cases']), int(day['deaths']))) 
	
	conn.commit()

def setUpMobilityTable(subregion, cur,conn):
	#cur.execute("DROP TABLE IF EXISTS Mobility")
	cur.execute("CREATE TABLE IF NOT EXISTS Mobility (id INTEGER, subregion TEXT, date TEXT, driving REAL, transit REAL, walking REAL)")

	
	
	data1 = get_mobilitydata(subregion)
	cur.execute('SELECT id FROM Locations WHERE subregion = ?', (subregion,))
	subregion_id = cur.fetchone()[0]
	for day in data1['data']:
		#print(day)
		cur.execute('INSERT OR IGNORE INTO Mobility (id, subregion, date, driving, transit, walking) VALUES (?,?,?,?,?,?)', (subregion_id, day['subregion_and_city'],day['date'], float(day['driving']), float(day['transit']),float(day['walking']))) 
	conn.commit()


def setUpVaccineTable(state, cur,conn):
	#cur.execute("DROP TABLE IF EXISTS Vaccination")
	cur.execute("CREATE TABLE IF NOT EXISTS Vaccination (id INTEGER, state TEXT, date TEXT, doses_admin INTEGER)")
	
	
	data = get_vaccinedata(state,25)
	cur.execute('SELECT id FROM Locations WHERE state= ?', (state,))
	state_id = cur.fetchone()[0]
	for key in data['timeline']:
		cur.execute('INSERT OR IGNORE INTO Vaccination (id, state, date, doses_admin) VALUES (?,?,?,?)', (state_id, data['state'], key, int(data['timeline'][key])))
	conn.commit()
def cases_and_vaccine_correlation(cur,conn):
	cur.execute("SELECT Covid.cases, Vaccination.doses_admin FROM Covid LEFT JOIN Vaccination ON Covid.id = Vaccination.id")
	corr = []
	for row in cur:
		corr.append(row)
	l = {}
	for tup in corr:
		if tup[0] not in l:
			l[tup[0]] = tup[1]
	return l
	




cur, conn = setUpDatabase('covid.db')
location_tup = setUpLocationTable(cur,conn)
if location_tup:
	(state, county, subregion) = location_tup
	setUpCovidCountyTable(county,cur, conn)
	setUpMobilityTable(subregion, cur,conn)
	setUpVaccineTable(state, cur,conn)
	cases_and_vaccine_correlation(cur,conn)