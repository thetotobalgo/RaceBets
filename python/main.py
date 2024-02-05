import requests
from prettytable import PrettyTable

def fetch_data():
    url = "https://offline.turfinfo.api.pmu.fr/rest/client/7/programme/05012024/R1/C1/participants"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None

def print_data_as_table(data):
    headers = ['nom', 'numPmu', 'age', 'sexe', 'race', 'placeCorde', 'oeilleres', 'proprietaire', 'entraineur', 'driver', 'nombreCourses', 'nombreVictoires', 'nombrePlaces', 'gainsCarriere', 'handicapValeur', 'poidsConditionMonte']
    table = PrettyTable()
    table.field_names = headers
    
    for participant in data['participants']:
        row = [
            participant.get('nom'),
            participant.get('numPmu'),
            participant.get('age'),
            participant.get('sexe'),
            participant.get('race'),
            participant.get('placeCorde'),
            participant.get('oeilleres'),
            participant.get('proprietaire'),
            participant.get('entraineur'),
            participant.get('driver'),
            participant.get('nombreCourses'),
            participant.get('nombreVictoires'),
            participant.get('nombrePlaces'),
            participant.get('gainsParticipant', {}).get('gainsCarriere'),
            participant.get('handicapValeur'),
            participant.get('poidsConditionMonte'),
        ]
        table.add_row(row)
    
    print(table)

def main():
    data = fetch_data()
    if data:
        print_data_as_table(data)

if __name__ == "__main__":
    main()
