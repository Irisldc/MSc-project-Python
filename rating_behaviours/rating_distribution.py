user_rating = open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_timely_behaviours.txt','r')
user_rating_distribution=open('reviewer_rating_distribution.txt','w')

for line in user_rating:
    author, info=line.rstrip().split('\t')
    info_list=info.split(';')
    info_list=filter(None,info_list)

    d={}

    cnt=0
    for i in info_list:
        temp_list=i.split(',')
        rating=temp_list[-1]
        cnt+=1
        if rating in d.keys():
            c=d[rating]
            c+=1
            d[rating]=c
        else:
            d[rating]=1

    print author, d, cnt

    p=0
    for key in d.keys():
        if key=='1.0' or key=='5.0':
            per=float(d[key])/cnt
            p+=per

    print p
    user_rating_distribution.write(author+'\t'+str(p)+'\n')