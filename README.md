# ScrapeIt
IP reconnaissance tools.



### ipwhois.py - Quickly determine a best guess on IP origin
Designed to query ASN, Organization Name, and ISP and then print it to the console so it can be easily copy/imported into excel.

#### Directions
- Create a file called search_ips.txt.
- Paste a single IP address on each line without any CIDR - No IP ranges
- Run ipwhois.py in the same directory as search_ips.txt


Ex Input:

117.195.80.248

41.232.226.134

117.201.207.122

79.113.38.177


Ex Output:

117.195.80.248,India,AS9829,"Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore","National Internet Backbone"
41.232.226.134,Egypt,AS8452,"TE Data","Te-As"
117.201.207.122,India,AS9829,"Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore","National Internet Backbone"
79.113.38.177,Romania,AS8708,"RCS & RDS Business","Rcs & Rds Sa"
