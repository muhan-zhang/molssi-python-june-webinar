import os
import argparse

# The file should be renamed as analyze_mdout.py

# Tell argparse to handle arguments
parser = argparse.ArgumentParser(description='This script parses amber mdout files to extract the total energy.')

# Tell argparse what arguments to expect
parser.add_argument('path',help='The filepath to the file to be analyzed.')

# Get arguments from the users
args = parser.parse_args()

filename = args.path

f = open(filename,'r')

# Read the data in the file
data = f.readlines()
f.close()

# Open a file for writing
base_filename = filename.split('.')[0]
output_filename = F'{base_filename}_Etot.txt'
f_write = open('Etot.txt','w+')
f_write.write('Total Energy\n')

etot = []

# Loop through lines in the file
for line in data:
    split_line = line.split()
    
    # Get information from the line
    if 'Etot' in line:
        etot.append(split_line[2])
        
etot = etot[:-2]

for energy in etot:
    f_write.write(F'{energy}\n')
        