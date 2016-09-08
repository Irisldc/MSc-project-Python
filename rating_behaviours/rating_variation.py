import numpy as np
from numpy import array
import scipy.stats.stats as st

reviewer_rating=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_timely_behaviours.txt','r')
reviewer_variation=open('reviewer_skewness.txt','w')

for line in reviewer_rating:
    author, info=line.rstrip().split('\t')

    info_list=info.split(';')
    info_list=filter(None, info_list)

    arr=[]
    for i in info_list:
        temp_list=i.split(',')
        rating=temp_list[-1]
        arr.append(float(rating))

    np_arr=array(arr)

    # std=np.std(np_arr,ddof=1)
    # mean=np.mean(np_arr)
    skewness=st.skew(np_arr)
    #print std, mean, std/mean
    print skewness
    #reviewer_variation.write(author+'\t'+str(std/mean)+'\n')
    reviewer_variation.write(author+'\t'+str(skewness)+'\n')