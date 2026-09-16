import csv



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



def gen(file):
    print(file + ":")

    stuElective = []
    combElective = []
    with open(file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            stuElective.append(row)


    for i in range(0, len(totalElective)):
        for j in range(i+1, len(totalElective)):
            combElective.append((totalElective[i], totalElective[j]))

    for i in range(len(stuElective)):
        for j in range(len(combElective)):
            if combElective[j][0] in stuElective[i] and combElective[j][1] in stuElective[i]:
                combElective[j] = "NA"


    for i in range(len(combElective)):
        if combElective[i] != "NA":
            print(combElective[i])
            

gen("F4.csv")
gen("F5.csv")
gen("F6.csv")