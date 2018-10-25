#write data to csv file

import csv

def alpha_csv(win):
	with open("alpha.csv","a") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([win])
	csvfile.close()

def random_csv(win):
	with open("random.csv","a") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([win])
	csvfile.close()



		