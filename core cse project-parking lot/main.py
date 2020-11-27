import Vehicle
from parking_lot import ParkingLot
import argparse


def main():

	parkinglot = ParkingLot()
	parser = argparse.ArgumentParser()  
	'''creating the parser'''
	parser.add_argument( "-f", action="store",  dest ='r_file', help = "provide Input File")
	'''adding arguments to parser'''
	args = parser.parse_args() 
	'''excuting parsr_arg'''
	
	if args.r_file:
		with open(args.r_file) as f:
			for line in f:
				line = line.rstrip('\n') 
				parkinglot.show(line)
	else:
			while True:
				line = input("$ ")
				parkinglot.show(line)

if __name__ == '__main__':
	main()