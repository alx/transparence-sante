import glob

i = 0
out = open('data/merged.csv','w')
out.write("entreprise,type_beneficiaire,beneficiaire,date,nature,montant,x,x,code_postal_beneficaire\n")
for path in glob.glob('./raw/*.csv'):
    with open(path) as csv:
        for line in csv:
            out.write(line.strip()+","+path.split("/")[-1].split(".")[0]+"\n")
            i += 1
for path in glob.glob('./raw/INCOMPLETE/*.csv'):
    with open(path) as csv:
        for line in csv:
            out.write(line.strip()+","+path.split("/")[-1].split(".")[0]+"\n")
            i += 1
print(i)