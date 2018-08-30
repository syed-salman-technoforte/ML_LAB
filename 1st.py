import csv
hypo = ['%','%', '%', '%', '%', '%','%']
with open("/home/weblab-sys-11/Desktop/nisarga.csv") as csv_file:
    readcsv=csv.reader(csv_file)
    print(readcsv)
    data=[]
    print("\n the given training examples are")
    for row in readcsv:
        print(row)
        if row[len(row)-1]=="yes":
            data.append(row)
print("examples are")
for x in data:
    print(x)
print("\n")
totalexample=len(data)
i=0
#j=0
k=0
print("the steps of s algo \n",hypo)
list=[]
p=0
d = len(data[p])-1
for j in range(d):
    list.append(data[i][j])
hypo=list
i=1
for i in range(totalexample):
    for k in range(d):      
        if hypo[k]!=data[i][k]:
            hypo[k]='?'
            k=k+1
        else:
            hypo[k]
    print(hypo)
i=i+1
print("\n MAXIMALLY SPECIFIC FIND S-hypothesis for given examples")
list=[]
for i in range(d):
    list.append(hypo[i])
print(list)
