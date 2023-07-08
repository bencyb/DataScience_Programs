# Create a Plot

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

randomNumber=np.random.rand(10)
print("randomNumber = ",randomNumber)

# Output::randomNumber =  [0.72759672 0.53498589 0.75667667 0.07040575 0.86072475 0.20198641
 # 						  0.75263163 0.3444022  0.38372824 0.13681558]

style.use("ggplot")
plt.plot(randomNumber,'g',label='line one',linewidth=2)
plt.xlabel("Range")
plt.ylabel('Numbers')
plt.title('First Plot')
plt.legend()
plt.show()