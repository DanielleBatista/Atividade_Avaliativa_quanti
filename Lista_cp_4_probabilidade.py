###Probabilidade é uma medida numérica da possibilidade de um evento ocorrer. 
# Desse modo,podemos usar probabilidades como medidas do grau de incerteza associado aos quatro eventos anteriormente relacionados. 
# Se houver probabilidades disponíveis, podemos determinar a possibilidade de cada um dos eventos ocorrer.

##Resolução de Exercício

#A tabela a seguir mostra a porcentagem de chegadas de voos no horário, o número de relatos de extravio de bagagem por 1.000 passageiros 
# e o número de reclamações de clientes por 1.000 passageiros para 10 companhias aéreas (site da Forbes, fevereiro de 2014).

##(a)Se você escolher aleatoriamente um voo da Delta Air Lines, qual é a probabilidade de que esse voo individual chegue no horário?
#Dados:
# Dicionário com os dados de pontualidade (%)
pontualidade = {
    "Virgin America": 83.5,
    "JetBlue": 79.1,
    "AirTran Airways": 87.1,
    "Delta Air Lines": 86.5,
    "Alaska Airlines": 87.5,
    "Frontier Airlines": 77.9,
    "Southwest Airlines": 83.1,
    "US Airways": 85.9,
    "American Airlines": 76.9,
    "United Airlines": 77.4
}
# Mostrar a probabilidade de um voo da Delta chegar no horário##
companhia = "Delta Air Lines"
probabilidade = pontualidade[companhia] / 100  # Convertendo de % para proporção

print(f"{probabilidade:.4f}")##Com quatro numeros da virgula##

#(b) Se você escolher aleatoriamente uma das 10 companhias aéreas para um estudo de acompanhamento sobre as classificações de qualidade deste setor, 
# qual é a probabilidade de escolher uma companhia aérea com menos de dois relatórios de bagagem extraviada por 1.000 passageiros?
# Lista com os dados de extravio de bagagem

extravio = [0.87, 1.88, 1.58, 2.10, 2.93, 2.22, 3.08, 2.14, 2.92, 3.87]

# Contar quantas companhias têm menos de 2 extravios
quantidade_menor_que_2 = sum(1 for x in extravio if x < 2) #for x in extravio: percorre cada valor da lista extravio, um por um. 
                                                           #if x < 2: verifica se aquele valor (número de extravios) é menor que 2. #
                                                           # 1 for x in extravio if x < 2: gera um 1 cada vez que a condição for verdadeira.

# Calcular a probabilidade
total_companhias = len(extravio)
probabilidade = quantidade_menor_que_2 / total_companhias

# Exibir resultado
print(f"{quantidade_menor_que_2} companhias têm menos de 2 extravios por 1.000 passageiros.")
print(f"Probabilidade: {probabilidade:.4f}")

#(c)Se você escolher aleatoriamente 1 das 10 companhias aéreas para um estudo de acompanhamento sobre as classificações de qualidade deste setor, 
# qual é a probabilidade de escolher uma companhia aérea com mais de uma reclamação de cliente por 1.000 passageiros?

reclamacao = [1.50, 0.79, 0.91, 0.73, 0.51, 1.05, 0.25, 1.74, 1.80, 4.24]
quantidade_maior_que_1 = sum(1 for x in reclamacao if x > 1)

#Calcular a probablidade #Contar quantas companhias têm mais de 1 reclamação
total_companhias = len(reclamacao)
probabilidade = quantidade_maior_que_1 / total_companhias

#Exibir resultado
print(f"{quantidade_maior_que_1} companhias têm mais de 1 reclamacao por 1.000 passageiros.")
print(f"Probabilidade: {probabilidade: .4f}")

# (d) Qual é a probabilidade de um voo da AirTran Airways selecionado aleatoriamente não chegar no horário?
# Probabilidade de chegar no horário
chegada_no_horario = 0.871

# Cálculo da probabilidade de NÃO chegar no horário
nao_chegar_no_horario = 1 - chegada_no_horario

