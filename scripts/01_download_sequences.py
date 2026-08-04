"""
Script: 01_download_sequences.py

Layer:
Layer 2 → Sequence Retrieval

Purpose:
Retrieve canonical protein FASTA sequences from UniProt.

Input:
Gene name
Species

Output:
Protein FASTA files stored in data/raw/

Project:
Baking_Apoptosis
"""
# Biological Question:
# What are the canonical protein sequences of the core TRAIL signalling proteins across selected mammalian species?  

import os #allows python to work w folders and create if want to
import csv #to read csv files
import requests #to communicate w websites

csv_file = "data/metadata/proteins.csv"

with open(csv_file, "r") as file:
    reader = csv.DictReader(file) #python reads our csv 

    for row in reader:
        gene = row["Gene"]
        protein = row["Protein"]
        species = row["Species"]
        folder = row["Folder"]
        taxon = row["Taxon_ID"]
        query = row["UniProt_Query"]
        priority = row["Priority"]
        
        print("=" * 70)
        print(f"Processing {protein}")
        print(f"Gene      : {gene}")
        print(f"Species   : {species}")
        print(f"Taxon ID  : {taxon}")
        print(f"Folder    : {folder}")
        print(f"Priority  : {priority}")
        print("Preparing UniProt query...")


params = {
    "query": query,
    "format": "json"
}

response = requests.get(
    "https://rest.uniprot.org/uniprotkb/search",
    params=params
)
print("Status:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("Response length:", len(response.text))
print("First 300 characters:")
print(repr(response.text[:300]))
