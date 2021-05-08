#!/usr/bin/env python3

""" Chris Stone Test Python"""
""" To get back up to speed with python ""

import argparse

# ----------------------------------
def get_args():
	parser = argparse.ArgumentParser(description='Hello')
	parser.add_argument('-n', '--name', metavar='any name', default='Old Guy', help='Old birthdy guy name')
	return parser.parse_args()

# ---------------------------------
def main():
""" Main call for the get_args function """

	args = get_args()
	print('Happy Birthday, ' + args.name + '!')

# --------------------------------
if __name__ == '__main__':
	main()
