import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
# days,values=np.loadtxt('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/fake_A3URRTIZEE8R7W_dates_count.txt',unpack=True,
#                        converters={0:mdates.strpdate2num('%Y-%m-%d')})
# days1,values1=np.loadtxt('/Users/lidongchen/PycharmProjects/MSc_project/preprocessing/044653143X_cumlative_rating_counts.txt',unpack = True,
#          converters = {0: mdates.strpdate2num('%Y-%m-%d')})
#,fmt='bx'

reviewer_date_count=open('/Users/lidongchen/PycharmProjects/MSc_project/timely_behaviours/reviewer_numOfReviews_monthly.txt','r')

for line in reviewer_date_count:
    author,dates=line.rstrip().split('\t')
    date_list=dates.split(';')
    date_list=filter(None,date_list)

    if author == 'A1ZCYIK3SLXA':

        X=[]
        Y=[]
        for d in date_list:

            review_date,info=d.split(' ')
            review_count=info.split(':')[-1]
            print review_count

            review_date = datetime.strptime(review_date, '%Y-%m-%d')
            X.append(review_date)
            Y.append(review_count)
            # if review_date in dic.keys():
            #     c=dic[review_date]
            #     c+=1
            #     dic[review_date]=c
            # else:
            #     dic[review_date]=1

        #print dic
        plt.plot_date(x=X,y=Y,fmt='o--')
        #plt.plot_date(x=days1,y=values1,fmt='gx')

        plt.ylim([0,5])
        plt.title('reviewer '+author+' timely behaviours')
        #plt.xlabel('time')
        plt.ylabel('num of reviews')
        plt.grid(True)
        plt.show()