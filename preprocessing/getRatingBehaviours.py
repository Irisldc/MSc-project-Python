import re
reviewer_info=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_timely_behaviours.txt','r')

cnt=0

for line in reviewer_info:

    cnt+=1
    tokens=line.split('\t')

    author=tokens[0]
    behaviours=tokens[1].split(';')

    user_rating=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_ratings/user_' + author+'.txt', 'w')

    for b in behaviours:
        info=re.split(r'[,\s]+', b)

        if len(info)>4:
            rating=info[4]

            user_rating.write(rating+'\n')

print 'compelet. num of reviewers:'+str(cnt)
