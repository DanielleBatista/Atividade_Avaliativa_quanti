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