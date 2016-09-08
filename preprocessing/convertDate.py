import re

user_behaviour=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_timely_behaviours.txt','r')

count=0

for line in user_behaviour:
    count+=1
    items=line.split('\t')

    author=items[0]
    info_list=items[1].split(';')
    author_file = open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_item_dates/user_' + author+'.txt', 'w')

    for i in (info_list):
        temp_list=re.split(r'[,\s]+', i)
        #print str(len(temp_list))
        if len(temp_list)>=5:

            item=temp_list[0]
            month=temp_list[1]

            if month=='January':
                month = '01'
            if month == 'February':
                month = '02'
            if month == 'March':
                month = '03'
            if month == 'April':
                month = '04'
            if month == 'May':
                month = '05'
            if month == 'June':
                month = '06'
            if month == 'July':
                month = '07'
            if month == 'August':
                month = '08'
            if month == 'September':
                month = '09'
            if month == 'October':
                month = '10'
            if month == 'November':
                month = '11'
            if month == 'December':
                month = '12'

            day=temp_list[2]
            year=temp_list[3]
            date=year+'-'+month+'-'+day

            author_file.write(item+'\t'+date+'\n')

print 'num of users:'+str(count)