def seq_check(s):
    tmp_chain = 0
    tmp_chain_len = 2
    for j in range(len(s)):
        if s[j]=='1':
            tmp_chain = 0
            tmp_chain_len += 1
        else:
            tmp_chain+=1
            if tmp_chain==tmp_chain_len:
                #cnt+=1
                return 1
    return 0
    
def generate_binary_seq(length,current = ''):
    if length==0:
        yield current
    else:
        yield from generate_binary_seq(length-1,current+'0')
        yield from generate_binary_seq(length-1,current+'1')
seq = list(generate_binary_seq(10))
# благоприятные исходы
cnt = 0 
for s in seq:
    cnt+=seq_check(s)
print(cnt)
print(cnt/1024)
# 410
# 0.400390625
# Это вероятность завершить испытание
#6. Если искателю удавалось завершить испытание, Зарифус отдавал Око Познания.
#Если же нет, то путник отправлялся на священную гору близь Аль-Джабра
#и дальше пытать своё счастье бросками монет.
# Ответ 0.4004
# если же игра может продолжаться бесконечно (формулировка п.6), то вероятность победы 1.0000

