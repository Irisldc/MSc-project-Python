import re,datetime
from os import listdir
from os.path import isfile,join
import glob

def readItem(fileDir):
    l=[]
    item_info=open(fileDir,'r')
    for line in item_info:
        date,rating=line.split(',')
        l.append(date)

    return l

def readReviewer(fileDir,days):

    early_count=0
    total_count=0

    reviewer_info=open(fileDir,'r')

    for line in reviewer_info:
        total_count+=1
        item, review_date=line.split('\t')

        print item

        item_file_path='/Users/lidongchen/Documents/UCL/MSc_project/Dataset/item_rating_dates/item_'+item+'.txt'
        item_dates=readItem(item_file_path)

        sorted_date=sorted(item_dates,key=lambda x:datetime.datetime.strptime(x, '%Y-%m-%d'))
        #print sorted_date

        first_review_date=datetime.datetime.strptime(sorted_date[0],'%Y-%m-%d')
        end_date=first_review_date+datetime.timedelta(days)

        print first_review_date
        print end_date

        review_date=datetime.datetime.strptime(review_date.rstrip(), '%Y-%m-%d')
        print review_date

        if first_review_date<=review_date<=end_date:
            early_count+=1
            print 'between'
        else:
            print 'not between'

    early_ratio=float(early_count)/total_count
    print 'early ratio='+str(early_ratio)
    return early_ratio

month=30
month_count=3
early_review_file=open('reviewer_early_ratio_'+month_count+'_month.txt','w')

fileDir='/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_item_dates/'

#reviewer_files=[f for f in listdir(fileDir) if isfile(join(fileDir, f))]
reviewer_files=glob.glob(fileDir+'*.txt')

for r in reviewer_files:
    # path=fileDir+r
    #
    # print path
    print r

    early_ratio=readReviewer(r, month*month_count)
    temp_list = r.split('/')
    name_list=re.split(r'[_.]+', temp_list[-1])
    reviewer_id=name_list[1]

    early_review_file.write(reviewer_id+'\t'+str(early_ratio)+'\n')





