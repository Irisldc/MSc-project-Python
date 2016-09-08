all_reviewer_ratings=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/A.Mukherjee_Amazon/reviewsNew.txt','r')
#record=open('rating_record.txt','w')
d={}
line_num=0
for line in all_reviewer_ratings:
    line_num+=1
    info_list=line.rstrip().split('\t')
    info_list=filter(None, info_list)

    #if len(info_list) > 2:
    print
    rating=info_list[5]
        #print rating
        #record.write(rating+'\n')
        # print 'author:'+info_list[0]+' item:'+info_list[1]
        # print 'rating:'+rating
    if rating in d.keys():
        c=d[rating]
        c+=1
        d[rating]=c
            #print rating,d[rating]
    else:
        d[rating]=1

# for key in d.keys():
#     print key, d[key]