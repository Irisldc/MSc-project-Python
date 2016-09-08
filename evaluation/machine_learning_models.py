from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import svm,grid_search
from sklearn.cross_validation import KFold
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn import preprocessing
from sklearn.feature_selection import SelectFromModel
import numpy as np
import copy
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

#logistic regression
parameters_lr={'C':[0.001,0.01,0.1,1,10,100,1000]}
logreg=grid_search.GridSearchCV(LogisticRegression(penalty='l2'), parameters_lr)

#naive bayes classifier
classifier_NB=GaussianNB()

#support vector machine
parameters_svm = {'kernel':('linear', 'rbf'), 'C':[1,10,100,1000],'gamma':[0.0001,0.001,0.01]}
classifier_SVM=grid_search.GridSearchCV(svm.SVC(), parameters_svm)

#boosting tree
classifier_GBDT=GradientBoostingClassifier()

#dat&feature file
data=open('/Users/lidongchen/PycharmProjects/MSc_project/reviewer_features.csv','r')
#data=open('/Users/lidongchen/PycharmProjects/MSc_project/reviewer_features_no_network.csv','r')
#data=pd.read_csv('/Users/lidongchen/PycharmProjects/MSc_project/reviewer_features.csv',header=0,skiprows=1,names=['id','degree','life_time','betweeness','helpfulness_score','clustering_coefficient','label'])
X=[]
Y=[]
line_num = 0

for line in data:

    if line_num==0:
        line_num+=1
        continue
    else:
        x_list=[]
        info_list=line.rstrip().split(',')
        info_list=filter(None,info_list)

        author=info_list[0]
        for i in range(1,len(info_list)-1):
            f=float(info_list[i])
            x_list.append(f)
        #1:life time; 3:early review ratio; 4:rating distribution;
        # 6: review summary duplicate; 7: helpfulness; 8: rating deviation;
        # 9: cc; 10:betweeness; 11:degree
            #feature selection by boosting tree: with social features
            #if i==1 or i==7  or i==9 or i==10 or i==11:
            # feature selection by boosting tree: no social features
            #if i == 1 or i == 6 or i == 4 or,, i == 8:
            # feature selection by extra tree: with social features
            #if i==1 or i==3 or i==6 or i==8 or i ==9 or i==11:
            # feature selection by extra tree: no social features
            #if i==6 or i==8 or i==7 or i==3:
            # feature selection by random forest: with social
            #if i==11 or i==10 or i==6 or i==8 or i==
            # feature selected by pearson correlation
            #if i==1 or i==3 or i==4 or i==6 or i==8:
            #feature selected by Max Information
            #if i==6 or i==8 or i==9 or i==10 or i==11:
            # feature selection by RFE for lr
            # if i==3 or i==4 or i==5 or i==6 or i==11:
            # feature selection by RFE for SVM
            #if i==3 or i==4 or i==5 or i==10 or i==11:
                # f=float(info_list[i])
                # x_list.append(f)

        #x_list=normalize(x_list, norm='l2')
        X.append(x_list)
        y=float(info_list[-1])
        Y.append(y)
        #print x_list,info_list[-1]
        line_num+=1


#X=normalize(X,norm='l2')

temp_X=copy.copy(X)
temp_Y=copy.copy(Y)
#print len(temp_X),len(temp_Y)

#copy data 4 times
for j in range(0,4):
    X.extend(temp_X)
    Y.extend(temp_Y)
    #print len(X),len(Y)

print len(X),len(Y)
X=np.array(X)
#X=normalize(X,norm='l2')
#data pre-processing
scaler= preprocessing.StandardScaler().fit(X)
X=scaler.transform(X)
#X=preprocessing.scale(X)
#X=preprocessing.Normalizer().fit_transform(X)
print X
Y=np.array(Y)
#print X,Y

k=5
kf=KFold(n=4130, n_folds=k, shuffle=True)

t_p_lr=0
t_r_lr=0
t_f1_lr=0
t_auc_lr=0

t_p_NB=0
t_r_NB=0
t_f1_NB=0
t_auc_NB=0

t_p_SVM=0
t_r_SVM=0
t_f1_SVM=0
t_auc_SVM=0

t_p_GBDT=0
t_r_GBDT=0
t_f1_GBDT=0
t_auc_GBDT=0

