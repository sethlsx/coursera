import networkx as nx
import numpy
from matplotlib import pyplot as plt

#read in the data
data = numpy.loadtxt('./data/facebook_combined.txt')

#Create a network graph
G = nx.Graph()
edge = []
for line in data:
    edge.append(tuple(line))
G.add_edges_from(edge)

nx.draw_networkx(G)
plt.show()