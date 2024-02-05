import csv

with open("organizations-100.csv", "r") as organizations_file:
    organizations_reader = csv.DictReader(organizations_file)

    employees_num = list(organizations_reader)
    sorted_employees = sorted(employees_num, key=lambda employee: employee["Number of employees"])

with open("sorted_csv.csv", "w") as sorted_csv:
    headers = ["Index", "Organization Id", "Name", "Website", "Country", "Description", "Founded", "Industry",
              "Number of employees"]

    writer = csv.DictWriter(sorted_csv, fieldnames=headers)
    writer.writeheader()
    writer.writerows(sorted_employees)
