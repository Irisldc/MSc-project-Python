import re

item_rating=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/044653143X_rating_dates.txt','r')
item_rating_dates=open('./044653143X_cumlative_rating_dates.txt','w')
item_rating_counts=open('./044653143X_cumlative_rating_counts.txt','w')

cumSum=0
cumCnt=0

for line in item_rating:
    tokens=line.split('\t')

    item=tokens[0]
    rating_dates=tokens[1].split(',')

    #if len(tokens)>2:
    sum=float(rating_dates[0])
    cnt=int(rating_dates[1])

    cumSum+=sum
    cumCnt+=cnt

    cumAvg=float(cumSum/cumCnt)

    item_rating_dates.write(item+'\t'+str(cumAvg)+'\n')
    item_rating_counts.write(item+'\t'+str(cnt)+'\n')





