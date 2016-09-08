import itertools
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def writeToFile(dic,file):
    for key in dic.keys():
        print key, dic[key]
        file.write(key+'\t'+str(dic[key])+'\n')

def combine2elements(list):
    return itertools.combinations(list,2)

user_file=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_timely_behaviours.txt','r')
user_simple_weighted_edge=open('reviewer_simple_weighted_edge.txt','w')

user_cc=open('reviewer_simple_weighted_projection_cc.txt','w')
user_bc=open('reviewer_simple_weighted_projection_bc.txt','w')
user_degree=open('reviewer_simple_weighted_projection_degree.txt','w')
user_unweighted_degree=open('reviewer_simple_unweighted_projection_degree.txt','w')
user_dc=open('reviewer_simple_weighted_projection_dc.txt','w')

#create a graph
G=nx.Graph()

d={}
for line in user_file:
    author,info=line.rstrip().split('\t')

    l=[]
    info_list=info.split(';')
    info_list=filter(None,info_list)
    for i in info_list:
        temp_list=i.split(',')
        item=temp_list[0].upper()
        #print item
        l.append(item)

    d[author]=l

#add nodes to graph
author_list=d.keys()
G.add_nodes_from(author_list)

author_combine=combine2elements(author_list)
for ac in author_combine:
    item_list1=d[ac[0]]
    item_list2=d[ac[1]]
    #print ac[0],item_list1,ac[1],item_list2

    s1=set(item_list1)
    s2=set(item_list2)
    intersect_set=s1&s2
    #print ac[0],ac[1],len(intersect_set)

    if len(intersect_set)>0:

        user_simple_weighted_edge.write(ac[0]+'\t'+ac[1]+'\t'+str(len(intersect_set))+'\n')

        #create a weighted graph
        G.add_edge(ac[0],ac[1],weight=len(intersect_set))

# nx.draw(G)
# plt.show()

print G.number_of_nodes()
print G.number_of_edges()

#degree
d_d = nx.degree(G)

#degree centrality
degree_centrality=nx.degree_centrality(G)

#clustering coefficient
d_cc = nx.clustering(G)

#betweeness centrality
d_bc = nx.betweenness_centrality(G)

writeToFile(d_d,user_degree)

d_degree={}
for key in d_d.keys():
    print key,d_d[key]
    degree=d_d[key]
    if degree in d_degree.keys():
        c=d_degree[degree]
        c+=1
        d_degree[degree]=c
    else:
        d_degree[degree]=1

# fig=plt.figure()
# ax=plt.gca()
#plt.scatter(d_degree.keys(), d_degree.values(), marker='x', c='g')
# plt.xlim(pow(10,-1), 1000)
# plt.ylim(pow(10,-1), 100)
# ax.set_xscale('log')
# ax.set_yscale('log')
# plt.title('degree distribution in log-log scale')
# plt.xlabel('log degree')
# plt.ylabel('log degree count')
#fig.show()
# plt.title('cumulative degree distribution')
# plt.xlabel('degree')
# plt.ylabel('cumulative degree count')
# plt.grid()
# plt.show()