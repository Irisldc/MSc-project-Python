import matplotlib.pyplot as plt
import collections
import numpy as np

reviewer_helpfulenss=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/labelled_reviewer_helpfulness.txt','r')

def simple_helpfulness_score():
    reviewer_helpfulenss_output = open('reviewer_helpfulness_ratio_norm.txt','w')
    d={}

    for line in reviewer_helpfulenss:
        author,info=line.rstrip().split('\t')

        info_list=info.split(';')
        info_list=filter(None,info_list)

        score=0
        cnt=0
        for i in info_list:
            cnt+=1
            h_vote,all_vote=i.split(':')
            h_vote=float(h_vote)
            all_vote=float(all_vote)

            if all_vote==0:
                score+=0
            else:
                score+=h_vote/all_vote

        if score in d.keys():
            c=d[score]
            c+=1
            d[score]=c
        else:
            d[score]=1

        print author,score
        norm_score=float(score)/cnt
        reviewer_helpfulenss_output.write(author+'\t'+str(norm_score)+'\n')

    return d

def weighted_helpfulness_score():
    d={}
    reviewer_helpfulenss_output = open('reviewer_helpfulness_weight.txt', 'w')
    for line in reviewer_helpfulenss:
        author, info = line.rstrip().split('\t')

        info_list = info.split(';')
        info_list = filter(None, info_list)

        pos_vote=0
        neg_vote=0

        for i in info_list:
            h_vote, all_vote = i.split(':')
            h_vote = float(h_vote)
            all_vote = float(all_vote)

            uh_vote=all_vote-h_vote
            pos_vote+=h_vote
            neg_vote+=uh_vote

        w_vote=pos_vote-neg_vote

        if w_vote in d.keys():
            c=d[w_vote]
            c+=1
            d[w_vote]=c
        else:
            d[w_vote]=1

        print author,w_vote
        reviewer_helpfulenss_output.write(author+'\t'+str(w_vote)+'\n')

    return d

def plot(dic):

    # #sort dic by key
    ordered_key=collections.OrderedDict(sorted(dic.items()))

    dic_keys=[]
    dic_values=[]

    for key in ordered_key:
        dic_keys.append(key)
        dic_values.append(dic[key])
        #print key,dic[key]

    dic_values=np.cumsum(dic_values)
    print dic_keys,dic_values
    # fig=plt.figure()
    # ax=plt.gca()
    plt.scatter(dic_keys, dic_values, c='b', marker='x')
    plt.title('reviewers helpfulness score vs. count')
    plt.xlabel('helpfulness score')
    plt.ylabel('cumulative count')
    # ax.set_xscale('log')
    # ax.set_yscale('log')
    plt.xlim(-1000,30000)
    #fig.show()
    plt.grid()
    plt.show()

#simple_helpfulness_score()
dic=weighted_helpfulness_score()
plot(dic)