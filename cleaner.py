import json
import sys
import uuid
from jq import jq
import os

filename_input = sys.argv[1]
filename_temp = str(uuid.uuid4())
#filename_temp = 'kks'
filename_output = sys.argv[2]
file_write = open(filename_temp,"w")
with open(filename_input) as f:
    for num_line, line in enumerate(f):
        try:
            idea_alert = json.loads(line)
            j = jq('select([.Category[]  != "Test"] | all) |(.DetectTime|tostring) + "\t" + (.|tostring)').transform(idea_alert)
            #print(j)
            #file_write.write(json.dumps(j, ensure_ascii=False))
            file_write.write(j + "\n")
        except Exception as e:
            #if category == test or if json is invalid it provides error
            print(filename_input," error on line: ", num_line, e)

file_write.close()
cmd = "cat {} | sort | cut -f 2 > {}".format(filename_temp, filename_output)
print(cmd)
os.system(cmd)
os.remove(filename_temp)
