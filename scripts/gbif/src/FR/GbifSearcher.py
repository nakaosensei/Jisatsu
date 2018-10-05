import pandas as pd
import GbifRequests as gr

def run():
    df = pd.read_excel('ListaMacrofitas.xlsx' ,header=None)
    plants = df[0]
    gbifrequests = gr.GbifRequests()
    plantsOcurrences = {}
    for i in range(len(plants)):
        tmpId = gbifrequests.searchID(plants[i])
        ocurrences = gbifrequests.getOccurrencesFromSpecies(plants[i])
        plantsOcurrences[plant]=ocurrences

run()
