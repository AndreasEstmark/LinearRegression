import numpy as np
import pandas as pd

df["Intercept"] = 1
#%%
class LinearRegression:

    """
    Method to compute the parameters of linear regression and R squared. 
    """

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def show_data(self):
        print(self.x, self.y)

    def fit(self):

        x = self.x

        y = self.y

        beta = inv(np.transpose(x).dot(x)).dot(np.transpose(x)).dot(y)

        e = y-x.dot(beta)

        squaredError = (np.transpose(e).dot(e))

        yDemeanedB = np.transpose(y-np.mean(y)).dot(y-np.mean(y))
            
        R2 = 1- (np.transpose(e).dot(e)/yDemeanedB)

        return [
            beta,
             R2
        ]

reg = LinearRegression(df.iloc[:,1:3], df.)

print(reg.fit())
