import numpy as np
from sklearn import linear_model

def read_input():
    train_data = list()
    test_data = list()
    F, N = map(int,input().split(' '))
    [train_data.append(input().split(' ')) for _ in range(0,N)]
    T = int(input())
    [test_data.append(input().split(' ')) for _ in range(0,T)]
    train_data = np.array(train_data,dtype=np.float64)
    test_data = np.array(test_data,dtype=np.float64)
    X_train = train_data[:,0:F]
    Y_train = train_data[:,-1]
    X_test = test_data
    return X_train,Y_train,X_test

def fit_and_predict(X_train,Y_train,X_test):
    model = linear_model.LinearRegression()
    model.fit(X_train,Y_train)
    Y_test = model.predict(X_test)
    return Y_test

def main():
    X_train, Y_train, X_test = read_input()
    result = fit_and_predict(X_train,Y_train,X_test)
    return '\n'.join(list(map(str,result)))

if __name__ == '__main__':
    prediction = main()
    print(prediction)
