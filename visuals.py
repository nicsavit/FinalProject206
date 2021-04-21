import json
import requests
import sqlite3
import os
import matplotlib.pyplot as plt
import numpy as np
from datatables import *

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

	state_0 = cur.execute("SELECT doses_admin FROM Vaccination WHERE state = 'Michigan'")
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

	state_1 = cur.execute("SELECT doses_admin FROM Vaccination WHERE state = 'Ohio'")
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

	state_2 = cur.execute("SELECT doses_admin FROM Vaccination WHERE state = 'Minnesota'")
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

	state_3 = cur.execute("SELECT doses_admin FROM Vaccination WHERE state = 'Arizona'")
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

def mobility_visualization(cur, conn):
	x = ["Ann Arbor", "Cleveland", "Minneapolis", "Phoenix"]
	y = [0, 50, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
	avg_walking_increase = []

	city_0 = cur.execute('SELECT walking FROM Mobility WHERE subregion = "Ann Arbor"')
	all_walking_for_city_0 = city_0.fetchall()
	initial_walking_value_for_city_0 = all_walking_for_city_0[0]
	final_walking_value_for_city_0 = all_walking_for_city_0[-1]
	str_inital_0 = str(initial_walking_value_for_city_0)
	str_final_0 = str(final_walking_value_for_city_0)
	strip_inital_0 = str_inital_0.strip('(),')
	strip_final_0 = str_final_0.strip('(),')
	total_walking_change_0 = float(strip_final_0) - float(strip_inital_0)
	average_walking_change_0 = total_walking_change_0/len(all_walking_for_city_0)
	avg_walking_increase.append(average_walking_change_0)

	city_1 = cur.execute('SELECT walking FROM Mobility WHERE subregion = "Cleveland"')
	all_walking_for_city_1 = city_1.fetchall()
	initial_walking_value_for_city_1 = all_walking_for_city_1[0]
	final_walking_value_for_city_1 = all_walking_for_city_1[-1]
	str_inital_1 = str(initial_walking_value_for_city_1)
	str_final_1 = str(final_walking_value_for_city_1)
	strip_inital_1 = str_inital_1.strip('(),')
	strip_final_1 = str_final_1.strip('(),')
	total_walking_change_1 = float(strip_final_1) - float(strip_inital_1)
	average_walking_change_1 = total_walking_change_1/len(all_walking_for_city_1)
	avg_walking_increase.append(average_walking_change_1)

	city_2 = cur.execute('SELECT walking FROM Mobility WHERE subregion = "Minneapolis"')
	all_walking_for_city_2 = city_2.fetchall()
	initial_walking_value_for_city_2 = all_walking_for_city_2[0]
	final_walking_value_for_city_2 = all_walking_for_city_2[-1]
	str_inital_2 = str(initial_walking_value_for_city_2)
	str_final_2 = str(final_walking_value_for_city_2)
	strip_inital_2 = str_inital_2.strip('(),')
	strip_final_2 = str_final_2.strip('(),')
	total_walking_change_2 = float(strip_final_2) - float(strip_inital_2)
	average_walking_change_2 = total_walking_change_2/len(all_walking_for_city_2)
	avg_walking_increase.append(average_walking_change_2)

	city_3 = cur.execute('SELECT walking FROM Mobility WHERE subregion = "Phoenix"')
	all_walking_for_city_3 = city_3.fetchall()
	initial_walking_value_for_city_3 = all_walking_for_city_3[0]
	final_walking_value_for_city_3 = all_walking_for_city_3[-1]
	str_inital_3 = str(initial_walking_value_for_city_3)
	str_final_3 = str(final_walking_value_for_city_3)
	strip_inital_3 = str_inital_3.strip('(),')
	strip_final_3 = str_final_3.strip('(),')
	total_walking_change_3 = float(strip_final_3) - float(strip_inital_3)
	average_walking_change_3 = total_walking_change_3/len(all_walking_for_city_3)
	avg_walking_increase.append(average_walking_change_3)

	print(avg_walking_increase)


	y_pos = np.arange(len(avg_walking_increase))
	plt.bar(y_pos, avg_walking_increase, color = 'orange')
	plt.xlabel("Counties")
	plt.ylabel("Average Change in Walking")
	plt.title("Average Change in Walking by City")
	plt.xticks([0,1,2,3], x)
	plt.show()

#ISSUE!!!!!!!
def covid_and_vaccine_visualization(cur, conn):
	x_covid = ["Washtenaw", "Cuyahoga", "Hennepin", "Maricopa"]
	y_covid = [0, 50, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
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


	x_vaccine = ["Michigan", "Ohio", "Minnesota", "Arizona"]
	y_vaccine = [0, 50, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
	avg_vaccine_increase = []

	state_0 = cur.execute("SELECT doses_admin FROM Vaccination WHERE state = 'Michigan'")
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

	state_1 = cur.execute("SELECT doses_admin FROM Vaccination WHERE state = 'Ohio'")
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

	state_2 = cur.execute("SELECT doses_admin FROM Vaccination WHERE state = 'Minnesota'")
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

	state_3 = cur.execute("SELECT doses_admin FROM Vaccination WHERE state = 'Arizona'")
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


    c = avg_covid_increase
	v = avg_vaccine_increase

	N = 4
	y_pos = np.arange(N)
	width = 0.35
	fig = plt.figure()
	ax = fig.add_axes([0,0,1,1])

	p1 = ax.bar(y_pos, c, width, label='Average Covid Increase')
	p2 = ax.bar(y_pos + width, v, width, label='Average Vaccine Increase')
	ax.set_ylabel('Average Increase of Vaccines and Covid Cases Per Day')
	ax.set_title('Average Increase of Vaccines and Covid Cases Per Day by Location')
	ax.set_xticks([0,1,2,3], x_vaccine)
	ax.legend(loc = 'best')
	ax.autoscale_view()
	plt.show()

def mobility_visualization_2(cur, conn):
	x = ["Ann Arbor", "Cleveland", "Minneapolis", "Phoenix"]
	y = [0, 50, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
	avg_driving_increase = []

	city_0 = cur.execute('SELECT driving FROM Mobility WHERE subregion = "Ann Arbor"')
	all_driving_for_city_0 = city_0.fetchall()
	initial_driving_value_for_city_0 = all_driving_for_city_0[0]
	final_driving_value_for_city_0 = all_driving_for_city_0[-1]
	str_inital_0 = str(initial_driving_value_for_city_0)
	str_final_0 = str(final_driving_value_for_city_0)
	strip_inital_0 = str_inital_0.strip('(),')
	strip_final_0 = str_final_0.strip('(),')
	total_driving_change_0 = float(strip_final_0) - float(strip_inital_0)
	average_driving_change_0 = total_driving_change_0/len(all_driving_for_city_0)
	avg_driving_increase.append(average_driving_change_0)

	city_1 = cur.execute('SELECT driving FROM Mobility WHERE subregion = "Cleveland"')
	all_driving_for_city_1 = city_1.fetchall()
	initial_driving_value_for_city_1 = all_driving_for_city_1[0]
	final_driving_value_for_city_1 = all_driving_for_city_1[-1]
	str_inital_1 = str(initial_driving_value_for_city_1)
	str_final_1 = str(final_driving_value_for_city_1)
	strip_inital_1 = str_inital_1.strip('(),')
	strip_final_1 = str_final_1.strip('(),')
	total_driving_change_1 = float(strip_final_1) - float(strip_inital_1)
	average_driving_change_1 = total_driving_change_1/len(all_driving_for_city_1)
	avg_driving_increase.append(average_driving_change_1)

	city_2 = cur.execute('SELECT driving FROM Mobility WHERE subregion = "Minneapolis"')
	all_driving_for_city_2 = city_2.fetchall()
	initial_driving_value_for_city_2 = all_driving_for_city_2[0]
	final_driving_value_for_city_2 = all_driving_for_city_2[-1]
	str_inital_2 = str(initial_driving_value_for_city_2)
	str_final_2 = str(final_driving_value_for_city_2)
	strip_inital_2 = str_inital_2.strip('(),')
	strip_final_2 = str_final_2.strip('(),')
	total_driving_change_2 = float(strip_final_2) - float(strip_inital_2)
	average_driving_change_2 = total_driving_change_2/len(all_driving_for_city_2)
	avg_driving_increase.append(average_driving_change_2)

	city_3 = cur.execute('SELECT driving FROM Mobility WHERE subregion = "Phoenix"')
	all_driving_for_city_3 = city_3.fetchall()
	initial_driving_value_for_city_3 = all_driving_for_city_3[0]
	final_driving_value_for_city_3 = all_driving_for_city_3[-1]
	str_inital_3 = str(initial_driving_value_for_city_3)
	str_final_3 = str(final_driving_value_for_city_3)
	strip_inital_3 = str_inital_3.strip('(),')
	strip_final_3 = str_final_3.strip('(),')
	total_driving_change_3 = float(strip_final_3) - float(strip_inital_3)
	average_driving_change_3 = total_driving_change_3/len(all_driving_for_city_3)
	avg_driving_increase.append(average_driving_change_3)

	print(avg_driving_increase)


	y_pos = np.arange(len(avg_driving_increase))
	plt.bar(y_pos, avg_driving_increase, color = 'purple')
	plt.xlabel("Counties")
	plt.ylabel("Average Change in Driving")
	plt.title("Average Change in Driving by City")
	plt.xticks([0,1,2,3], x)
	plt.show()

cur, conn = setUpDatabase('covid.db')
covid_visualization(cur, conn)
vaccine_visualization(cur, conn)
mobility_visualization(cur, conn)
covid_and_vaccine_visualization(cur, conn)
mobility_visualization_2(cur, conn)
