import os
import os.path
import json 
import glob

source_path = "/Users/danledger/Dropbox/Shared/Dreammaker FX/Arduino Effect Sketches"
output_path = "/Users/danledger/Github/Dreammaker_FX/runjumplabs.github.io/dreammaker_fx/_effects"



files = glob.glob(output_path)
for f in files:
    os.remove(f)

for subdir, dirs, files in os.walk(source_path):
    for file in files:
    	d = subdir.split('/')
    	if len(d) > 8:
    		effect = {}
    		effect['category'] = d[7]
    		#print(file)
    		if file.endswith(".ino"):
    			ino_file = os.path.join(subdir, file)
    			effect['name'] = file.replace(".ino","")
    			json_file = os.path.join(subdir, file.replace(".ino",".json")) 

    			if (os.path.exists(json_file)):
    				with open(json_file) as j:
    					data = json.load(j)
    					effect.update(data)
    				print("Found config file!")

    			with open(ino_file, 'r') as file:
    				effect['ino_txt'] = file.read()

    			print(effect)

    			#print os.path.join(subdir, file)