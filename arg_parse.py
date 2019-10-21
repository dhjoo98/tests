'''
argparse module is a parser(a part of compiler) for arguments & subcommands
'''

import argparse

#step1, create ArgumentParser
parser = argparse.ArgumentParser(description='Process some integers')
# 명령행을 파이썬 데이터형으로 파싱하는데 필요한 모든 정보를 담고 있다. 

#step2, Add arguments
#add_argument() method to fill up ArgumentParser
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default:find the max)')
#two attributes: integers & accumulate

#step3, Parsing Arguments - using parse_args() method
a = parser.parse_args(['--sum', '7','-1','42'])
print(a)
#on script, sys.argv automatically decides the arguments

#source: https://docs.python.org/ko/3.7/library/argparse.html