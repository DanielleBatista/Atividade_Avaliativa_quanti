import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros
p = 0.40
n = 100
erro_padrao_p = np.sqrt(p * (1 - p) / n)

# Gerando uma distribuição amostral de p
x = np.linspace(0, 1, 1000)
y = norm.pdf(x, p, erro_padrao_p)

# Plotando a distribuição
plt.plot(x, y, label=r'$\hat{p} \sim N(0.40, 0.049)$')
plt.fill_between(x, y, alpha=0.2)
plt.title("Distribuição Amostral de p")
plt.xlabel("Proporção Amostral (p̂)")
plt.ylabel("Densidade de Probabilidade")
plt.legend()
plt.grid(True)
plt.show()

