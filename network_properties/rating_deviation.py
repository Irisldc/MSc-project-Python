reviewer_info=open('/Users/lidongchen/Documents/workspace/MapReduceAssignment/reviewer_timely_behaviours.txt','r')
item_info=open('/Users/lidongchen/PycharmProjects/MSc_project/network_properties/item_degree_info.txt','r')
reviewer_rating_deviation_ratio=open('reviewer_rating_deviation_ratio.txt','w')

item_dic={}
for i in item_info:
    item,degree,rated_degree=i.rstrip().split('\t')
    item=item.upper()
    item_dic[item]=rated_degree

print len(item_dic.keys())

for key in item_dic.keys():
    print key,item_dic[key]

for r in reviewer_info:
    author,info=r.rstrip().split('\t')

    info_list=info.split(';')
    info_list=filter(None,info_list)

    spam_cnt=0
    cnt=0
    for line in info_list:
        cnt+=1

        temp=line.split(',')
        rating=float(temp[-1])
        item=temp[0]
        item=item.upper()
        rd=float(item_dic[item])
        #print author,item,rating,rd

        if (rating>=4 and rd<=10) or (rating<=2 and rd>=100):
            spam_cnt+=1

    ratio=float(spam_cnt)/cnt
    print author,spam_cnt,cnt,ratio
    reviewer_rating_deviation_ratio.write(author+'\t'+str(ratio)+'\n')


