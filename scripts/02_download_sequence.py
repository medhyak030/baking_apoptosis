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

#stage 1 of automation: Retrieving the accession number of the protein from uniprot using the gene name and species.
csv_file = "data/metadata/proteins.csv"
with open(csv_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        gene = row["Gene"]
        query_gene = row["Query_Gene"]
        protein = row["Protein"]
        species = row["Species"]
        taxon = row["Taxon_ID"]
        folder = row["Folder"]
        query = f"gene_exact:{query_gene} AND organism_id:{taxon}"
        print(gene, species)

        params = { #python to uniprot: search this protein return JSON
            "query": query,
            "format": "json"
        }
        response = requests.get(
            "https://rest.uniprot.org/uniprotkb/search",
            params=params
        )
        if response.status_code != 200: #cuz 200 is for ssuccess
            print(f"Failed to retrieve {gene}")
            continue

        data = response.json() #pyhton converts json to python dictionary
        results = data["results"]

        selected = None #candidate protein to download so this is literally the whole python dict for it

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

        # print("Reached after protein search")  printed the whole py dict so hid it
        # print("selected =", selected)

        if selected is None:
            print(f"No reviewed protein found for {species}")
            continue
        print("\nProtein selected successfully")
        print(f"Gene      : {gene}")
        print(f"Species   : {species}")
        print(f"Accession : {selected['primaryAccession']}")
        print(f"Entry     : {selected['entryType']}")
#till now we successfully retrieved the accession number of the protein. Now we will download the FASTA sequence using this accession number. 
#what we followed was reading csv file, teling python the query to search in uniprot, getting the response, checking if the response is successful, converting the response to python dictionary, iterating through the results and checking if the species and entry type match our criteria, and finally printing the accession number of the selected protein.

#stage 2 of automation: Downloading the FASTA sequence using the accession number.
        accession = selected["primaryAccession"]
        

        fasta_url = f"https://rest.uniprot.org/uniprotkb/{accession}.fasta" #the {} is an automated way to insert the accession number into the URL. This is called string formatting in Python. It allows us to create a URL that is specific to the protein we want to download. and takes up any accession number and returns the FASTA sequence for that protein. The .fasta at the end of the URL tells uniprot to return the sequence in FASTA format.
        fasta_response = requests.get(fasta_url)
        print("FASTA Status:", fasta_response.status_code) #gets the status of the request. 200 means success, 404 means not found, etc.
        #print(fasta_response.text[:200]) #used text cuz we want plain text response. and we are printing the first 200 characters of the response to check if we got the correct sequence.
 #stage 3 of automation: Saving the FASTA sequence to a file.
        if fasta_response.status_code != 200:
            print(f"Failed to download FASTA for {gene}")
            continue
        output_dir = os.path.join("data", "raw", folder) #creates a path to the folder where we want to save the sequence. os.path.join is used to create a path that is compatible with the operating system we are using. This is important because different operating systems use different path separators (e.g., / for Linux and \ for Windows).
        os.makedirs(output_dir, exist_ok=True) #creates the folder if it doesn't exist. exist_ok=True means that if the folder already exists, don't raise an error.
        output_file = os.path.join(output_dir, f"{gene}.fasta") #creates
        with open(output_file, "w") as fasta_file: #opens the file in write mode. if the file doesn't exist, it will be created. if it does exist, it will be overwritten.
            fasta_file.write(fasta_response.text) #writes the sequence to the file.
        print(f"Saved: {output_file}")