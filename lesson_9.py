from re import X
import numpy as np
import matplotlib.pyplot as plt

a=1
b=1

x = np.linspace(-2, 0, 2000)



plt.figure(figsize=(8, 6))




def f(x):
    return ((xb)-(ab))/x**b

plt.plot(x, f(x), color="black")

#plt.scatter(x, f(np.abs(x)), color="darkmagenta", s=1)

plt.xlabel("Frequency (cm$^{-1}$)")
plt.ylabel("f(x)")
plt.title("График функции с точкой разрыва второго рода")
plt.legend()
plt.grid(True)
plt.ylim(-10, 10)  

left, bottom, width, height = [0.55, 0.55, 0.35, 0.35]
ax2 = plt.gca().add_axes([left, bottom, width, height])
x_inset = np.linspace(-10, 0, 500)
ax2.plot(x_inset, f(x_inset, a, b), color='blue')
ax2.plot(x_inset, g(x_inset, a, b), color='red')
ax2.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
ax2.set_xlim(-10,0)



plt.show()

##############################################################################

import numpy as np
import matplotlib.pyplot as plt

def f(x, alpha, beta):
    return np.sqrt((alpha*x + beta)2 + 4 - x2)


x = np.linspace(-5, 5, 500) 


plt.figure(figsize=(12, 4))
plt.subplot(131)  
plt.plot(x, f(x,1,0.5), label='α=1, β=0.5')
plt.plot(x, f(x,1,-0.5), label='α=1, β=-0.5')
plt.plot(x, f(x,1,-1.5), label='α=1, β=-1.5')
plt.plot(x, f(x,1,0), 'b--', label='α=1, β=0') 
plt.plot(x, f(x,1,-1), 'r--', label='α=1, β=-1') 

plt.legend()
plt.title('График 1')
plt.xlabel('x')
plt.ylabel('y')



plt.subplot(132)  

plt.plot(x, f(x,1,0.5), label='α=1, β=0.5')
plt.plot(x, f(x,1,0.8), label='α=1, β=0.8')
plt.plot(x, f(x,1,0), 'b--', label='α=1, β=0') 
plt.plot(x, f(x,1,-1), 'r--', label='α=1, β=-1') 
plt.legend()
plt.title('График 2')
plt.xlabel('x')
plt.ylabel('y')



plt.subplot(133)  
plt.plot(x, f(x,1,-0.5), label='α=1, β=-0.5')
plt.plot(x, f(x,1,-0.8), label='α=1, β=-0.8')
plt.plot(x, f(x,1,-1.5), label='α=1, β=-1.5')
plt.plot(x, f(x,1,-2.5), label='α=1, β=-2.5')
plt.plot(x, f(x,1,0), 'b--', label='α=1, β=0') 
plt.plot(x, f(x,1,-1), 'r--', label='α=1, β=-1') 
plt.legend()
plt.title('График 3')
plt.xlabel('x')
plt.ylabel('y')

plt.tight_layout()
plt.show()
