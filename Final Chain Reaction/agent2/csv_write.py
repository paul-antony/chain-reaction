#write data to csv file

import csv

def write_to_csv(win,filename):
	with open(filename,"a") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(win)
	csvfile.close()



if __name__ == "__main__":
	write_to_csv(["random player","alpha depth 1","alpha depth 2"],"pastdata.csv")