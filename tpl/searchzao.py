import requests


def search_tlp(name):
    downloadcsv = "&csv=true"
    name += downloadcsv
    down = requests.get(name)
    return down
