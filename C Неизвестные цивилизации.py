# Учёным априори известно, что любой представитель цивилизации
# связан с другим представителем этой же цивилизации через несколько
#«рукопожатий».

# Считаю, что рукопожатие включает обоих персон в одну цивилизацию

persons = []
with open('C persons.txt','r',encoding='utf-8') as file:
    for line in file:
        persons.append(line.strip())
#print(persons)
pairs = []
with open('C pairs.txt','r',encoding='utf-8') as file:
    for line in file:
        a,b = line.split(' - ')
        pairs.append((a.strip(),b.strip()))
#print(pairs)
res = []
while persons:
    x = persons.pop()
    res.append([x])
    #print(res)
    flg=1
    while flg:
        cnt=0
        for pair in pairs:
            for p in res[-1]:
                if p == pair[0] and pair[1] not in res[-1]:
                    #print(str(p)+' '+str(pair)+' '+str(pair[0]))
                    idx = persons.index(pair[1])
                    x = persons.pop(idx)
                    res[-1].append(x)
                    cnt += 1
                elif p == pair[1] and pair[0] not in res[-1]:
                    idx = persons.index(pair[0])
                    x = persons.pop(idx)
                    res[-1].append(x)
                    cnt += 1
        if cnt==0:
            flg=0
print(res)
print(len(res))
#11
