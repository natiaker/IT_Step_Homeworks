import csv

with open("organizations-100.csv", "r") as organizations_file:
    organizations_reader = csv.DictReader(organizations_file)

    secured_organizations = [row for row in organizations_reader if row["Website"][:5] == "https"]

    with open("ssl_companies.csv", "w") as ssl_companies:
        headers = ["Organization Id", "Name", "Website", "Industry", "Number of employees"]

        writer = csv.DictWriter(ssl_companies, fieldnames=headers)
        writer.writeheader()

        for row in secured_organizations:
            del row["Index"]
            del row["Country"]
            del row["Founded"]
            del row["Description"]
            writer.writerow(row)
