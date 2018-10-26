from train import *
from csv_write import *
from evaluate import *



while True:
	train()
	
	data = []
	data.append(rand())
	data.append(alpha(1))
	data.append(alpha(2))

	write_to_csv(data,"pastdata.csv")


	