"""
Not a very nice looking  has a future though
once I get a bit more time.

idea is to feed a list of ip's
ouput is a comma seperated file of


-- to do:
   resolve empty space in ip file
   figure out what to do with load balance ip's
   build command line interface ...



blah.blah.org,127.0.0.1
"""

import socket

file_to_read = "ip_list.txt"
file_to_write = "mapped_ip_list.txt"

outfile = open(file_to_write, "w")

with open(file_to_read) as openfileobject:
    for line in openfileobject:
        line = line.rstrip()
        fqdn = socket.gethostbyaddr(line)
        print(fqdn)
        out_data = fqdn[0] + " , " + line
        outfile.write(out_data)
        # print(out_data)

outfile.close()
