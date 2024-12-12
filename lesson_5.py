Урок 5 задание 1,2
def acos(x, y) :
    return x  / ((x * x + y * y) ** 0.5)
 
###################
# вариант 1 для трех точек
x1, x2 = map(float,input().split())
y1, y2 = map(float,input().split())
z1, z2 = map(float,input().split())
res = [x1, x2]
acosx = acos(x1, x2)
acosy = acos(y1, y2)
if acosy > acosx :
    acosx = acosy
    res = [y1, y2]
acosz = acos(z1, z2)
if acosz > acosx :
    acosz = acosz
    res = [z1, z2]
print(*res)
###########
# вариант 2 для "n" точек
n = 3
res = [tuple(map(float,input().split())) for i in range(n)]
rcos = [acos(*res[i]) for i in range(n)]
k = rcos.index(max(rcos))
print(res[k])
