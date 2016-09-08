from itertools import groupby
import re
from datetime import datetime

reviewer_file=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_timely_behaviours.txt','r')
reviewer_burstiness=open('max_numOf_reviews_daily.txt','w')

for line in reviewer_file:
    author, info=line.rstrip().split('\t')
    info_list=info.split(';')
    info_list=filter(None,info_list)

    date_list=[]
    for i in info_list:
        temp_list = re.split(r'[,\s]+', i)

        if len(temp_list)>4:
            month=temp_list[1]
            day=temp_list[2]
            year=temp_list[3]
            full_date=year+' '+month+' '+day

            full_date = str(datetime.strptime(full_date, '%Y %B %d'))
            # print full_date
            date_list.append(full_date)

    date_list = sorted(date_list)
    print date_list

    date_str=''
    # group dates by day
    num0f_reviews=[]
    for k, v in groupby(date_list, key=lambda x: x):
    #group dates by month
    #for k, v in groupby(date_list, key=lambda x: x[:7]):
        l=list(v)
        date_str+=k+':'+str(len(l))+';'
        num0f_reviews.append(len(l))
        print k, l, len(l)

    m=max(num0f_reviews)
    print author,m
    #group dates by week
    # for k,v in groupby(date_list, lambda x:x.days//7):
    #     print k, list(v)
    #reviewer_burstiness.write(author+'\t'+date_str+'\n')
    reviewer_burstiness.write(author+'\t'+str(m)+'\n')