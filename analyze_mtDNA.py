import urllib.request
import csv
from collections import Counter

# Download human mitochondrial DNA
url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_012920.1&rettype=fasta&retmode=text"

response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")

# Clean DNA sequence
sequence = "".join(
    line.strip()
    for line in data.splitlines()
    if not line.startswith(">")
).upper()

cleaned_sequence = "".join(
    base for base in sequence if base in "ATGCN"
)

# Count nucleotides
counts = Counter(cleaned_sequence)

A = counts["A"]
T = counts["T"]
G = counts["G"]
C = counts["C"]

length = len(cleaned_sequence)

# Calculate GC and AT content
gc_content = ((G + C) / length) * 100
at_content = ((A + T) / length) * 100

# Display results
print("Human Mitochondrial DNA Analysis")
print("Accession: NC_012920.1")
print("Sequence Length:", length)
print("A:", A)
print("T:", T)
print("G:", G)
print("C:", C)
print("GC Content:", round(gc_content, 2), "%")
print("AT Content:", round(at_content, 2), "%")

# Save results
with open("analysis_results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Parameter", "Value"])
    writer.writerow(["Sequence Length", length])
    writer.writerow(["A", A])
    writer.writerow(["T", T])
    writer.writerow(["G", G])
    writer.writerow(["C", C])
    writer.writerow(["GC Content", round(gc_content, 2)])
    writer.writerow(["AT Content", round(at_content, 2)])

print("Analysis completed successfully!")
