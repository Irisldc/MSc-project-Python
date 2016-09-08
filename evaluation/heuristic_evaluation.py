from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
feafure_file=open('/Users/lidongchen/PycharmProjects/MSc_project/reviewer_features.csv','r')

y_predict=[]
y_true=[]

line_num=0
true_reviewer=0
fake_reviewer=0
for f in feafure_file:

    if line_num==0:
        line_num+=1
        continue
    else:
        info_list=f.rstrip().split(',')
        info_list=filter(None,info_list)

        life_time=float(info_list[1])
        max_reviews_daily=float(info_list[2])
        early_review_ratio=float(info_list[3])

        rating_distribution=float(info_list[4])
        repeated_rating=float(info_list[5])

        summary_duplicate=float(info_list[6])
        helpfulness=float(info_list[7])
        rating_deviation=float(info_list[8])

        cc=float(info_list[9])
        bc=float(info_list[10])
        degree=float(info_list[11])
        true_label=float(info_list[12])

        if true_label==1:
            fake_reviewer+=1
        else:
            true_reviewer+=1

        # lift time, helpfulness, cc, betweenness, degree
        #if (life_time<=3 and helpfulness<=1) or ((cc>=0.5 or cc==0) and bc<pow(10,-4)) or degree<=80:
        if (life_time<=3 and max_reviews_daily>=3 and early_review_ratio>=0.15) or\
                (rating_distribution>=0.8 and rating_deviation>=0.2 and helpfulness<=0) or\
                summary_duplicate>=0.15 or repeated_rating>=1 or \
                ((cc>=0.5 or cc==0) and bc<pow(10,-4)) or degree<=80:

            label=1
        else:
            label=0

        y_predict.append(label)
        y_true.append(true_label)

        line_num+=1

precision=precision_score(y_true,y_predict,average='binary')
recall=recall_score(y_true,y_predict,average='binary')
f1=f1_score(y_true,y_predict,average='binary')
auc=roc_auc_score(y_true,y_predict)
print precision,recall,f1,auc
print fake_reviewer,true_reviewer



