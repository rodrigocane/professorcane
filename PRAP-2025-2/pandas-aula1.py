import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'
drinks = pd.read_csv(url, keep_default_na=False, na_values=[''])
# print(drinks["country"]) #printando só o nome dos países
# print(drinks.iloc[30:,0:]) # selecionando da linha 30 em diante, todas as colunas
# print(drinks[drinks["continent"] == "SA"]) #filtro - selecionando linhas de países da América do Sul
# print(drinks[drinks["beer_servings"] == drinks["beer_servings"].min()]) #filtro - países que menos consomem cerveja e são mais tristes :(
# print(drinks["wine_servings"].describe()) #tudo q é estatística matemática
# print(drinks.sort_values(["beer_servings"], ascending=False)) #ordenando por consumo de breja
dicionario_traducoes = {
    'country': 'país',
    'beer_servings': 'consumo_cerveja',
    'spirit_servings': 'consumo_destilados',
    'wine_servings': 'consumo_vinho',
    'total_litres_of_pure_alcohol' : 'total_litros_de_puro_alcool',
    'continent' : 'continente'
}
drinks.rename(columns=dicionario_traducoes, inplace=True) #traduzindo os nomes de colunas

dicionario_continentes = {
    'AF' : 'África',
    'AS' : 'Ásia',
    'EU' : 'Europa',
    'NA' : 'América do Norte',
    'SA' : 'América do Sul',
    'OC' : 'Oceania'
}
drinks["nome_continente"] = drinks['continente'].map(dicionario_continentes) #adicionando uma coluna com o nome por extenso de cada continente
#print(drinks)

drinks["consumo_fermentados"] = drinks["consumo_cerveja"] + drinks["consumo_vinho"] #adicionando coluna fermentados
#print(drinks)
#print(drinks[drinks['consumo_cerveja'].isna()]) #trazendo países onde o c_cerva está nulo

df_cerveja = drinks.groupby("continente").agg(consumo_medio_cerveja=("consumo_cerveja","mean"), mais_bebe_cerva=("consumo_cerveja","max"))
#print(df_cerveja) #continentes que mais bebem cerveja

#trazendo tudo que é estatística sobre os continentes no que tange o consumo de vinho
df_vinho = drinks.groupby("continente").consumo_vinho.describe() 
#print(df_vinho)
