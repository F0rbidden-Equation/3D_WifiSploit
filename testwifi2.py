

import subprocess
cmd = ["nmcli -t -f ssid dev wifi"]
proc = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
for line in proc.stdout.readlines():
    #print(line)

    list2 = (line.decode('utf-8'))


