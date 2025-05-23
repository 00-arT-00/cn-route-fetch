from urllib.request import urlretrieve

def fetch_file(url, filename):
    try:
        urlretrieve(url, filename)
        return True
    except:
        return False

def process_routes(filename, country="CN"):
    list = []
    route = []
    route6 = []
    length = 0
    try:
        with open(filename, "r") as delegated:
            for line in delegated:
                if line.startswith("apnic"):
                    list = line.split("|")
                    if list[1] == country and list[2] == "ipv4":
                        length = (24 - ((len(bin(int(list[4])))) - 11))
                        route.append(f"{list[3]}/{length}")
                    elif list[1] == country and list[2] == "ipv6":
                        route6.append(f"{list[3]}/{list[4]}")
            return (route, route6)
    except:
        return False
    
if __name__ == '__main__':
    fetch_file("https://ftp.apnic.net/stats/apnic/delegated-apnic-latest", "delegated-apnic-latest")
    if fetch_file:
        result = process_routes("delegated-apnic-latest")
        print(result[0])
        print(result[1])
    else:
        print("ERROR")