# Exibir resultado
# Probabilidade de chegar no horário
chegada_no_horario = 0.871

# Cálculo da probabilidade de NÃO chegar no horário
nao_chegar_no_horario = 1 - chegada_no_horario

# Exibir resultado
print(f"Probabilidade de não chegar no horário: {nao_chegar_no_horario:.4f}")
print(f"Probabilidade de não chegar no horário: {nao_chegar_no_horario:.2%}")

# 20. A Junior Achievement USA e a Fundação Allstate entrevistaram adolescentes de 14 a 18 anos 
# e perguntaram em que idade eles pensam que se tornarão financeiramente independentes (USA Today, 30 de abril de 2012). 
 #As respostas de 944 adolescentes a esta pergunta são as seguintes.
 #Considere o experimento de selecionar aleatoriamente um adolescente de sua respectiva população com idade de 14 a 18 anos.
  
 #(a) Calcule a probabilidade de ser financeiramente independente para cada uma das quatro categorias de idade. 
 
 # Total de respostas
total = 944     ##Número de participantes

# Dicionário com os dados da idades com numero de respostas que vai percorrer cada item do dicionário respostas.
respostas = {
    "16 a 20": 191,
    "21 a 24": 467,
    "25 a 27": 244,
    "28 ou mais": 42
}

# Calcular e imprimir as probabilidades 
for faixa, qtd in respostas.items(): #Inicio do loop, "faixa" idade
    prob = qtd / total
    print(f"Faixa {faixa}: {prob:.4f} ({prob:.2%})")

# (b). Qual é a probabilidade de ser financeiramente independente antes dos 25 anos? 

### total
total = 944

#Soma dos valores antes de 25 anos
antes_25 = 191 + 467 #16 a 20 + 21 +24

#Calcular a probabilidade 
prob_antes_25 = antes_25 / total

#Exibir resultado
print(f"Probabilidade de independência financeira antes dos 25 anos: {prob_antes_25:.4f} ({prob_antes_25:.2%})")

# (c). Qual é a probabilidade de ser financeiramente independente após os 24 anos? 
##total
total = 944

#Soma dos valores após dos 24 anos
apos_24 = 244 + 42

#Calcular a probabilidade
prob_apos_24 = apos_24 / total

#Exibir resultado
print(f"Probabildiade de independência financeira após os 24 anos: {prob_apos_24: .4f} ({prob_apos_24: .2%})")

# (d). As probabilidades sugerem que os adolescentes podem ser um pouco irrealistas em suas expectativas sobre quando se tornarão financeiramente independentes?
#A probabilidade de ser financeiramente independente antes dos 25 anos, 0,6970, parece alta, dadas as condições econômicas gerais. Parece que os adolescentes que res-ponderam 
# a esta pesquisa podem ter expectativas irrealistas sobre se tornarem financeiramente independentes em uma idade relativamente jovem.

# Questão 28 ##Lei da adição
##A lei da adição é útil quando estamos interessados em saber qual é a probabilidade de pelo menos um de dois eventos ocorrer. Ou seja, com os eventos A e B, estamos interessados em saber 
#qual é a probabilidade de ocorrência do evento A ou do evento B, ou de ambos.

#Uma pesquisa com assinantes de revistas mostrou que 45,8% haviam alugado um carro nos últimos 12 meses por razões comerciais, 
# 54% alugaram um carro durante os últimos 12 meses por razões pessoais e 
# 30% alugaram um carro nos últimos 12 meses por razões tanto comerciais quanto pessoais.

#(a).Qual é a probabilidade de um assinante ter alugado um carro durante os últimos 12 meses por razões comerciais ou pessoais? 
# Probabilidades
comercial = 0.458
pessoal = 0.54
ambos = 0.30

# União: comercial OU pessoal
prob_ou = comercial + pessoal - ambos

# Exibir resultado
print(f"Probabilidade de ter alugado por razões comerciais OU pessoais: {prob_ou:.4f} ({prob_ou:.2%})")

#(b).Qual é a probabilidade de um assinante não ter alugado um carro durante os últimos 12 meses por razões comerciais ou por razões pessoais?

