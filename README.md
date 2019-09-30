# 0 - Melbourne-Min-Temperature
## Previsão da Temperatura mínima da cidade de Melbourne (AUS)

### Dataset utilizado
- Série temporal de temperatura mínima diária referente à cidade de Melbourne, Austrália, no período de 1981 a 1990. Dados retirados de: [Australian Bureau of Meteorology](http://www.bom.gov.au/)
### Objetivos - Parte 1
- desenvolver um modelo linear de previsão, tal que:
![preditor-linear](./0-Melbourne-Min-Temperature/Imagens/preditor-linear.png)
- Para este caso, os dados de 1990 são reservados para teste
- Além disso, utilizar um esquema de __validação cruzada do tipo k-fold__ para selecionar o melhor valor do hiperparâmetro K. Neste caso, o hiperparâmetro é o número de dias anteriores ao dia em que se deseja prever a temperatura os quais devem ser avaliados de K = 1 ... 30
- Como parâmetro de qualidade do modelo preditor, deve-se utilizar o valor __RMSE (root mean squared error)__

### Objetivos - Parte 2
- desenvolver um modelo linear de previsão que utiliza como entrada valores obtidos de transformações não-lineares do vetor __x(n)__. Em outras palavras, os atributos que efetivamente são linearmente combinados na predição resultam de mapeamentos não-lineares dos atrasos da série presentes no vetor original __x(n)__. No caso, devem ser gerados T atributos transformados como a seguir:
![mapeamento-nao-linear](./0-Melbourne-Min-Temperature/Imagens/mapeamento-nao-linear.png)
- Para k = 1, ..., T e sendo os vetores __Wk__ com componentes gerados aleatoriamente conforme distribuição uniforme
- Além disso, utilizar um esquema de __validação cruzada do tipo k-fold__ juntamente com a técnica de [Ridge Regression](https://towardsdatascience.com/ridge-regression-for-better-usage-2f19b3a202db) para selecionar o melhor valor de combinação para o par ($\lambda$, T), sendo $\lambda$ o coeficiente de Ridge. Neste caso, devem ser tomadas amostras de 5 dias anteriores para T = 1 ... 100 e os possíveis valores $\lambda$ devem ser buscados iterativamente seguindo uma lógica de busca
- Como parâmetro de qualidade do modelo preditor, deve-se utilizar o valor __RMSE (root mean squared error)__
