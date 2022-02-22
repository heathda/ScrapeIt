# ScrapeIt - IP Reconnaissance Tools



### ipwhois.py - Quickly determine a best guess on IP origin
Designed to query Country, ASN, Organization Name, and ISP and then print it to the console so it can be easily copy/imported into excel for further analysis/sharing/presentation.

##### Directions
- Create a file called search_ips.txt.
- Paste a single IP address on each line.  No CIDR. No IP ranges
- Run ipwhois.py in the same directory as search_ips.txt


Ex Input:

185.220.101.49  
41.232.226.134  
23.129.64.214  
79.113.38.177  


Ex Output:

185.220.101.49,Germany,AS60729,"Zwiebelfreunde e.V","Zwiebelfreunde e.V."  
41.232.226.134,Egypt,AS8452,"TE Data","Te-As"  
23.129.64.214,United States,AS396507,"Emerald Onion","Emerald Onion"  
79.113.38.177,Romania,AS8708,"RCS & RDS Business","Rcs & Rds Sa"  
