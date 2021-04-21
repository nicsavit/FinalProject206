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

def setUpCountyTable(cur,conn):
	counties = [
		"Washtenaw",
		"Cuyahoga",
		"Hennepin",
		"Maricopa"
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
		"Maricopa"
	]
	for c in counties:
		data = get_countydata(c, 30)

		for day in data:
			cur.execute('SELECT id FROM County WHERE county = ?', (day['county'],))
			county_id = cur.fetchone()[0]

			cur.execute('INSERT INTO Covid (id, date, cases, deaths) VALUES (?,?,?,?)', (county_id, day['date'], int(day['cases']), int(day['deaths']))) 
	
	conn.commit()

def setUpMobilityTable(cur,conn):
	cur.execute("DROP TABLE IF EXISTS Mobility")
	cur.execute("CREATE TABLE Mobility (subregion TEXT, date TEXT, driving REAL, transit REAL, walking REAL)")
	subregions = [
		"Ann Arbor",
		"Cleveland",
		"Minneapolis",
		"Phoenix"
	]
	
	for s in subregions:
		data1 = get_mobilitydata(s)
		#print(data1.keys())
		for day in data1['data']:
			#print(day)
			cur.execute('INSERT INTO Mobility (subregion, date, driving, transit, walking) VALUES (?,?,?,?,?)', (day['subregion_and_city'],day['date'], float(day['driving']), float(day['transit']),float(day['walking']))) 
	conn.commit()

def setUpVaccineTable(cur,conn):
	cur.execute("DROP TABLE IF EXISTS Vaccination")
	cur.execute("CREATE TABLE Vaccination (state TEXT, date TEXT, doses_admin INTEGER)")
	states = [
		"Michigan",
		"Ohio",
		"Minnesota",
		"Arizona"
	]
	for s in states:
		data = get_vaccinedata(s,30)
		# print(data['state'])
		# cur.execute('INSERT INTO Vaccination (state) VALUES (?)', (data['state']))
		for key in data['timeline']:
			cur.execute('INSERT INTO Vaccination (state, date, doses_admin) VALUES (?,?,?)', (data['state'], key, int(data['timeline'][key])))
		conn.commit()

