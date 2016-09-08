import matplotlib.pyplot as plt
import datetime
import numpy as np

#A1O6R8R9BH159F
#A1ZCYIK3SLXA
user_file=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/user_A1O6R8R9BH159F_rating_count.txt','r')

features_file='/Users/lidongchen/PycharmProjects/MSc_project/reviewer_features.csv'

def count_degree(file):

    spammer_dic={}
    non_spammer_dic={}

    file=open(file,'r')

    line_num=0
    for line in file:
        if line_num==0:
            line_num+=1
            continue
        else:
            info=line.rstrip().split(',')
            label=float(info[-1])
            degree=float(info[11])
            cc=float(info[9])

            if label==0:
                if degree in non_spammer_dic.keys():
                    c=non_spammer_dic[degree]
                    c+=1
                    non_spammer_dic[degree]=c
                else:
                    non_spammer_dic[degree]=1
            else:
                if degree in spammer_dic.keys():
                    c = spammer_dic[degree]
                    c += 1
                    spammer_dic[degree] = c
                else:
                    spammer_dic[degree] = 1

            line_num+=1
    return spammer_dic,non_spammer_dic

x=[]
y=[]

spammer_dic,non_spammer_dic=count_degree(features_file)

print spammer_dic
for key in spammer_dic.keys():
    x.append(key)
    y.append(float(spammer_dic[key])/344)

# for line in user_file:
#     tokens=line.split('\t')
#     x#.append(datetime.datetime.strptime(tokens[0],"%Y-%m-%d").date())
#     x.append(int(float(tokens[0])))
#     y.append(int(tokens[1]))
#y=np.cumsum(y)

plt.scatter(x,y,marker='x',c='green')
plt.title('degree distribution of spammers')
plt.xlabel('degree k')
plt.ylabel('p(k)')
# ax=plt.subplot(111)
# ax.bar(x,y,width=0.5,color='blue',align='center')
#ax.set_xlim(0,6)
# ax.set_ylim()
#ax.xaxis_date()
# ax.set_title('user A1O6R8R9BH159F rating distribution')
# ax.set_xlabel('ratings')
# ax.set_ylabel('count of ratings')
plt.show()