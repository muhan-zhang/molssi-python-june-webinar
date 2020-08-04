import os, argparse, numpy
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='This script parses amber files to extract the total energy. You can also use it to create plots.')
parser.add_argument('path',help='The filepath to the file to be analyzed')
args = parser.parse_args()

md_file = args.path
outfile = open(md_file,'r')
md_data = outfile.readlines()
outfile.close()
filename = md_file.split('.')[-2]
etot_energy = []
etot_file = open(F'{filename}_Etot.txt','w+')
for line in md_data:
    if 'Etot' in line:
        etot_line = line
        etot_energy.append(etot_line.split()[2])
etot_energy = etot_energy[:-2]
etot_energy = numpy.array(etot_energy).astype(numpy.float)
for i in etot_energy:
    etot_file.write(F'{i}\n')
etot_file.close()

plt.figure()
plt.xlabel('Simulation cycles')
plt.ylabel('Total energy (kcal/mol)')
plt.plot(etot_energy,label=filename)
plt.legend()
plt.savefig(F'{filename}.png',dpi=300)