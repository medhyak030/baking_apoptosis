import csv
import requests

input_file = "data/metadata/proteins.csv"
output_file = "data/processed/domain_annotations.csv"
with open(input_file, "r") as file, open(output_file, "w", newline="") as output:

    reader = csv.DictReader(file)

    writer = csv.writer(output)

    writer.writerow([
        "Gene",
        "Protein",
        "Species",
        "Taxon_ID",
        "Accession",
        "Feature",
        "Description",
        "Start",
        "End"
    ])
    
    for row in reader:

        gene = row["Gene"]
        protein_name = row["Protein"]
        species = row["Species"]
        taxon = row["Taxon_ID"]

        query = f"gene_exact:{gene} AND organism_id:{taxon}"
        params = {
            "query": query,
            "format": "json"
        }

        response = requests.get(
            "https://rest.uniprot.org/uniprotkb/search",
            params=params
        )
        if response.status_code != 200:
            print(f"Failed to retrieve {gene} - {species}")
            continue
        data = response.json()
        results = data["results"]

        selected = None

        for protein_data in results:

            organism = protein_data["organism"]["scientificName"]
            entry = protein_data["entryType"]

            if organism == species and "reviewed" in entry:
                selected = protein_data
                break

        if selected is None:
            print(f"No reviewed protein found for {gene} - {species}")
            continue

        features = selected["features"]

        print(f"\n{protein_name} - {species}")
        print(f"Accession: {selected['primaryAccession']}")
        print(f"Number of features: {len(features)}")

        for feature in features:

            feature_type = feature.get("type")
            description = feature.get("description")
            location = feature.get("location", {})

            if feature_type in [
                "Signal peptide",
                "Transmembrane",
                "Topological domain"
            ]:
                keep = True

            elif feature_type in ["Domain", "Region"]:
                keep = description is not None

            else:
                keep = False

            if not keep:
                continue

            start = location.get("start", {}).get("value")
            end = location.get("end", {}).get("value")
            print(f"{feature_type:20} {start:4} - {end:4}  {description}")
            writer.writerow([
                gene,
                protein_name,
                species,
                taxon,
                selected['primaryAccession'],
                feature_type,
                description,
                start,
                end
            ])