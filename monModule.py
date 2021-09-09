import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def lorenz_curve(X,Y,df):
    df = df.sort_values(Y)
    index = (np.arange(1,df[X].shape[0]+1))
    X_lorenz = index/df[X].nunique()
    Y_lorenz = df[Y].cumsum() / df[Y].sum()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(X_lorenz, Y_lorenz, color='blue', linewidth=3)
    plt.plot([0,1], [0,1],color='grey')
    ax.set_ylim(0, 1)
    ax.set_xlim(0, 1)
    plt.title("Répartition du {} entre {}".format(Y,X))
    plt.xlabel("Part cumulée de {}".format(X))
    plt.ylabel("Part cumulée de {}".format(Y))
    
def gini(df):
    df = np.sort(df)
    index = np.arange(1,df.shape[0]+1)
    n = df.shape[0]
    return ((np.sum((2 * index - n  - 1) * df)) / (n * np.sum(df)))