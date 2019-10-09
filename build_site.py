import os
import os.path
import json 
import glob

source_path = "/Users/danledger/Dropbox/Shared/Dreammaker FX/Arduino Effect Sketches"
output_path = "/Users/danledger/Github/Dreammaker_FX/runjumplabs.github.io/dreammaker_fx/_effects/"



files = glob.glob(output_path+"*")
for f in files:

    print(f)
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

                
                line = "---\n"
                line = line + "layout: default\n"
                line = line + "name: "+effect['name']+"\n"
                line = line + "effect_type: "+effect['category']+"\n"
                if 'title' in effect:
                    line = line + "title: "+effect['title']+"\n"
                if 'creator' in effect:
                    line = line + "creator: "+effect['creator']+"\n"
                if 'description' in effect:
                    line = line + "description: "+effect['description']+"\n"
                if 'min_firmware' in effect:
                    line = line + "min_firmware: "+effect['min_firmware']+"\n"
                line = line + "---\n"

                line = line + "<h5>{{ page.title }} </h3>\n"
                line = line + "<ul>\n"
                line = line + "<li>Created by: {{page.creator}} </li>\n"
                line = line + "<li>Minimum firmware ver: {{page.min_firmware}} </li>\n"
                line = line + "<li>Description: {{page.description}} </li>\n"

                line = line + "</ul>\n"
                line = line + "<strong>Arduino sketch</strong>\n"
                line = line + "<pre><code class=\"cpp\" style=\"arduino\">"
                line = line + effect['ino_txt']
                line = line + "\n</code></pre>\n"

                output_file = output_path + effect['name'] + ".html"

                with open(output_file, "w") as text_file:
                    text_file.write(line)

                # print(line)

                #print os.path.join(subdir, file)

