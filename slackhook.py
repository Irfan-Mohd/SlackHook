import requests
import argparse
import os

def argument_parser():
    arg = argparse.ArgumentParser(description = "Slack Webhook URL Validator")
    arg.add_argument('-f','--file', help = 'Path to the input file', required = True)
    parse_arg = arg.parse_args()
    print("## checking file path")
    if (os.path.exists(parse_arg.file)):
        nfile = parse_arg.file
        process_file(nfile)
    else:
        print("Error Encountered while searching for file. Please check the file path")



def process_file(filename):
    with open(filename) as f:
        content = f.readlines()
        for lines in content:
            url = lines.strip()
            send_request(url)

            
def send_request(url):
    res = requests.post(url, data = '{"text" : "Hi There!"}')
    if (res.text == 'invalid_payload' or res.text == 'ok'):
        print("%s: is valid" % url )
    else:
        print("%s: is not valid" % url)


if __name__ == "__main__":
    argument_parser()