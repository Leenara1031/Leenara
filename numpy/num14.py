import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
plt.xlabel('Degree')
plt.ylabel('Prob. of node degree')
plt.hist(list([d for n, d in G.degree()]), histtype='step')