# Probabilidade de comercial OU pessoal (já calculada antes)
prob_ou = 0.698

# Complemento
prob_nao_alugou = 1 - prob_ou

# Exibir
print(f"Probabilidade de NÃO ter alugado por nenhum motivo: {prob_nao_alugou:.4f} ({prob_nao_alugou:.2%})")

##Questão 33
##Estudantes que fizeram o Teste de Admissão de Graduação em Administração (GMAT, na sigla em inglês) foram questionados sobre o curso de graduação 
# e a intenção de cursar o MBA como estudantes em tempo integral ou parcial. A seguir, um resumo de suas respostas.

#(a).Desenvolva uma tabela de probabilidades conjuntas para esses dados. 

import pandas as pd

#Criar tabela com os dados
dados = {
    "Integral": [353, 197, 251], 
    "Meio período": [150, 161, 194]
}

index = ["Administração" , "Engenharia" , "Outros"] #Definição dos rótulos das linhas da tabela (índice): as áreas de formação dos alunos.

df= pd.DataFrame(dados, index = index) ##Transformar dados em tabela
df["Total"] = df.sum(axis = 1) #Aqui calculamos a soma horizontal de cada linha (Integral + Meio período) e cria uma nova coluna chamada "Total"
df.loc["Total"] = df.sum()   #Soma as colunas (soma vertical) para adicionar a última linha com os totais de cada coluna

##Calcular tabela de probabilidade conjunta
prob_df = df / df.loc["Total" , "Total"]   #Dividir o total pelo total geral

print(prob_df. round (4))

#(b)Use as probabilidades marginais correspondentes ao setor de graduação (Administração, Engenharia, outros) para comentar sobre qual desses setores produz o maior potencial de estudantes de MBA.
import pandas as pd
import matplotlib.pyplot as plt

# 1. Dados brutos (frequência absoluta)
dados = {
    "Integral": [352, 197, 251],
    "Meio período": [150, 161, 194]
}
index = ["Administração", "Engenharia", "Outros"]

# 2. Criar o DataFrame
df = pd.DataFrame(dados, index=index)

# 3. Calcular totais e total geral
df["Total"] = df.sum(axis=1)
total_geral = df["Total"].sum()

# 4. Calcular as probabilidades marginais por setor de graduação
prob_marginais = df["Total"] / total_geral

# 5. Exibir as probabilidades marginais
print("Probabilidades marginais por setor de graduação:")
print(prob_marginais.round(4))

# 6. Gráfico de barras
plt.figure(figsize=(8, 5))
bars = plt.bar(prob_marginais.index, prob_marginais.values, color=["#1f77b4", "#ff7f0e", "#2ca02c"])
plt.title("Potencial de estudantes de MBA por setor de graduação", fontsize=14)
plt.ylabel("Probabilidade marginal")
plt.ylim(0, 0.5)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionar rótulos de valor nas barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.01,
             f'{height:.2%}', ha='center', fontsize=10)

plt.tight_layout()
plt.show()

#(C). Se o estudante pretende frequentar aulas em período integral de um curso de MBA, qual é a probabilidade de que ele seja um graduado em Engenharia?

##Dados
engenharia_integral = 197
total_integral = 800

##Probabilidade Condicional
prob_condicional = engenharia_integral / total_integral

# Exibir resultado
print(f"Probabilidade de ser de Engenharia dado que é Integral: {prob_condicional:.4f} ({prob_condicional:.2%})")

## (d). Se o estudante for graduado no setor de Administração, qual é a probabilidade de que ele pretenda frequentar aulas em tempo integral para conseguir um MBA?
##Dados
adm_integral = 352
total_integral = 800

#Probabilidade Condicional
prob_condicional = adm_integral / total_integral

#Exibir resultado
print(f"Probabilidade de ser Administração dado que é Integral: {prob_condicional: .4f} ({prob_condicional: .2%})")


