#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("daily-minimum-temperatures.csv")
df['Index'] = df.index


# In[3]:


df.head(10)


# In[4]:


df.shape


# In[5]:


df.describe()


# In[6]:


# Check if data has NaN/NULL values
df.isnull().any().any()


# In[7]:


plt.figure(figsize = (20, 10))
df_test = df.iloc[0:100,:]
df_test["Temp"].plot(label = "test")
plt.legend()


# In[71]:


plt.figure(figsize = (15, 10))
df_1981 = df.iloc[0:365*1,:]
df_1981["Temp"].plot(label = "1981")
df_1982 = df.iloc[365*1:365*2,:]
df_1982["Temp"].plot(label = "1982")
df_1983 = df.iloc[365*2:365*3,:]
df_1983["Temp"].plot(label = "1983")
df_1984 = df.iloc[365*3:365*4,:]
df_1984["Temp"].plot(label = "1984")
df_1985 = df.iloc[365*4:365*5,:]
df_1985["Temp"].plot(label = "1985")
df_1986 = df.iloc[365*5:365*6,:]
df_1986["Temp"].plot(label = "1986")
df_1987 = df.iloc[365*6:365*7,:]
df_1987["Temp"].plot(label = "1987")
df_1988 = df.iloc[365*7:365*8,:]
df_1988["Temp"].plot(label = "1988")
df_1989 = df.iloc[365*8:365*9,:]
df_1989["Temp"].plot(label = "1989")
df_1990 = df.iloc[365*9:365*10-1,:]
df_1990["Temp"].plot(label = "1990")
plt.ylabel("Temperature - °C", size = 30, labelpad = 25)
plt.xlabel("Index - Day", size = 30, labelpad = 25)
plt.legend()


# In[43]:


# Split Training and Test data
training = df.iloc[0:len(df)-365, :]
test = df.iloc[len(df)-365:len(df), :]


# In[18]:


def fit_reg_lin(X, Y):
    '''
    Função que gera um modelo de Regressão Linear baseado solução fechada (pseudo inversa) do tipo 
    y' = w0 + w1*X1 + ... + wk*Xk, a partir de um vetor de amostras X e Y
    output: [w0, w1, ..., wn]
    '''
    # phi matrix - add a column of 1's for w0 weight
    phi = np.c_[np.ones(len(X)), X]
    
    # Y matrix    
    Y = np.matrix(Y).reshape((len(Y), 1))
    
    # calculate w = (phi.T * phi)-¹ * phi.T * Y, where * is matrix product
    return (np.linalg.inv(phi.T.dot(phi)).dot(phi.T).dot(Y))


# In[19]:


# K = 30
k = 30

X = np.zeros((len(training), k))
Y = np.zeros((len(training), 1))

for i in range(len(training)):
    X[i] = df["Temp"][i+0 : i+k]
    Y[i] = df["Temp"][i+k]


# In[20]:


print(X.shape)
print(Y.shape)


# In[21]:


fit_reg_lin(X = X, Y = Y)


# # to do
# - avaliar o modelo obtido acima, descobrir qual Xi vai com qual Wi
#     - quem é o bias: 0.549 ou 0.589? aparentemente, pelo jeito que o problema foi modelado, 0.549 é o bias e 0.0009495 é o termo que múltiplica a entrada x(n = -k)
# - calcular o erro quadratico medio do modelo obtido acima
# - dispor os dados em formato "anelar", isto é, o último dado "dar a mão" ao primeiro dado
# - obter modelos para diferentes valores de K
# - ler sobre regras de generalização
# - realizar cross-validation com K fold

# In[23]:


def fit_reg_lin_v2(X, Y):
    '''
    Função que gera um modelo de Regressão Linear baseado solução fechada (pseudo inversa) do tipo 
    y' = w0 + w1*X1 + ... + wk*Xk, a partir de um vetor de amostras X e Y
    output: [w0, w1, ..., wn]
    '''
    # phi matrix - add a column of 1's for w0 weight
    phi = X
    
    # Y matrix    
    Y = np.matrix(Y).reshape((len(Y), 1))
    
    # calculate w = (phi.T * phi)-¹ * phi.T * Y, where * is matrix product
    return (np.linalg.inv(phi.T.dot(phi)).dot(phi.T).dot(Y))


# In[27]:


# K = 30
k = 30

X = np.zeros((len(training), k))
Y = np.zeros((len(training), 1))

for i in range(len(training)):
    X[i] = df["Temp"][i+0 : i+k]
    Y[i] = df["Temp"][i+k]
    
# Add a column of 1's to X for w0
X = np.c_[np.ones(len(X)), X]


# In[37]:


W = fit_reg_lin_v2(X=X, Y = Y)
print (W.shape)


# In[32]:


X.shape


# In[73]:


# Evaluating the model

# data for test
k = 30
X_test = np.zeros((len(test), k))
Y_test = np.zeros((len(test), 1))
                  
for i in range(len(test)):
    X_test[i] = df["Temp"][len(df["Temp"]) - 365 - k + i: len(df["Temp"]) - 365 + i]
    Y_test[i] = df["Temp"][len(df["Temp"]) - 365 + i]

# Add a column of 1's to X for w0
X_test = np.c_[np.ones(len(X_test)), X_test]

y_estimated = X_test.dot(W)
y_real = Y_test

print(type(y_estimated))
print(type(y_real))
plt.figure(figsize = (20, 10))
plt.plot(y_estimated, color = "red", label = "my model")
plt.plot(y_real, color = "blue", label = "real data")
plt.legend()

