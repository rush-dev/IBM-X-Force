# IBM-X-Force
IBM X-Force script to obtain IP reputation data.

# Requirements (Setup)

- Python 3.6+
- Requests
- API key from https://api.xforce.ibmcloud.com (free on account creation, simply change the api_key variable to your key in the config file before running)
- Argparse
```
pip install Requests
pip install argparse
```
## Usage
<b>For Full Page Results</b>
```
python main.py -i 8.8.8.8
python main.py --ip 8.8.8.8
```
<b>For the most recent submission:</b>
```
python main.py -i 8.8.8.8 -n
python main.py --ip 8.8.8.8 --new
```
# Troubleshooting
- If you are receiving errors, please look at the Issues queue and see if there is already an issue open.
- If you have a unique issue, please create a new Issue, and include the output of your terminal.
