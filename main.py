import pandas as pd
import matplotlib.pyplot as plt


class AnaliseVendas:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.df = None

    def carregar_dados(self):

        self.df = pd.read_csv(self.arquivo)

    def produtos_mais_vendidos(self):

        produtos_mais_vendidos = self.df.groupby('Produto')['Vendas'].sum().reset_index()


        produtos_mais_vendidos = produtos_mais_vendidos.sort_values(by='Vendas', ascending=False)


        return produtos_mais_vendidos

    def vendas_por_mes(self):
        # Extrair o mês e o ano de cada entrada de data
        self.df['Data'] = pd.to_datetime(self.df['Data'])
        self.df['Mes'] = self.df['Data'].dt.month
        self.df['Ano'] = self.df['Data'].dt.year


        vendas_por_mes = self.df.groupby(['Ano', 'Mes'])['Vendas'].sum().reset_index()


        return vendas_por_mes

    def plotar_grafico_vendas_mensais(self):
        # Calcular as vendas por mês
        vendas_por_mes = self.vendas_por_mes()


        plt.bar(vendas_por_mes['Mes'], vendas_por_mes['Vendas'])
        plt.xlabel('Mês')
        plt.ylabel('Vendas')
        plt.title('Vendas Mensais')
        plt.xticks(range(1, 13))
        plt.savefig('grafico_vendas_mensais.png')


analise = AnaliseVendas('vendas.csv')
analise.carregar_dados()

produtos_mais_vendidos = analise.produtos_mais_vendidos()
print("Produtos mais vendidos:")
print(produtos_mais_vendidos)

vendas_por_mes = analise.vendas_por_mes()
print("\nVendas por mês:")
print(vendas_por_mes)

analise.plotar_grafico_vendas_mensais()
