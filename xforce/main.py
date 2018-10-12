import requests
from bin import config
from requests.auth import HTTPBasicAuth
import argparse

parser = argparse.ArgumentParser(
    description='This utility sends a GET request to api.xforce.ibmcloud.com with an entered IP and returns the output to the terminal.'
)

# Required arguments
required = parser.add_argument_group('required arguments')
required.add_argument("-i", "--ip", help="query a single IP address.", action="store", type=str, required=True)
required.add_argument("-n", "--new", help="Latest submission.", action="store_true", required=False)

args = parser.parse_args()

req = requests.get(f'{config.url_ip}{args.ip}', auth=HTTPBasicAuth(config.api_key, config.api_pw))
content = req.json()

# Error handling - No records #

if content['history'] == [] and content['subnets'] == [] and content['cats'] == {}:
    print(f"No Records found for {args.ip}")

# Display latest submission #

if args.new == True:
    print(('-' * 50), "\n" + f"Submission Date: {content['history'][-1]['created']}")
    print(f"Location: {content['history'][-1]['geo']['country']}, {content['history'][-1]['geo']['countrycode']}")
    print(f"Subnet: {content['history'][-1]['ip']}")
    print(f"Reason: {content['history'][-1]['reason']}")
    print(f"{content['history'][-1]['reasonDescription']}")
    print(f"Score: {content['history'][-1]['score']}")

    if content['history'][-1]['categoryDescriptions'] == {}:
        print('No Category Descriptions submitted')
    else:
        for i in content['history'][-1]['categoryDescriptions']:
            print(f"Categorie(s): {i}")
            print(f"{content['history'][-1]['categoryDescriptions'][i]}")
            
    try:
        for i in content['history'][-1]['asns']:
            print(f"ASN: {i}")
            print(f"Company: {content['history'][-1]['asns'][i]['Company']}")
            print(f"CIDR: {content['history'][-1]['asns'][i]['cidr']}")

    except (KeyError, IndexError):
        pass

# Display full results #

if args.new == False:
    for line in content['history']:
        print(('-' * 50), "\n" + f"Submission Date: {line['created']}")
        print(f"Location: {line['geo']['country']}, {line['geo']['countrycode']}")
        print(f"Subnet: {line['ip']}")
        print(f"Reason: {line['reason']}")
        print(f"{line['reasonDescription']}")
        print(f"Score: {line['score']}")

        if line['categoryDescriptions'] == {}:
            print('No Category Descriptions submitted')
        else:
            for i in line['categoryDescriptions']:
                    print(f"Categorie(s): {i}")
                    print(f"{line['categoryDescriptions'][i]}")
            
        try:
            for i in line['asns']:
                print(f"ASN: {i}")
                print(f"Company: {line['asns'][i]['Company']}")
                print(f"CIDR: {line['asns'][i]['cidr']}")

        except (KeyError, IndexError):
            continue