#(e). Admitamos que A denote o evento de que o estudante pretende frequentar aulas em tempo integral para conseguir um diploma em MBA, e que B denote 
#o evento de o estudante ser um graduado no setor de Administração. Os eventos A e B são independentes? Justifique sua resposta.

# Dados da tabela
total_geral = 1305
admin_integral = 352
total_integral = 800
total_admin = 502

# Probabilidades
p_a = total_integral / total_geral             # P(A): probabilidade de Integral
p_b = total_admin / total_geral                # P(B): probabilidade de Administração
p_a_inter_b = admin_integral / total_geral     # P(A ∩ B): Integral e Administração
p_a_mul_b = p_a * p_b                          # P(A) * P(B)

# Verificação da independência
print(f"P(A) = {p_a:.4f}")
print(f"P(B) = {p_b:.4f}")
print(f"P(A ∩ B) = {p_a_inter_b:.4f}")
print(f"P(A) * P(B) = {p_a_mul_b:.4f}")

# Comparação
if round(p_a_inter_b, 4) == round(p_a_mul_b, 4):
    print("✅ Os eventos A e B são independentes.")
else:
    print("❌ Os eventos A e B NÃO são independentes.")


#Questão 38- O Institute for Higher Education Policy, uma empresa de pesquisa sediada em Washington, 
# estudou o pagamento de empréstimos estudantis de 1,8 milhão de universitários 
# cujo empréstimos começaram a ser pagos seis anos antes (The Wall Street Journal, 27 de novembro de 2012). 
# O estudo descobriu que 50% dos empréstimos estudantis estavam sendo pagos de forma satisfatória, enquanto os outros 50% estavam inadimplentes. 
# A tabela de probabilidades conjuntas a seguir mostra as probabilidades do status de empréstimo estudantil e se o estudante conseguiu se formar ou não.

#(a).Qual é a probabilidade de um aluno que fez empréstimo estudantil ter recebido um diploma universitário?

import pandas as pd

# Criando a tabela de probabilidades conjuntas
dados = {
    "Satisfatório": [0.26, 0.24],
    "Inadimplente": [0.16, 0.34]
}
index = ["Diploma: Sim", "Diploma: Não"]

# Criar o DataFrame
df = pd.DataFrame(dados, index=index)

# Adicionar total por linha e coluna
df["Total"] = df.sum(axis=1)
df.loc["Total"] = df.sum()

# Exibir a tabela
print("Tabela de Probabilidades Conjuntas:")
print(df)

# Calcular a probabilidade de um aluno ter recebido diploma universitário
prob_diploma_sim = df.loc["Diploma: Sim", "Total"]
print(f"\nProbabilidade de ter diploma universitário: {prob_diploma_sim:.2f} ou {prob_diploma_sim:.0%}")

# (b). Qual é a probabilidade de um aluno que fez empréstimo estudantil não ter recebido um diploma universitário?

import pandas as pd

# Criando a tabela de probabilidades conjuntas
dados = {
    "Satisfatório": [0.26, 0.24],
    "Inadimplente": [0.16, 0.34]
}
index = ["Diploma: Sim", "Diploma: Não"]

# Criar o DataFrame
df = pd.DataFrame(dados, index=index)

# Adicionar total por linha e coluna
df["Total"] = df.sum(axis=1)
df.loc["Total"] = df.sum()

# Exibir a tabela
print("Tabela de Probabilidades Conjuntas:")
print(df)

#Calcular a probabilidade que fez emprestimos e não pegou diploma
prob_diploma_não = df.loc["Diploma: Não", "Total"]
print(f"\nProbabilidade que fez emprestimo e não pegou diploma universitário: {prob_diploma_não:.2f} ou {prob_diploma_não:.0%}")

#(c). Considerando que o aluno recebeu seu diploma universitário, qual é a probabilidade de este aluno ter um empréstimo inadimplente? 
#
# Alunos com diploma e inadimplente## p_inadimplente_graduado
p_inadimplente_graduado = 0.16
total_diploma = 0.42

#Probabilidade Condicional
p_diploma_inadimplente = p_inadimplente_graduado / total_diploma *100

