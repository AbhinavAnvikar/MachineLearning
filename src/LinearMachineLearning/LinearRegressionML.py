import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

"""data= pd.read_csv("test_data.csv")
print(data)
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='Quadretic')
plt.legend()
"""

# generate random data-set
#np.random.seed(0)


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

def calculateError(x,y,m,b):
    no_of_sample = np.size(x)
    err_tot = 0
    for i in range(no_of_sample):
        err_tot += (y[i] - (m*x[i] + b))**2
    err = err_tot/no_of_sample
    return err

#TODO : Generate
def gradientDescent(m,b,x,y,learn_rate):
    no_size = np.size(x)
    m_grad_sum = float(0)
    b_grad_sum = float(0)
    for i in range(no_size):
        m_grad_sum = m_grad_sum - (x[i] * ((y[i] - (m*x[i] + b))))
        b_grad_sum = b_grad_sum - round((y[i] - (m*x[i]+b)),ndigits=3)
    m_delta = m_grad_sum * (2/no_size)
    b_delta = b_grad_sum * (2/no_size)
    new_m = m - (learn_rate * m_delta)
    new_b = b - (learn_rate * b_delta)
    return new_m,new_b

def trainModel(m,b,x,y,learn_rate,iter):
    res=[m,b]
    prediction_line(x, res[0], res[1],'r')
    for i in range(1,iter+1):
        res = gradientDescent(res[0],res[1],x,y,learn_rate)
        print(f'Iteration : {i} , Value of m : {res[0]} , Value of b : {res[1]}, Error Rate : {calculateError(x,y,res[0],res[1])}')
        time.sleep(.1)
    #prediction_line(x, res[0], res[1], 'g')
    return res[0],res[1]
#',format(iter,res[0],res[1],calculateError(x,y,res[0],res[1])))

def modelTest(x,m,b):
    y = m*x + b
    return y

def prediction_line(x,m,b,color):
    y_pred  = b + np.multiply(m,x)
    plt.scatter(x, y_pred, s=30, marker='*' ,color=color)
    plt.plot(x,y_pred,color=color)

def main():
    # Random Sample Set
    x = [1, 2, 3, 4, 5]
    y = [1, 3, 2.5, 4.5, 4.5]

    # Start with basic coeficient variables
    m = 0.0
    b = 0.0
    iter = 100  # no of iteration to train the model
    learn_rate = .025  # Rate of learning
    plt.scatter(x, y, s=40, marker='o')
    plt.ylabel('Number of Objects (in Millions)')
    plt.xlabel('Number of Iterations')
    m,b= trainModel(m,b,x,y,learn_rate,iter)
    x.append(6)
    prediction_line(x, m, b,'g')
    plt.show()

if __name__== '__main__':
    main()