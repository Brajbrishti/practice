dict={}
str ="Akshainie"
# print(len(str))
for i in str:
    dict[i]=dict.get(i,0)+1
for k,v in dict.items():
    print('key={}\t its occurrences={}'.format(k,v))