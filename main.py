import csv
file_path = "./F4.csv"

totalElective = ["PHY"
,"CHEM"
,"BIO"
,"ECON"
,"CHIS"
,"ICT"
,"BAFS"
,"GEO"
,"CLIT"
,"HIST"
,"VA"] 

with open(file_path, mode='r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    pass