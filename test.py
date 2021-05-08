#!/usr/bin/env python3


import argparse

# ----------------------------------
def get_args():
	parser = argparse.ArgumentParser(description='Hello')
	parser.add_argument('-n', '--name', metavar='any name', default='Old Guy', help='Old birthdy guy name')
	return parser.parse_args()

# ---------------------------------
def main():
	args = get_args()
	print('Happy Birthday, ' + args.name + '!')

# --------------------------------
if __name__ == '__main__':
	main()
