import csv

INPUT = "israel-alerts.csv"
OUTPUT = "karmiel-alerts.csv"

with open(INPUT, encoding="utf-8") as infile, open(OUTPUT, "w", encoding="utf-8", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header)

    for row in reader:
        if row[0] == "כרמיאל":
            writer.writerow(row)

print(f"Done. Karmiel alerts written to {OUTPUT}")
