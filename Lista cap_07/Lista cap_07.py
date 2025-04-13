#Qestão 15
#A National Football League (NFL) faz pesquisa com torcedores a fim de desenvolver uma classificação para cada jogo de futebol (site da NFL, 24 de outubro de 2012). Cada jogo é classificado em uma escala de 0 (sem importância) a 100 (memorável).
# As classificações dos fãs para uma amostra aleatória de 12 jogos estão a seguir. 

import numpy as np

notas = [57, 20, 61, 57, 86, 80, 74, 79, 72, 83, 73, 74]

media = np.mean(notas)
desvio_pop = np.std(notas)               # errado para esse caso
desvio_amostral = np.std(notas, ddof=1)  # correto

print(f"Média: {media:.2f}")
print(f"Desvio padrão populacional: {desvio_pop:.2f}")
print(f"Desvio padrão amostral: {desvio_amostral:.2f}")

#Questão 18 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros da distribuição amostral
mu = 200               # Média
sigma = 5              # Erro padrão (desvio padrão da média amostral)

# Criar intervalo de valores para o eixo x
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Plotando a distribuição
plt.figure(figsize=(10, 5))
plt.plot(x, y, color='blue', label='Distribuição amostral de x̄')
plt.title('Distribuição amostral da média (x̄ ~ N(200, 5))')
plt.xlabel('Média amostral (x̄)')
plt.ylabel('Densidade de probabilidade')
plt.axvline(mu, color='red', linestyle='--', label='Média = 200')
plt.fill_between(x, y, where=(x >= mu - sigma) & (x <= mu + sigma), color='skyblue', alpha=0.5, label='±1 desvio padrão')
plt.legend()
plt.grid(True)
plt.show()

#Questão 19 Uma população tem uma média de 200 e um desvio padrão de 50. Suponha que uma amostra aleatória simples de tamanho 100 seja selecionada e x utilizada para estimar m. 
# a. Qual é a probabilidade de que a média amostral esteja dentro de ± 5 da média populacional? 
# b. Qual é a probabilidade de que a média amostral esteja dentro de ± 10 da média populacional?


from scipy.stats import norm

# Parâmetros
mu = 200
sigma = 50
n = 100
erro_padrao = sigma / (n**0.5)

# a. Probabilidade de estar dentro de ±5
prob_a = norm.cdf(5 / erro_padrao) - norm.cdf(-5 / erro_padrao)

# b. Probabilidade de estar dentro de ±10
prob_b = norm.cdf(10 / erro_padrao) - norm.cdf(-10 / erro_padrao)

print(f"a. Probabilidade (±5): {prob_a:.4f} ou {prob_a*100:.2f}%")
print(f"b. Probabilidade (±10): {prob_b:.4f} ou {prob_b*100:.2f}%")

from scipy.stats import norm
import numpy as np

# Califórnia
mu_ca = 22
sigma_ca = 4
n_ca = 30
erro_padrao_ca = sigma_ca / np.sqrt(n_ca)
z_ca = 1 / erro_padrao_ca
prob_ca = norm.cdf(z_ca) - norm.cdf(-z_ca)

# Nova York
mu_ny = 42
sigma_ny = 4
n_ny = 45
erro_padrao_ny = sigma_ny / np.sqrt(n_ny)
z_ny = 1 / erro_padrao_ny
prob_ny = norm.cdf(z_ny) - norm.cdf(-z_ny)

print(f"Califórnia: P(±1 in) = {prob_ca:.4f} ou {prob_ca*100:.2f}%")
print(f"Nova York:  P(±1 in) = {prob_ny:.4f} ou {prob_ny*100:.2f}%")


#Questão 28 O estado da Califórnia tem uma precipitação média anual de 22 polegadas, enquanto o estado de Nova York tem uma precipitação média anual de 42 polegadas (site da Current Results, 27 de outubro de 2012). Suponha que o desvio padrão para ambos os estados seja de 4 polegadas. Foi obtida uma amostra de 30 anos de índices pluviométricos para a Califórnia e uma amostra de 45 anos de índices pluviométricos para Nova York. 
#a. Mostre a distribuição de probabilidade da precipitação média anual da amostra para a Califórnia.
 ##b. Qual é a probabilidade de que a média amostral esteja dentro de 1 polegada da média populacional da Califórnia? 
#c. Qual é a probabilidade de que a média amostral esteja dentro de 1 polegada da média populacional de Nova York? 
#d. Em que caso, item (b) ou item (c), a probabilidade de obter uma média amostral dentro de 1 polegada da média populacional é maior? Por quê?


from scipy.stats import norm
import numpy as np

# Dados da Califórnia
mu_ca = 22              # média
sigma_ca = 4            # desvio padrão
n_ca = 30               # tamanho da amostra
erro_padrao_ca = sigma_ca / np.sqrt(n_ca)

# Probabilidade de estar dentro de 1 polegada da média
z_ca = 1 / erro_padrao_ca
prob_ca = norm.cdf(z_ca) - norm.cdf(-z_ca)

# Dados de Nova York
mu_ny = 42
sigma_ny = 4
n_ny = 45
erro_padrao_ny = sigma_ny / np.sqrt(n_ny)

z_ny = 1 / erro_padrao_ny
prob_ny = norm.cdf(z_ny) - norm.cdf(-z_ny)

# Resultados
print(f"Califórnia:")
print(f"  Erro padrão: {erro_padrao_ca:.4f}")
print(f"  Probabilidade de estar dentro de 1 in: {prob_ca:.4f} ou {prob_ca*100:.2f}%\n")

print(f"Nova York:")
print(f"  Erro padrão: {erro_padrao_ny:.4f}")
print(f"  Probabilidade de estar dentro de 1 in: {prob_ny:.4f} ou {prob_ny*100:.2f}%")

# Comparação
if prob_ca > prob_ny:
    print("\n🔍 A probabilidade é maior para a Califórnia.")
else:
    print("\n🔍 A probabilidade é maior para Nova York.")

 #Questão 31 Uma amostra aleatória simples de tamanho 100 é selecionada a partir de uma população com p = 0,40. 
 # a. Qual é o valor esperado de p? 
 # b. Qual é o erro padrão de p? 
 # c. Mostre a distribuição amostral de p.
 # d. O que a distribuição amostral de p mostra?
 
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

