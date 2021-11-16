import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

K = np.loadtxt('C:/Users/202-19/AI/test.csv', delimiter=',')
G = nx.to_networkx_graph(K)
nx.draw(G)
plt.show()

