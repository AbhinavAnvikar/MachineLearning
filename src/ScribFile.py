import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.DataFrame(pd.read_excel("AirQualityUCI.xlsx"))


#data = data.set_index("CO(GT)")

#data = data.drop("-200.0")

df_error = df[ df['CO(GT)'] < 0 ]

df = df.drop(df_error.index,axis=0)

data = pd.DataFrame(df[['Time','CO(GT)']])
data['Time'] = data['Time'].astype(str)

data['Time'] = data['Time'].replace(to_replace=':00:00',value='',regex=True)

print(data.dtypes)

x=list(data['Time'])
y=list(data['CO(GT)'])

print(y)

#
# print(time_inf)


"""

x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='Quadretic')
plt.legend()

# generate random data-set
#np.random.seed(0)
x = [1,2,3,4,5]
y = [1,3,4,6,4]
m=1
b=0
iter = 10
learn_rate=.025

def linearRegression(x,y):
    n=np.size(x)
    m_x, m_y = np.mean(x), np.mean(y)
    SS_xy = np.sum(np.multiply(x,y)) - n * m_y * m_x
    SS_xx = np.sum(np.multiply(x,x)) - n * m_x * m_x
    m = SS_xy / SS_xx
    b = m_y - m * m_x
    print(m);
    print(b);
    return m,b



def prediction_line(x,m,b):
    y_pred  = b + np.multiply(m,x)
    plt.scatter(x, y_pred, s=30, marker='x')
    plt.plot(x,y_pred,color='g')

# plot

res = linearRegression(x,y)
prediction_line(x,res[0],res[1])
plt.scatter(x,y,s=30,marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

"""