import pandas as pd
import numpy as np


chat_id =  968976840 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = 100  
    t = 41  
    s = np.random.laplace(loc=100, scale=10, size=n)  
    a = 2 * s / (t ** 2)  
    x_mean = np.mean(a)  
    return x.mean() # Ваш ответ
