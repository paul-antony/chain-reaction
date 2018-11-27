from train import *
from csv_write import *
from evaluate import *



while True:

	train(1)
	train(2)

	data = []

	data.append(rand1())
	data.append(rand2())

	data.append(alpha1(1))
	data.append(alpha2(1))

	data.append(alpha1(2))
	data.append(alpha2(2))

	write_to_csv(data,"pastdata.csv")



	


	