print(f"A probabilidade ser inadimplente e diplomado {p_diploma_inadimplente: .2f}%")

#(d).Considerando que o aluno não recebeu seu diploma universitário, qual é a probabilidade de o aluno ter um empréstimo inadimplente?

p_inadimplente_nao_graduado = 0.34
total_nao_diploma = 0.58

#Probabilidade Condicional
p_nao_diploma_inadimplente = p_inadimplente_nao_graduado / total_nao_diploma *100

print(f"A probabilidade do aluno que não recebeu o diploma e ser inadimplente {p_nao_diploma_inadimplente: .2f}%")

#(e).Qual é o impacto de abandonar a faculdade sem um diploma para alunos que têm um empréstimo estudantil?

#Dados
#Alunos com diploma e inadimplente## p_inadimplente_graduado
p_inadimplente_graduado = 0.16
total_diploma = 0.42

#Dados
p_inadimplente_nao_graduado = 0.34
total_nao_diploma = 0.58

#Probabilidade Condicional
p_diploma_inadimplente = (p_inadimplente_graduado / total_diploma) * 100
p_nao_diploma_inadimplente = (p_inadimplente_nao_graduado / total_nao_diploma) *100

impacto_abanono = p_nao_diploma_inadimplente - p_diploma_inadimplente
#Diferença
aumento = (impacto_abanono / p_diploma_inadimplente) * 100

print(f"Qual é o impacto de abandonar a faculdade sem um diploma para alunos que têm um empréstimo estudantil {aumento: .2f} %")

#Resultado 
#Alunos que não concluem a faculdade têm uma chance significativamente maior de ficarem inadimplentes com o empréstimo estudantil. 
# Isso sugere que a conclusão do curso tem um papel protetor importante na capacidade 
# de manter o pagamento dos empréstimos em dia — possivelmente porque quem se forma tem melhores oportunidades de emprego e renda.

#Questão 42 - 
# Um banco local fez uma revisão de sua política de cartões de crédito com a intenção de cancelar alguns contratos destes cartões. No passado, aproximadamente 5% dos detentores de cartões de crédito se tornaram inadimplentes, deixando o banco incapaz de cobrar o saldo devedor. 
# Portanto, a gerência estabeleceu uma probabilidade a priori de 0,05 de que qualquer portador de cartão de crédito em particular se tornará inadimplente. O banco também desco-briu que a probabilidade de os clientes que não são inadimplentes deixarem de efetuar um pagamento mensal é de 0,20. 
# Naturalmente, a probabilidade de os inadimplentes deixarem de efetuar um pagamento mensal é de 1.

# (a). Dado que o cliente tenha deixado de efetuar um ou mais pagamentos mensais, calcule a probabilidade a posteriori de que ele se torne inadimplente.
#Dados
p_inadimplente = 0.05
p_nao_inadimplente = 0.95

p_pagamento_dado_inadimplente = 1.0
p_pagamento_dado_nao_inadimplente = 0.20

#Probabilidade total de não pagamento
p_pagamento = (p_pagamento_dado_inadimplente * p_inadimplente) + \
              (p_pagamento_dado_nao_inadimplente * p_nao_inadimplente)

# Probabilidade a posteriori com Bayes
p_inadimplete_dado_pagamento = (p_pagamento_dado_inadimplente * p_inadimplente) / p_pagamento
print(f"Probabilidade de inadimplencia dado quue não pagou: {p_inadimplete_dado_pagamento * 100: .2f} %")

# (b). O banco gostaria de cancelar o cartão de crédito se a probabilidade de um cliente se tornar inadimplente for maior que 0,20. 
# O banco deveria cancelar o cartão se o cliente deixar de efetuar um pagamento mensal? Sim ou não? Por quê?

#Resposta
#Como a probabilidade real ultrapassa o limite estabelecido pela política do banco (ainda que por pouco), o critério para cancelamento é atendido.
#Portanto, sim, o banco deveria cancelar o cartão de crédito do cliente se ele deixou de efetuar um pagamento mensal.


