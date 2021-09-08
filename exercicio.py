texto = 'Bruno, Brasil, CPF: 111.222.333-44'

import re

padrao = re.compile('[0-9]{3}[.]{0,1}[0-9]{3}[.]{0,1}[0-9]{3}[-]{0,1}[0-9]{2}')
busca = padrao.search(texto)

if busca:
    cpf = busca.group()
    print(cpf)
