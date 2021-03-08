import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return t*(t>0)-(t-1)*(t>1)-(t-3)*(t>3)+(t-4)*(t>4)+2*(t>4)+(t-4)*(t>4)-(t-5)*(t>5)-(t-5)*(t>5)+(t-6)*(t>6)-2*(t>6)

t = np.linspace(-1, 7, 1000)
plt.figure()
plt.plot(t, f(t), '-b')
plt.title(f.__doc__)
plt.grid( linestyle=':')
plt.tight_layout()
plt.show()