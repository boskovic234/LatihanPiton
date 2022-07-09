import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd

x = [8.0, 1, 2.5, 4, 28.0]
x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]
print(x)
print(x_with_nan)

# MEAN = Average = Rata2

# Cara 1
mean_ = sum(x) / len(x)
mean_

# Cara 2
mean_ = statistics.mean(x)
mean_

means = 0.24857 * 2 + 0.45647 * 4 + 0.35948 * 8
means
round(means)

# Weighted mean, juga disebut weighted arithmetic mean atau weighted average, 
# adalah generalisasi dari rata-rata aritmatika yang memungkinkan kita untuk menentukan kontribusi relatif dari setiap titik data ke hasil.
x = [8.0, 1, 2.5, 4, 28.0]
w = [0.1, 0.2, 0.3, 0.25, 0.15]

wmean = sum(w[i] * x[i] for i in range(len(x))) / sum(w)
print(wmean)

wmean = sum(x_ * w_ for (x_, w_) in zip(x, w)) / sum(w)
print(wmean)

y, z, w = np.array(x), pd.Series(x), np.array(w)

wmean = np.average(y, weights=w)
print(wmean)

wmean = np.average(z, weights=w)
print(wmean)

# Harmonic Mean
hmean = len(x) / sum(1 / item for item in x)
hmean

x = [60,20]
hmean = len(x) / sum(1 / item for item in x)
hmean

hmean = statistics.harmonic_mean(x)
hmean

# Geometri Mean
gmean = 1

for item in x:
    gmean *= item
    
gmean **= 1 / len(x)
gmean

scipy.stats.gmean(y)

# Median
# [8.0, 1, 2.5, 4, 28.0],2
x = [8.0, 1, 2.5, 4, 28.0]
n = len(x) 
if n % 2:
    print('cek')
    median_ = sorted(x)[round(0.5*(n-1))]
else:
    print('cek2')
    x_ord, index = sorted(x), round(0.5 * n)
    median_ = 0.5 * (x_ord[index-1] + x_ord[index])

median_

# Mode/Modus, nilai yang sering muncul
u = [2, 3, 2, 8, 12]
v = [12, 15, 12, 15, 21, 15, 12]

mode_ = statistics.mode(u)
mode_

# Measure Of Variability (Variance)
# [8.0, 1, 2.5, 4, 28.0]
n = len(x)

mean_ = sum(x) / n
sum(x)
mean_

((1-8.7)**2+(2.5-8.7)**2+(4-8.7)**2+(8-8.7)**2+(28-8.7)**2)/4

var_ = sum((item - mean_)**2 for item in x) / (n - 1)
var_

var_ = statistics.variance(x)
var_

# Standard Deviation

