"""
Import libraries

↓

Open retrieved_proteins.csv

↓

Read one row

↓

Get accession

↓

Download FASTA

↓

Save file
"""

import os #allows python to work w folders and create if want to
import csv #to read csv files
import requests #to communicate w websites

csv_file = "data/metadata/proteins.csv"
with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        gene = row["Gene"]
        protein = row["Protein"]
        species = row["Species"]
        taxon = row["Taxon_ID"]
        folder = row["Folder"]
        query = f"gene_exact:{gene} AND organism_id:{taxon}"
        print(gene, species)

        params = {
            "query": query,
            "format": "json"
        }
        response = requests.get(
            "https://rest.uniprot.org/uniprotkb/search",
            params=params
        )
        if response.status_code != 200:
            print(f"Failed to retrieve {gene}")
            continue

        data = response.json()
        results = data["results"]

        selected = None

        for protein_data in results:

            organism = protein_data["organism"]["scientificName"]
            entry = protein_data["entryType"]

            print("CSV species      :", repr(species))
            print("UniProt species  :", repr(organism))
            print("Entry type       :", entry)
            print("-" * 50)

            if organism == species and "reviewed" in entry:

                selected = protein_data

                break
            
            if selected is None:
                print(f"No reviewed protein found for {species}")
                continue
            print(selected["primaryAccession"])