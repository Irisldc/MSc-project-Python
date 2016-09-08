user_file=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_timely_behaviours.txt','r')
user_repeated_rating=open('reviewer_repeated_rating.txt','w')

for line in user_file:
    author, info=line.rstrip().split('\t')
    print author
    info_list=info.split(';')
    info_list=filter(None,info_list)

    dic={}
    for i in info_list:
        temp_list=i.split(',')
        item=temp_list[0]
        rating=temp_list[-1]

        if item in dic.keys():
            r=dic[item]
            if rating==r:
                r+=','+rating
                dic[item]=r
        else:
            dic[item]=rating

    repeated_count=0
    for key in dic.keys():
        ratings=dic[key].split(',')
        print key+':'+str(ratings)

        if len(ratings)>1:
            repeated_count+=1
            #print author+'\t'+key+':'+str(len(ratings))

    user_repeated_rating.write(author+'\t'+str(repeated_count)+'\n')


