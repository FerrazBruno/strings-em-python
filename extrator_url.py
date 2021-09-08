import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL esta vazia')

        padrao = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao.match(self.url)
        if not match:
            raise ValueError('A URL nao eh valida')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_de_busca):
        indice_parametro = self.get_url_parametros().find(parametro_de_busca)
        indice_valor = indice_parametro + len(parametro_de_busca) + 1
        e_comercial = self.get_url_parametros().find('&', indice_valor)
        if e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:e_comercial]

        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\nParametros: ' + self.get_url_parametros() + '\nURL base: ' + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url


dolar = 5.5
url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)
print(f'O tamanho da URL é: {len(extrator_url)}')
print(f'URL completa: {extrator_url}')
print(f'extrator_url == extrator_url_2? {extrator_url == extrator_url_2}')
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(f'Valor do parametro quantidade: {valor_quantidade}')

moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')

if moeda_origem == 'dolar' and moeda_destino == 'real':
    real = int(valor_quantidade) * dolar
    print(f'O valor em reais é: {real}')
elif moeda_origem == 'real' and moeda_destino == 'dolar':
    d = int(valor_quantidade) / dolar
    print(f'O valor em dolares é: {round(d, 2)}')
else:
    print('Cambio nao esta disponivel') 

