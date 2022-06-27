import INFO

send_to = "62 GB Volume"
try:
    f = open(send_to)
    f.write(INFO.ssh_has)
    f.close()
except Exception as e:
    print(e)
    exit()
