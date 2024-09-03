import json

def carregar_dados(dados):
    with open(dados, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

def analisar_faturamento(faturamento_diario):
    valores = [item['valor'] for item in faturamento_diario if item['valor'] > 0]

    if not valores:
        return None, None, 0

    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_media

def main():
    faturamento_diario = carregar_dados('dados.json')

    menor_valor, maior_valor, dias_acima_media = analisar_faturamento(faturamento_diario)

    print(f"Menor valor de faturamento: {menor_valor:.2f}")
    print(f"Maior valor de faturamento: {maior_valor:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

if __name__ == "__main__":
    main()
