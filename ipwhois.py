#Quick IP Recon - Country, ASN, Org Name, IP Owner
#Can be used to quickly determine a best guess on IP origin
#Uses the IPWHOIS.app API - 50,000 queries a month (free tier)


import json
from urllib.request import urlopen

#Open file with IP Addresses.  Each IP on its own line. - no CIDR or IP ranges
search_ip_txt_file = open("search_ips.txt", "r")
#Read the file
ip_array_from_file = search_ip_txt_file.read()
#Create an array consisting of each IP
ip_array = ip_array_from_file.split("\n")
#Close file
search_ip_txt_file.close()

#Open the ipwhois.app URL with each ip.
#Download the json results for each ip
for i in ip_array:
    with urlopen("http://ipwhois.app/json/" + i) as response:
        source = response.read()

    data = json.loads(source)

    #pull values from the json keys and set to variables
    country_json = json.dumps(data['country'])
    ip_json = json.dumps(data['ip'])
    ip_asn = json.dumps(data['asn'])
    ip_org = json.dumps(data['org'])
    ip_isp = json.dumps(data['isp'])

    #strip double quotes from the strings from some variables
    #I commented out the strip from a couple others
    #I want to past this into excel for further analysis and sharing
    country = country_json.strip('"')
    ip = ip_json.strip('"')
    asn = ip_asn.strip('"')
    #org = ip_org.strip('"')
    #isp = ip_isp.strip('"')

    #print(ip,country,asn,org,isp)
    print(ip + "," + country + "," + asn + "," + ip_org + "," + ip_isp)
