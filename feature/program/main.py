import json
import argparse
import requests

def setup(argv):
    car = ''
    r = requests.get("https://gq67r.mocklab.io/escuela42/newspapers")

    if argv is None:
        parser = argparse.ArgumentParser(description="Example of commands", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument("-n", "--name", type=str, help="Get the information with the name specified")
        parser.add_argument("-t", "--type", type=str, help="Get the list of newspapers of the specified type")
        parser.add_argument("-o", "--owner", type=str, help="Get the list of newspapers of the specified owner")
        args = parser.parse_args()
        config = vars(args)
    else:
        car = argv[1]
        string = argv.split("\"")[1]
        config = {}
        if car == 'n':
            config.update({'name': string})
        elif car == 't':
            config.update({'type': string})
        elif car == 'o':
            config.update({'owner': string})
    ret = loop(r, config)
    print(ret)
    return ret

def loop(r, config):

    # Variables
    values = ""
    result = {}

    # Loop code
    for i, j in config.items():
        if j is not None:
            values = i
    arr = r.json()
    for i in arr.values():
        for j in i.keys():
            if i[j] == config[values]:
                #print(i)
                result.update(i)
    return json.dumps(result)

if __name__ == "__main__":
    setup(None)