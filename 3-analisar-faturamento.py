import json

def carregar_dados_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        return dados

def analisar_faturamento(dados):
    faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]
    if not faturamentos:
        return None, None, 0
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)
    dias_acima_media = len([f for f in faturamentos if f > media_faturamento])
    return menor_faturamento, maior_faturamento, dias_acima_media

def main():
    caminho_arquivo = 'faturamento.json'
    dados = carregar_dados_arquivo(caminho_arquivo)
    if not dados:
        return
    menor, maior, acima_media = analisar_faturamento(dados)
    if menor is not None:
        print(f"Menor valor de faturamento no mês: R$ {menor:.2f}")
        print(f"Maior valor de faturamento no mês: R$ {maior:.2f}")
        print(f"Número de dias com faturamento acima da média mensal: {acima_media}")

if __name__ == "__main__":
    main()
