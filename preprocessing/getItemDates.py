import re

item_list=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/item_rating_dates.txt','r')

for line in item_list:

    tokens=line.split('\t')
    item=tokens[0]
    info=tokens[1].split('|')

    item_file = open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/item_rating_dates/item_'+item+'.txt', 'w')

    for i in info:
        info_list=i.rstrip().split(';')

        if len(info_list)>2:
            date=info_list[1]
            rating=info_list[2]
            date_list=re.split(r'[,\s]+', date)

            if len(date_list)>2:
                month=date_list[0]
                day=date_list[1]
                year=date_list[2]

                flag=0

                if month == 'January':
                    month = '01'
                elif month == 'February':
                    month = '02'
                elif month == 'March':
                    month = '03'
                elif month == 'April':
                    month = '04'
                elif month == 'May':
                    month = '05'
                elif month == 'June':
                    month = '06'
                elif month == 'July':
                    month = '07'
                elif month == 'August':
                    month = '08'
                elif month == 'September':
                    month = '09'
                elif month == 'October':
                    month = '10'
                elif month == 'November':
                    month = '11'
                elif month == 'December':
                    month = '12'
                else:
                    flag=1
                    print 'item:'+item+' month='+month+' year='+year+' day='+day

                date=year+'-'+month+'-'+day
                if flag==0:
                    item_file.write(date+','+rating+'\n')


