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
ds1 = []
with open(file_path, mode='r', encoding='utf-8') as csv_file:
    reader1 = csv.reader(csv_file)
    for row in reader1:
        ds1.append(row)
dus=[]
for ia in totalElective:
    for ib in totalElective:
        if ia != ib and not [ib, ia] in dus:
            dus.append( [ia, ib])

#print(dus)

for ic in ds1:
    for ie in range(3):
        print((ie+1)%3)
        print(ic)
        if [ic[ie], ic[(ie+1)%3]] in dus:
            dus.remove[ic[ie], ic[(ie+1)%3]]
            pass
print(dus)
    