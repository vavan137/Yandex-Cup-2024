#Считаем, что на картинке не может быть шума.
#Напишите программу, которая найдёт квадратик в этом массиве,
#а затем выяснит, был ли он отмечен или нет.
#Толщина линий квадратика и крестика — 1 пкс.
#Крестик — это две прямые линии,
#которые соединяют противоположные углы квадрата.

w,h = map(int,input().split())
Pict = []
for i in range(h):
    Pict.append(input())
#
# найду теоретические границы квадратика
start = (-1,-1)
end = (0,0)
for j in range(h):
    for i in range(w):
        if Pict[j][i]=='1' and start==(-1,-1):
            start = (j,i) #самый верхний левый угол
        if Pict[j][i]=='1' and start!=(-1,-1):
            end = (j,i) #самый нижний правый угол

# проверю, что квадрат замкнут (и вне квадратика нет '1'?)
flg_bad = 0
for j in range(h):
    s = Pict[j]
    for i in range(w):
        if j == start[0]:
            if s[i] == '1' and i>end[1]:
                flg_bad += 1
            if s[i]=='0' and start[1]< i<= end[1]:
                flg_bad += 1
        elif j == end[0]:
            if i<start[1] and s[i] == '1':
                flg_bad += 1
            if s[i]=='0' and start[1]< i<= end[1]:
                flg_bad+=1
        elif start[0]<j<end[0]:
            if (i == start[1] or i == end[1]) and s[i] == '0':
                flg_bad += 1
        else:
            #здесь не должно быть единиц
            pass
if end[0]-start[0] != end[1]-start[1]:
    flg_bad+=1
#
flg_mark=1
if flg_bad==0:
    # квадрат есть. Ищем крестик.
    for k1 in range(0,end[0]-start[0]+1):
        s = Pict[start[0]+k1]
        #print(s)
        id1 = start[1] + k1
        id2 = end[1] - k1
        #print('id1='+str(id1)+' id2= '+str(id2))
        if s[id1]!='1' or s[id2]!='1':
            flg_mark -= 1

if flg_bad>0:
    print('Printing error')
else:
    if flg_mark==1:
        print('Marked')
    else:
        print('Not marked')

# здесь не проверяются квадраты,со стороной менее 5.
#В центре таких сплошная клякса, формально являющаяся пересечением диагоналей толщиной 1. 
