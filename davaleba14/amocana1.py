import csv

with open("titanic.csv", "r") as titanic_csv:
    titanic_reader = csv.DictReader(titanic_csv)

    survived = [row for row in titanic_reader if row["Survived"] == "1"]
    print(survived)


with open("survived.csv", "w") as survived_csv:
    headers = ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin",
               "Embarked"]

    writer = csv.DictWriter(survived_csv, fieldnames=headers)
    writer.writeheader()
    writer.writerows(survived)
    