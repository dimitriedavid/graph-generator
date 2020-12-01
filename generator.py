import random
import numpy as np
import sys
from tqdm import tqdm

output_dir = 'in/'
max_cost = 10000

if (sys.argv[1] == "quiet"):
    nr_noduri = int(input())
    procent_muchii = float(input())
    muchii_negative = input()
    file_name = input()
else:
    nr_noduri = int(input("Nr noduri [2, 10^5]: "))
    procent_muchii = float(input("Procent din graf complet %: "))
    muchii_negative = input("Muchii negative in graf y/n: ")
    file_name = input("Nume fisier iesire: ")

nr_muchii_max = nr_noduri * (nr_noduri - 1)
nr_muchii = int(float(procent_muchii) / 100 * nr_muchii_max)

if (nr_muchii > 1e6):
    nr_muchii = int(1e6)


print("Generating: " + file_name)
print("=> Numar muchii:", nr_muchii)


f = open(output_dir + file_name, "w")

f.write(str(nr_noduri) + " " + str(nr_muchii) + "\n")

maxed_sources = []
source_dest_map = {}

for i in tqdm(range(nr_muchii)):

    # select a source that has available destinations
    source = random.randint(1, nr_noduri)
    while source in maxed_sources:
        source = random.randint(1, nr_noduri)

    # get list of already used destinations for this source
    if source not in source_dest_map:
        source_dest_map[source] = []
    used_destinations = source_dest_map[source]

    # get destination
    dest = random.randint(1, nr_noduri)
    while dest == source or dest in used_destinations:
        dest = random.randint(1, nr_noduri)

    # add source dest pair to map
    used_destinations.append(dest)

    # check if source is maxed
    if len(used_destinations) == (nr_noduri - 1):
        maxed_sources.append(source)

    cost = int((np.random.normal(0, 2, 1)) * 100)

    if (muchii_negative == 'n'):
        cost = abs(cost)

    f.write(str(source) + ' ' + str(dest) + ' ' + str(cost) + '\n')