def covid_visualization(cur, conn):
	x = ["Washtenaw", "Cuyahoga", "Hennepin", "Maricopa"]
	y = [0, 50, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
	avg_covid_increase = []

	county_0 = cur.execute('SELECT cases FROM Covid WHERE id = 0')
	all_cases_for_county_0 = county_0.fetchall()
	initial_case_value_for_county_0 = all_cases_for_county_0[0]
	final_case_value_for_county_0 = all_cases_for_county_0[-1]
	str_inital_0 = str(initial_case_value_for_county_0)
	str_final_0 = str(final_case_value_for_county_0)
	strip_inital_0 = str_inital_0.strip('(),')
	strip_final_0 = str_final_0.strip('(),')
	total_case_change_0 = int(strip_final_0) - int(strip_inital_0)
	average_case_change_0 = total_case_change_0/len(all_cases_for_county_0)
	avg_covid_increase.append(average_case_change_0)

	county_1 = cur.execute('SELECT cases FROM Covid WHERE id = 1')
	all_cases_for_county_1 = county_1.fetchall()
	initial_case_value_for_county_1 = all_cases_for_county_1[0]
	final_case_value_for_county_1 = all_cases_for_county_1[-1]
	str_inital_1 = str(initial_case_value_for_county_1)
	str_final_1 = str(final_case_value_for_county_1)
	strip_inital_1 = str_inital_1.strip('(),')
	strip_final_1 = str_final_1.strip('(),')
	total_case_change_1 = int(strip_final_1) - int(strip_inital_1)
	average_case_change_1 = total_case_change_1/len(all_cases_for_county_1)
	avg_covid_increase.append(average_case_change_1)

	county_2 = cur.execute('SELECT cases FROM Covid WHERE id = 2')
	all_cases_for_county_2 = county_2.fetchall()
	initial_case_value_for_county_2 = all_cases_for_county_2[0]
	final_case_value_for_county_2 = all_cases_for_county_2[-1]
	str_inital_2 = str(initial_case_value_for_county_2)
	str_final_2 = str(final_case_value_for_county_2)
	strip_inital_2 = str_inital_2.strip('(),')
	strip_final_2 = str_final_2.strip('(),')
	total_case_change_2 = int(strip_final_2) - int(strip_inital_2)
	average_case_change_2 = total_case_change_2/len(all_cases_for_county_2)
	avg_covid_increase.append(average_case_change_2)

	county_3 = cur.execute('SELECT cases FROM Covid WHERE id = 3')
	all_cases_for_county_3 = county_3.fetchall()
	initial_case_value_for_county_3 = all_cases_for_county_3[0]
	final_case_value_for_county_3 = all_cases_for_county_3[-1]
	str_inital_3 = str(initial_case_value_for_county_3)
	str_final_3 = str(final_case_value_for_county_3)
	strip_inital_3 = str_inital_3.strip('(),')
	strip_final_3 = str_final_3.strip('(),')
	total_case_change_3 = int(strip_final_3) - int(strip_inital_3)
	average_case_change_3 = total_case_change_3/len(all_cases_for_county_3)
	avg_covid_increase.append(average_case_change_3)

	print(avg_covid_increase)


	y_pos = np.arange(len(avg_covid_increase))
	plt.bar(y_pos, avg_covid_increase, color = 'pink')
	plt.xlabel("Counties")
	plt.ylabel("Average Increase of Cases")
	plt.title("Average Increase of Cases by County")
	plt.xticks([0,1,2,3], x)
	plt.show()


def vaccine_visualization(cur, conn):
	# increase of covid cases per day. average change in walking percentage
	x = ["Michigan", "Ohio", "Minnesota", "Arizona"]
	y = [0, 50, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
	avg_vaccine_increase = []

	state_0 = cur.execute('SELECT doses_admin FROM Vaccination WHERE state = Michigan')
	all_vaccines_for_state_0 = state_0.fetchall()
	initial_vaccine_value_for_state_0 = all_vaccines_for_state_0[0]
	final_vaccine_value_for_state_0 = all_vaccines_for_state_0[-1]
	str_inital_0 = str(initial_vaccine_value_for_state_0)
	str_final_0 = str(final_vaccine_value_for_state_0)
	strip_inital_0 = str_inital_0.strip('(),')
	strip_final_0 = str_final_0.strip('(),')
	total_vaccine_change_0 = int(strip_final_0) - int(strip_inital_0)
	average_vaccine_change_0 = total_vaccine_change_0/len(all_vaccines_for_state_0)
	avg_vaccine_increase.append(average_vaccine_change_0)

	state_1 = cur.execute('SELECT doses_admin FROM Vaccination WHERE state = Ohio')
	all_vaccines_for_state_1 = state_1.fetchall()
	initial_vaccine_value_for_state_1 = all_vaccines_for_state_1[0]
	final_vaccine_value_for_state_1 = all_vaccines_for_state_1[-1]
	str_inital_1 = str(initial_vaccine_value_for_state_1)
	str_final_1 = str(final_vaccine_value_for_state_1)
	strip_inital_1 = str_inital_1.strip('(),')
	strip_final_1 = str_final_1.strip('(),')
	total_vaccine_change_1 = int(strip_final_1) - int(strip_inital_1)
	average_vaccine_change_1 = total_vaccine_change_1/len(all_vaccines_for_state_1)
	avg_vaccine_increase.append(average_vaccine_change_1)

	state_2 = cur.execute('SELECT doses_admin FROM Vaccination WHERE state = Minnesota')
	all_vaccines_for_state_2 = state_2.fetchall()
	initial_vaccine_value_for_state_2 = all_vaccines_for_state_2[0]
	final_vaccine_value_for_state_2 = all_vaccines_for_state_2[-1]
	str_inital_2 = str(initial_vaccine_value_for_state_2)
	str_final_2 = str(final_vaccine_value_for_state_2)
	strip_inital_2 = str_inital_2.strip('(),')
	strip_final_2 = str_final_2.strip('(),')
	total_vaccine_change_2 = int(strip_final_2) - int(strip_inital_2)
	average_vaccine_change_2 = total_vaccine_change_2/len(all_vaccines_for_state_2)
	avg_vaccine_increase.append(average_vaccine_change_2)

	state_3 = cur.execute('SELECT doses_admin FROM Vaccination WHERE state = Minnesota')
	all_vaccines_for_state_3 = state_3.fetchall()
	initial_vaccine_value_for_state_3 = all_vaccines_for_state_3[0]
	final_vaccine_value_for_state_3 = all_vaccines_for_state_3[-1]
	str_inital_3 = str(initial_vaccine_value_for_state_3)
	str_final_3 = str(final_vaccine_value_for_state_3)
	strip_inital_3 = str_inital_3.strip('(),')
	strip_final_3 = str_final_3.strip('(),')
	total_vaccine_change_3 = int(strip_final_3) - int(strip_inital_3)
	average_vaccine_change_3 = total_vaccine_change_3/len(all_vaccines_for_state_3)
	avg_vaccine_increase.append(average_vaccine_change_3)

	print(avg_vaccine_increase)


	y_pos = np.arange(len(avg_vaccine_increase))
	plt.bar(y_pos, avg_vaccine_increase, color = 'green')
	plt.xlabel("States")
	plt.ylabel("Average Increase of Vaccines Per Day")
	plt.title("Average Increase of Vaccines Per Day by State")
	plt.xticks([0,1,2,3], x)
	plt.show()



cur, conn = setUpDatabase('covid.db')
setUpCountyTable(cur,conn)
setUpCovidCountyTable(cur, conn)
setUpMobilityTable(cur,conn)
covid_visualization(cur, conn)
get_vaccinedata('Arizona', 30)
setUpVaccineTable(cur,conn)
vaccine_visualization(cur, conn)