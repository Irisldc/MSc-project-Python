from datetime import datetime
import re

user_time = open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_timely_behaviours.txt','r')
user_life = open('reviewer_life_time.txt','w')

cnt=0
for line in user_time:
    cnt+=1

    author,info=line.rstrip().split('\t')
    print author
    info_list=info.split(';')
    info_list=filter(None, info_list)

    date_list=[]

    for i in info_list:
        temp_list = re.split(r'[,\s]+', i)

        if len(temp_list)>4:

            month=temp_list[1]
            day=temp_list[2]
            year=temp_list[3]

            full_date=year+' '+month+' '+day
            #print full_date

            full_date=datetime.strptime(full_date, '%Y %B %d')
            #print full_date
            date_list.append(full_date)

    date_list=sorted(date_list)
    print date_list

    life_time=date_list[-1]-date_list[0]
    print 'life time:'+str(life_time)
    temp=str(life_time).split(' ')

    if len(temp)==1:
        life=0
    else:
        life=temp[0]

    user_life.write(author+'\t'+str(life)+'\n')

print 'num of reviewers:'+str(cnt)