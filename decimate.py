#!/usr/bin/env python3

import argparse
import sys
from re import *

def main():
	parser = argparse.ArgumentParser(description='Decimate a file by keeping certain lines and tossing others.',
		epilog='See the source for more information.')
	parser.add_argument('-n', '--numlines', type=int, metavar='N', default=10,
		help='keep 1 out of N lines')
	parser.add_argument('-o', '--output-file', type=argparse.FileType('w'), metavar='FILE', default=sys.stdout,
		help='the file for the results to be written to (defaults to stdout)')
	parser.add_argument('infile', type=argparse.FileType('r'), metavar='FILE', default=[sys.stdin], nargs='*',
		help='a list of files to be read from in order (defaults to stdin)')
	parser.add_argument('-e', '--expression', default='True',
		help='a boolean-valued Python expression to decide whether to keep or toss a line. Functions from the `re\' module have been imported for use with this option.')
	args = parser.parse_args()
	ln = 0
	for file in args.infile:
		for _line in file:
			line = _line[:-1] # omit the newline for convenience in the expression
			if ln % args.numlines == 0 and eval(args.expression):
				args.output_file.write(_line)
			ln += 1
if __name__ == '__main__':
	main()