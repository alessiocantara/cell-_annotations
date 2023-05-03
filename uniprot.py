import requests
from bioservices import UniProt
import json


def search_uniprot(organism_name, organelle, filename):
    service = UniProt()
    queries = f'organism_name:"{organism_name}" AND organelle:"{organelle}"'
    result = service.search(queries)

    #extract columsn and rows
    rows = result.split('\n')
    columns = rows[0].split('\t')
    data = [row.split('\t') for row in rows[1:]]

    #convert to dicts
    results_list = []
    for row in data:
        result_dict = {}
        for i in range(len(columns)):
            result_dict[columns[i]] = row[i]
        results_list.append(result_dict)

    #write on json
    with open(filename, 'w') as f:
        json.dump(results_list, f)

search_uniprot("Mus Musculus", "Mitochondrion", "mito_mouse_uniprot.json")
