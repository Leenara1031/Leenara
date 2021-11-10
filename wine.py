import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# red_df = pd.read_csv('../resources/winequality-red.csv', sep = ';', header = 0, engine= 'python')
# white_df = pd.read_csv('../resources/winequality-white.csv', sep = ';', header = 0, engine= 'python')
#
# red_df.to_csv('../resources/winequality-red.csv', index = False)
# white_df.to_csv('../resources/winequality-white.csv', index = False)
#
# red_df.head()
# red_df.insert(0, column = 'type', value = 'red')
# red_df.head()
# red_df.shape
#
# white_df.head()
# white_df.insert(0, column = 'type', value = 'white')
# white_df.head()
# white_df.shape
#
# wine = pd.concat([red_df, white_df])
# wine.shape
# wine.to_csv('../resources/wine.csv', index = False)

data_df = pd.read_csv('../resources/wine.csv', header = 0, engine= 'python')

print('데이터셋 크기 : ', data_df.shape)
print(data_df.head())

data_df = data_df.drop(['type', 'alcohol', 'quality'], axis = 1, inplace = False)
print(data_df.head())

print('데이터셋 크기 : ', data_df.shape)
print(data_df.info())

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

Y = data_df['mpg']
X = data_df.drop(['mpg'], axis = 1, inplace = False)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 0)
lr = LinearRegression()
lr.fit(X_train, Y_train)

Y_predict = lr.predict(X_test)

mse = mean_squared_error(Y_test, Y_predict)
rmse = np.sqrt(mse)
print('MSE : {0:.3F}, RMSE : {1:.3f}'.format(mse, rmse))
print('R^2(Variance score) : {0:.3f}'.format(r2_score(Y_test, Y_predict)))

print('Y 절편 값 : ', np.round(lr.intercept_, 2))
print('회귀 계수 값 : ', np.round(lr.coef_, 2))

coef = pd.Series(data = np.round(lr.coef_, 2), index = X.columns)
coef.sort_values(ascending = False)

fig, axs = plt.subplots(figsize = (13, 13), ncols = 13, nrows = 5)
x_features = ['type', 'quality']
# x_features = ['sulphates', 'pH', 'density', 'total sulfur dioxide',
#               'free sulfur dioxide', 'chlorides', 'residual sugar',
#               'citric acid', 'volatile acidity', 'fixed acidity']
plot_color = ['r', 'b']

for i, feature in enumerate(x_features):
    row = int(i/2)
    col = i%2
    sns.regplot(x = feature, y = 'mpg', data = data_df, ax = axs[row][col], color = plot_color[i])

plt.show()