for i in range(0,10):

    print 'k-fold test round: '+str(i)

    total_precision_lr = 0
    total_recall_lr = 0
    total_f1_lr = 0
    total_auc_lr = 0

    total_precision_NB = 0
    total_recall_NB = 0
    total_f1_NB = 0
    total_auc_NB = 0

    total_precision_SVM = 0
    total_recall_SVM = 0
    total_f1_SVM = 0
    total_auc_SVM = 0

    total_precision_GBDT = 0
    total_recall_GBDT = 0
    total_f1_GBDT = 0
    total_auc_GBDT = 0

    f_cnt = 0
    for train_index, test_index in kf:
        f_cnt+=1
        print 'folder '+str(f_cnt)

        X_train, X_test=X[train_index], X[test_index]
        Y_train, Y_test=Y[train_index], Y[test_index]
        print len(X_train)

        #model training
        logreg.fit(X_train, Y_train)
        classifier_NB.fit(X_train, Y_train)
        classifier_SVM.fit(X_train, Y_train)
        classifier_GBDT.fit(X_train, Y_train)

        #feature selection
        # svm_model=SelectFromModel(classifier_SVM,prefit=True)
        # lr_model=SelectFromModel(logreg,prefit=True)
        # X_new_svm=svm_model.transform(X_train)
        # X_new_lr=lr_model.transform(X_train)
        # print 'feature selection from svm:',X_new_svm.shape
        # print 'feature selection from logistic regression:',X_new_lr.shape

        #model prediction
        predicted_lr=logreg.predict(X_test)
        predicted_NB=classifier_NB.predict(X_test)
        predicted_SVM = classifier_SVM.predict(X_test)
        predicted_GBDT=classifier_GBDT.predict(X_test)

        #model evaluation
        recall_lr=recall_score(Y_test,predicted_lr,average='binary')
        precision_lr=precision_score(Y_test,predicted_lr,average='binary')
        f1_lr=f1_score(Y_test,predicted_lr,average='binary')
        auc_lr=roc_auc_score(Y_test,predicted_lr)

        recall_NB = recall_score(Y_test, predicted_NB, average='binary')
        precision_NB = precision_score(Y_test, predicted_NB, average='binary')
        f1_NB = f1_score(Y_test, predicted_NB, average='binary')
        auc_NB = roc_auc_score(Y_test, predicted_NB)

        recall_SVM = recall_score(Y_test, predicted_SVM, average='binary')
        precision_SVM = precision_score(Y_test, predicted_SVM, average='binary')
        f1_SVM = f1_score(Y_test, predicted_SVM, average='binary')
        auc_SVM = roc_auc_score(Y_test, predicted_SVM)

        recall_GBDT = recall_score(Y_test, predicted_GBDT, average='binary')
        precision_GBDT = precision_score(Y_test, predicted_GBDT, average='binary')
        f1_GBDT = f1_score(Y_test, predicted_GBDT, average='binary')
        auc_GBDT = roc_auc_score(Y_test, predicted_GBDT)

        print 'logistic regression:'+str(precision_lr), recall_lr, f1_lr, auc_lr
        print 'naive bayes:'+str(precision_NB), recall_NB, f1_NB, auc_NB
        print 'SVM:' + str(precision_SVM), recall_SVM, f1_SVM, auc_SVM
        print 'GBDT:' + str(precision_GBDT), recall_GBDT, f1_GBDT, auc_GBDT

        total_precision_lr+=precision_lr
        total_recall_lr+=recall_lr
        total_f1_lr+=f1_lr
        total_auc_lr+=auc_lr

        total_precision_NB += precision_NB
        total_recall_NB += recall_NB
        total_f1_NB += f1_NB
        total_auc_NB += auc_NB

        total_precision_SVM += precision_SVM
        total_recall_SVM += recall_SVM
        total_f1_SVM += f1_SVM
        total_auc_SVM += auc_SVM

        total_precision_GBDT += precision_GBDT
        total_recall_GBDT += recall_GBDT
        total_f1_GBDT += f1_GBDT
        total_auc_GBDT += auc_GBDT

    avg_precision_lr=float(total_precision_lr)/k
    avg_recall_lr=float(total_recall_lr)/k
    avg_f1_lr=float(total_f1_lr)/k
    avg_auc_lr=float(total_auc_lr)/k

    avg_precision_NB = float(total_precision_NB) / k
    avg_recall_NB = float(total_recall_NB) / k
    avg_f1_NB = float(total_f1_NB) / k
    avg_auc_NB = float(total_auc_NB) / k

    avg_precision_SVM = float(total_precision_SVM) / k
    avg_recall_SVM = float(total_recall_SVM) / k
    avg_f1_SVM = float(total_f1_SVM) / k
    avg_auc_SVM = float(total_auc_SVM) / k

    avg_precision_GBDT = float(total_precision_GBDT) / k
    avg_recall_GBDT = float(total_recall_GBDT) / k
    avg_f1_GBDT = float(total_f1_GBDT) / k
    avg_auc_GBDT = float(total_auc_GBDT) / k

    print 'Logistic regression avg after k-fold:'+str(avg_precision_lr),avg_recall_lr,avg_f1_lr,avg_auc_lr
    print 'Naive Bayes avg after k-fold:' + str(avg_precision_NB), avg_recall_NB, avg_f1_NB, avg_auc_NB
    print 'SVM avg after k-fold:' + str(avg_precision_SVM), avg_recall_SVM, avg_f1_SVM, avg_auc_SVM
    print 'GBDT avg after k-fold:' + str(avg_precision_GBDT), avg_recall_GBDT, avg_f1_GBDT, avg_auc_GBDT

    t_p_lr+=avg_precision_lr
    t_r_lr+=avg_recall_lr
    t_f1_lr+=avg_f1_lr
    t_auc_lr+=avg_auc_lr

    t_p_NB += avg_precision_NB
    t_r_NB += avg_recall_NB
    t_f1_NB += avg_f1_NB
    t_auc_NB += avg_auc_NB

    t_p_SVM += avg_precision_SVM
    t_r_SVM += avg_recall_SVM
    t_f1_SVM += avg_f1_SVM
    t_auc_SVM += avg_auc_SVM

    t_p_GBDT += avg_precision_GBDT
    t_r_GBDT += avg_recall_GBDT
    t_f1_GBDT += avg_f1_GBDT
    t_auc_GBDT+= avg_auc_GBDT

print 'Logistic Regression final avg:'+str(float(t_p_lr)/10),float(t_r_lr)/10,float(t_f1_lr/10),float(t_auc_lr)/10
print 'Naive Bayes final avg:'+str(float(t_p_NB)/10),float(t_r_NB)/10,float(t_f1_NB/10),float(t_auc_NB)/10
print 'SVM final avg:'+str(float(t_p_SVM)/10),float(t_r_SVM)/10,float(t_f1_SVM/10),float(t_auc_SVM)/10
print 'GBDT final avg:'+str(float(t_p_GBDT)/10),float(t_r_GBDT)/10,float(t_f1_GBDT/10),float(t_auc_GBDT)/10