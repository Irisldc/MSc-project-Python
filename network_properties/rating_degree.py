import matplotlib.pyplot as plt
import collections

user_rating = open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_timely_behaviours.txt','r')
labelled_simple_degree=open('labelled_simple_degree_edges.csv','w')

unweighted_degree_list=[]
rating_degree_list=[]

for line in user_rating:
    author, info=line.rstrip().split('\t')
    info_list=info.split(';')
    info_list=filter(None,info_list)

    unweighted_degree=len(info_list)

    rating_degree=0
    for i in info_list:
        temp=i.split(',')
        item=temp[0]
        rating=temp[-1]
        rating_degree+=float(rating)

        labelled_simple_degree.write(author+','+item+','+rating+'\n')

    unweighted_degree_list.append(unweighted_degree)
    rating_degree_list.append(rating_degree)

#     if unweighted_degree>1000:
#         print author, unweighted_degree, rating_degree
#
# print len(unweighted_degree_list), len(rating_degree_list)
#
# plt.title('number of reviews vs. rating sum')
# plt.xlabel('number of reviews')
# plt.ylabel('rating sum')
# plt.scatter(unweighted_degree_list,rating_degree_list,c='g',marker='x')
# plt.grid()
# plt.show()