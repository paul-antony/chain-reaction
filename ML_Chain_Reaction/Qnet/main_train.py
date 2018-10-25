from train import *
from csv_write import *
from evaluate import *


count = 0
while True:
	train()
	alpha_csv(alpha())
	random_csv(rand())
	print("round:",count)
	count = count + 1

	