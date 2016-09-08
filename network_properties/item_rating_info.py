import matplotlib.pyplot as plt
import numpy as np
import collections

item_rating=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/labelled_item_rating_dates.txt','r')
item_degree_info=open('item_degree_info.txt','w')

authors=set()

d={}
for line in item_rating:

    item, ratings=line.rstrip().split('\t')

    rating_list=ratings.split('|')
    rating_list=filter(None, rating_list)

    degree=0
    rating_degree=0

    for r in rating_list:

        temp=r.split(';')
        rating=temp[-1]
        #print item,rating
        author=temp[0]

        authors.add(author)
        degree+=1
        rating_degree+=float(rating)

    if rating_degree in d.keys():
        c=d[rating_degree]
        c+=1
        d[rating_degree]=c
    else:
        d[rating_degree]=1

    item_degree_info.write(item+'\t'+str(degree)+'\t'+str(rating_degree)+'\n')

#sort dic by key
ordered_key=collections.OrderedDict(sorted(d.items()))
dic_key=[]
dic_value=[]
for key in ordered_key:
    dic_key.append(key)
    dic_value.append(d[key])
    print key,d[key]

dic_value=np.cumsum(dic_value)

for pos in range(len(dic_value)):
    print dic_key[pos],float(dic_value[pos])/dic_value[-1]

print dic_value
fig=plt.figure()
ax=plt.gca()
ax.scatter(d.keys(),d.values(),c='g',marker='x')
ax.set_xscale('log')
ax.set_yscale('log')
#ax.scatter(dic_key,dic_value,c='b',marker='x')
# plt.ylim(-20,800)
# plt.xlim(-20,800)
plt.grid()
plt.ylabel('cumulative count')
plt.xlabel('item rated degree')
plt.title('labelled items rated-degree distribution')
fig.show()
plt.show()

print len(authors)

