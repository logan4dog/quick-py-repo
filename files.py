# Open file 'textfiles.txt'
f = open('textfiles.txt')
# Create list to hold lines in file
h = list()
# Read each line of file into list h.
for line in f:
    h.append(line.split())

for item in h:
    field1 = item[4]+'\t'
    field2 = item[8]+'\t'
    field3 = item[5]+' '+item[6]+' '+item[7]
    if len(field1) < 15:
        print(len(field1))
    else:
        print(len(field1))

    print("{0} {1} {2} ".format(field1, field2, field3)
