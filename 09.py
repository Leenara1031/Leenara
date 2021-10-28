import numpy as np
import networkx as nx

K = np.loadtxt("social.csv", delimiter=",")
G = nx.to_networkx_graph(K)
ksub = nx.connected_component_subgraphs(G)
klist = list(ksub)

nx.draw(klist[0], with_labels=True, node_color='yellow', edge_color='red')