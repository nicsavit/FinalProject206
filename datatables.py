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
	cur.execute("DROP TABLE IF EXISTS Locations")
	cur.execute("CREATE TABLE Locations (id INTEGER PRIMARY KEY, state TEXT, county TEXT, subregion TEXT)")
	for i in range(len(states)):
		cur.execute("INSERT INTO Locations (id, state, county, subregion) VALUES (?,?,?,?)",(i,states[i], counties[i], subregions[i]))
	conn.commit()

def setUpCovidCountyTable(cur, conn):
	cur.execute("DROP TABLE IF EXISTS Covid")
	cur.execute("CREATE TABLE Covid (id INTEGER, date TEXT, cases INTEGER, deaths INTEGER)")
	counties = [
		"Washtenaw",
		"Cuyahoga",
		"Hennepin",
		"Maricopa"
	]
	for c in counties:
		data = get_countydata(c, 30)

		for day in data:
			cur.execute('SELECT id FROM Locations WHERE county = ?', (day['county'],))
			county_id = cur.fetchone()[0]

			cur.execute('INSERT INTO Covid (id, date, cases, deaths) VALUES (?,?,?,?)', (county_id, day['date'], int(day['cases']), int(day['deaths']))) 
	
	conn.commit()

def setUpMobilityTable(cur,conn):
	cur.execute("DROP TABLE IF EXISTS Mobility")
	cur.execute("CREATE TABLE Mobility (id INTEGER, subregion TEXT, date TEXT, driving REAL, transit REAL, walking REAL)")
	subregions = [
		"Ann Arbor",
		"Cleveland",
		"Minneapolis",
		"Phoenix"
	]
	
	for s in subregions:
		data1 = get_mobilitydata(s)
		cur.execute('SELECT id FROM Locations WHERE subregion = ?', (s,))
		subregion_id = cur.fetchone()[0]
		for day in data1['data']:
			#print(day)
			cur.execute('INSERT INTO Mobility (id, subregion, date, driving, transit, walking) VALUES (?,?,?,?,?,?)', (subregion_id, day['subregion_and_city'],day['date'], float(day['driving']), float(day['transit']),float(day['walking']))) 
	conn.commit()


def setUpVaccineTable(cur,conn):
	cur.execute("DROP TABLE IF EXISTS Vaccination")
	cur.execute("CREATE TABLE Vaccination (id INTEGER, state TEXT, date TEXT, doses_admin INTEGER)")
	states = [
		"Michigan",
		"Ohio",
		"Minnesota",
		"Arizona"
	]
	for s in states:
		data = get_vaccinedata(s,30)
		cur.execute('SELECT id FROM Locations WHERE state= ?', (s,))
		state_id = cur.fetchone()[0]
		for key in data['timeline']:
			cur.execute('INSERT INTO Vaccination (id, state, date, doses_admin) VALUES (?,?,?,?)', (state_id, data['state'], key, int(data['timeline'][key])))
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
setUpLocationTable(cur,conn)
setUpCovidCountyTable(cur, conn)
setUpMobilityTable(cur,conn)

setUpVaccineTable(cur,conn)
# cases_and_vaccine_correlation(cur,conn)