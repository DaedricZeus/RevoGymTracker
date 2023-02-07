# Importing needed packages
import json
import urllib3
from urllib3 import request
import pyodbc
import pandas as pd
from datetime import datetime
#
#

# Getting membership data from Revo
def urlrequest(urlBase, listOfGyms):
	# Define needed variables
	memberCountDf = pd.DataFrame(columns=['Timestamp', 'GymID', 'MemberCount'])
	idCounter = 1
	# Define now to connect to server
	http = urllib3.PoolManager()
	# Loop through the gyms
	for gym in listOfGyms:
		# Make new URL
		newUrl = urlBase + gym + '.json'
		# Get the response from the new URL
		response = http.request('GET', newUrl)
		# Get the member count and put it into a temp dataframe
		memberCount = json.loads(response.data.decode('utf-8'))
		tempDf = pd.DataFrame(data = {'Timestamp':[datetime.now()], 'GymID':[idCounter], 'MemberCount':[memberCount]}, index=[str(idCounter)])
		# Append the temp dataframe into the main dataframe
		memberCountDf = pd.concat([memberCountDf, tempDf], axis=0)
		# Interate the counter
		idCounter += 1
	# Return the list of member counts
	return memberCountDf

# Function that appends the data into the db
def addToDatabase(memberDf):
	# Define needed variables
	server = 'DESKTOP-ES08OQ7\SQLEXPRESS'
	database = 'RevoGym'
	username = 'DESKTOP-ES08OQ7\shado'
	# Connect to the db
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
	cursor = cnxn.cursor()
	# Insert dataframe into SQL Server
	for index, row in memberDf.iterrows():
		cursor.execute("INSERT INTO fact.MembershipNums (TimeOfQuery, GymID, MemberCount) values(?,?,?)", row.Timestamp, row.GymID, row.MemberCount)
	cnxn.commit()
	cursor.close()
	return

# Main Function
def main(listOfGyms):
	urlBase = 'https://revofitness.com.au//wp-content/themes/blankslate/member_visits_v3/'
	memberDf = urlrequest(urlBase, listOfGyms)
	addToDatabase(memberDf)
	return

main(['belmont']) # Must be in the same order at the db