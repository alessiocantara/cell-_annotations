import requests
from bioservices import UniProt
import json


def search_uniprot(organism_name, organelle, filename):
    service = UniProt()
    queries = f'organism_name:"{organism_name}" AND organelle:"{organelle}"'
    result = service.search(queries)

    # Extract column names and data
    rows = result.split('\n')
    columns = rows[0].split('\t')
    data = [row.split('\t') for row in rows[1:]]

    # Convert data to list of dictionaries
    results_list = []
    for row in data:
        result_dict = {}
        for i in range(len(columns)):
            result_dict[columns[i]] = row[i]
        results_list.append(result_dict)

    # Write results to JSON file
    with open(filename, 'w') as f:
        json.dump(results_list, f)

search_uniprot("Mus Musculus", "Mitochondrion", "mito_mouse_uniprot.json")