import codecs, json, sys

from proton3 import potentials
from proton3.audio import file_generator
from proton3.systems import one_dimensional
from proton3.systems import two_dimensional


# sys.argv[i] refers to the value sent from the nodejs process
energy_level = int(sys.argv[1])

free_particle = one_dimensional.free_particle().array[energy_level]

# path for json
file_path = "./data.json" 
# the array to .json output file
values = {'data' : free_particle.tolist()}
json.dump(values, codecs.open(file_path, 'w', encoding='utf-8'), 
          separators=(',', ':'), 
          sort_keys=True, 
          indent=4) 

# value of 'feedback' in order to trigger 
# the reading of JSON file 
print(energy_level)


