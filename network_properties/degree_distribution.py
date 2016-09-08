import matplotlib.pyplot as plt
import numpy as np
import collections
reviewer_degree = open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_timely_behaviours.txt','r')
#reviewer_degree=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/all_reviewer_degree.txt','r')
reviewer_degree_output=open('labelled_reviewer_degree.txt','w')
#reviewer_degree_output=open('all_reviewer_degree.txt','w')

d={}
for line in reviewer_degree:
    author, reviews = line.rstrip().split('\t')

    review_list=reviews.split(';')
    review_list=filter(None, review_list)
    degree = len(review_list)

    # if degree!='':
    #     reviewer_degree_output.write(author+'\t'+degree+'\n')

    if degree in d.keys():
        c=d[degree]
        c+=1
        d[degree]=c
    else:
        d[degree]=1

# dic_key=sorted(d, key=d.get)
# dic_value=sorted(d.values())

#sort dic by key
ordered_key=collections.OrderedDict(sorted(d.items()))

dic_key=[]
dic_value=[]
for key in ordered_key:
    dic_key.append(key)
    dic_value.append(d[key])
    print key,d[key]
# print dic_key
# print dic_value

x=np.arange(pow(10,-2),pow(10,1))
y=[]
for i in x:
    y.append(pow(i,-0.5))

fig=plt.figure()
ax=plt.gca()
#plt.subplot(223)
#plt.loglog(dic_key, dic_value)
#plt.xticks(x,dic_key)
plt.xlim(1,10000)
plt.ylim(pow(10,-0.1),100)
plt.xlabel('log degree of labelled reviewers')
plt.ylabel('log count')
#plt.plot(x,y)
plt.title('degree distribution')
ax.scatter(dic_key,dic_value,c='g',marker='x')
ax.set_xscale('log')
ax.set_yscale('log')
fig.show()
plt.show()