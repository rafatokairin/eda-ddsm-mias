from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plot
import numpy as np # álgebra linear
import os # acesso ao diretório
import pandas as pd # processamento dos dados .csv
import math
import seaborn as sns

for dirname, _, filenames in os.walk('/home/rafatokairin/uni-programs/ic'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Função gráficos de distribuição (histograma/gráfico de barras) dos dados das colunas
def plotPerColumnDistribution(df, nGraphShown, nGraphPerRow):
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]]  # Para fins de exibição, selecione colunas com 1 a 50 valores únicos
    nRow, nCol = df.shape
    columnNames = list(df)
    
    # Garantir que nGraphRow seja um número inteiro
    nGraphRow = math.ceil(nCol / nGraphPerRow)
    
    plt.figure(num=None, figsize=(6 * nGraphPerRow, 8 * nGraphRow), dpi=80, facecolor='w', edgecolor='k')
    
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        
        if not np.issubdtype(type(columnDf.iloc[0]), np.number):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        
        plt.ylabel('counts')
        plt.xticks(rotation=90)
        plt.title(f'{columnNames[i]} (column {i})')
    
    plt.tight_layout(pad=1.0, w_pad=1.0, h_pad=1.0)
    plt.show()

# Função matriz de correlação
def plotCorrelationMatrix(df, graphWidth):
    filename = getattr(df, 'dataframeName', 'Unnamed DataFrame')
    
    # Remove colunas com valores NaN
    df = df.dropna(axis='columns')
    
    # Manter apenas colunas com mais de 1 valor único
    df = df[[col for col in df if df[col].nunique() > 1]]
    
    # Filtrar apenas colunas numéricas
    df = df.select_dtypes(include=[float, int])
    
    # Verificar se há colunas suficientes para calcular a correlação
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    
    # Calcular matriz de correlação
    corr = df.corr()
    
    # Plotar a matriz de correlação
    plt.figure(figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Correlation Matrix for {filename}', fontsize=15)
    plt.show()

# Função gráficos de dispersão e densidade
def plotScatterMatrix(df, plotSize, textSize):
    df = df.select_dtypes(include=[np.number])  # Manter apenas colunas numéricas
    
    # Remover colunas com valores NaN
    df = df.dropna(axis='columns')
    
    # Manter colunas com mais de 1 valor único
    df = df[[col for col in df if df[col].nunique() > 1]]
    
    columnNames = list(df)
    
    # Limitar o número de colunas para evitar problemas com inversão de matriz
    if len(columnNames) > 10:
        columnNames = columnNames[:10]
    
    df = df[columnNames]

    if df.empty or len(df.columns) < 2:
        print("The DataFrame does not have enough columns to create a scatter matrix.")
        return
    
    # Criar a matriz de dispersão
    ax = pd.plotting.scatter_matrix(
        df, alpha=0.75, figsize=[plotSize, plotSize], diagonal='kde'
    )
    
    # Adicionar coeficientes de correlação na matriz
    corrs = df.corr().values
    for i, j in zip(*np.triu_indices_from(corrs, k=1)):
        ax[i, j].annotate(
            f'Corr. coef = {corrs[i, j]:.3f}',
            (0.8, 0.2),
            xycoords='axes fraction',
            ha='center',
            va='center',
            size=textSize,
        )
    
    plt.suptitle('Scatter and Density Plot')
    plt.show()