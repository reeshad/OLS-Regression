
import numpy as np
import matplotlib.pyplot as plot
from matplotlib import style
from statistics import mean

style.use('ggplot')

x_dataset = np.array([10,30,54,67,84,91])
y_dataset = np.array([9,15,43,51,67,87])

#Formulas for linear regression
#y = mx + b
#Yi = B1*Xi + B0 (without considering random error)
#b = mean(y) - m* mean(x)
#m = mean(x) * mean(y) - mean(x*y) / (mean(x)^2) - mean(x^2)

def slope():
    m = ((mean(x_dataset)*mean(y_dataset))-(mean(x_dataset*y_dataset)))/(((mean(x_dataset))*(mean(x_dataset)))-(mean(x_dataset*x_dataset)))
    return m

#uncomment the print function to check the error
#print(slope())

def intercept():
    b = mean(y_dataset)-(slope()*mean(x_dataset))
    return b

#uncomment the print function to check the error
#print(intercept())

m = slope()
b = intercept()
regression_line = [((m*x)+b)for x in x_dataset]

plot.scatter(x_dataset,y_dataset)
plot.plot(x_dataset,regression_line)
plot.show()

