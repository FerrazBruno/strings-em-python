url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'

indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:] # quantidade=100&moedaOrigem=real&moedaDestino=dolar

parametro_de_busca = 'quantidade'
indice_do_parametro = url_parametros.find(parametro_de_busca) # 0
indice_valor = indice_do_parametro + len(parametro_de_busca) + 1 # 11

indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
