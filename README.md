# CN Route Fetch

### Description:

This script generates sets of prefixes allocated to China from the APNIC database.

### How it works:

The script will try to download the latest delegated data from [https://ftp.apnic.net/stats/apnic/delegated-apnic-latest](https://ftp.apnic.net/stats/apnic/delegated-apnic-latest) and filter data matching these keywords: "CN" "ipv4" "ipv6"

### How to use:

Execute it with Python 3.6 or a higher version, and it will print lists containing CN routes.

### To-dos:

Add the ability to feed routes via the BGP protocol or store them in files with a specific format.