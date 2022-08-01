import json

d1 = {
    "Pesso 1": {
        'nome': 'Antonio',
        'idade': 18,
    },

    "Pesso 2": {
        'nome': 'Allyson',
        'idade': 17,
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

print(d1_json)
