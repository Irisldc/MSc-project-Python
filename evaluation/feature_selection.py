from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn import preprocessing
import numpy as np
from numpy import array
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFE
from scipy.stats import pearsonr
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import f_regression
import copy
from minepy import MINE

# #logistic regression
# logreg=linear_model.LogisticRegression()
#
# #naive bayes classifier
# classifier_NB=GaussianNB()
#
# #support vector machine
# classifier_SVM=svm.SVC(kernel='linear')

#dat&feature file
#data=open('/Users/lidongchen/PycharmProjects/MSc_project/reviewer_features_no_network.csv','r')
data=open('/Users/lidongchen/PycharmProjects/MSc_project/reviewer_features.csv','r')
all_preprocessed_features=open('all_preprocessed_features.txt','w')

feature_selected_by_GBDT=open('feature_selected_by_GBDT.txt','w')
feature_selected_by_ETC=open('feature_selected_by_ETC.txt','w')
feature_importance_by_ETC_file=open('feature_importance_by_ETC.txt','w')

feature_selected_by_l1_lr=open('feature_selected_by_l1_lr.txt','w')
#feature_selected_by_l1_NB=open('feature_selected_by_l1_NB.txt','w')
feature_selected_by_l1_SVM=open('feature_selected_by_l1_SVM.txt','w')

feature_selected_by_RFE_lr=open('feature_selected_by_RFE_lr.txt','w')
feature_selected_by_RFE_NB=open('feature_selected_by_RFE_NB.txt','w')
feature_selected_by_RFE_SVM=open('feature_selected_by_RFE_SVM.txt','w')

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

        X.append(x_list)
        y=float(info_list[-1])
        Y.append(y)
        #print x_list,info_list[-1]
        line_num+=1

# temp_X=copy.copy(X)
# temp_Y=copy.copy(Y)
#
# #copy data 4 times
# for j in range(0,4):
#     X.extend(temp_X)
#     Y.extend(temp_Y)
#     #print len(X),len(Y)

print len(X),len(Y)

#shuffle data
#data pre-processing
#X=normalize(X,norm='l2')
X=np.array(X)
#X=preprocessing.scale(X)
scaler= preprocessing.StandardScaler().fit(X)
X=scaler.transform(X)
Y=np.array(Y)

for x in X:
    all_preprocessed_features.write(str(x)+'\n')
#print X

# # model training
# logreg.fit(X, Y)
# classifier_NB.fit(X, Y)
# classifier_SVM.fit(X, Y)

#select features by GBDT
clf_GBDT=GradientBoostingClassifier()
d_GBDT={}

print 'average feature importance by GBDT:'
for i in range(0,10):
    x_new_select_by_GBDT=clf_GBDT.fit(X,Y).transform(X)
    feature_importance_by_GBDT=clf_GBDT.feature_importances_
    for j in range(len(feature_importance_by_GBDT)):
        if j in d_GBDT.keys():
            s=d_GBDT[j]
            s+=feature_importance_by_GBDT[j]
            d_GBDT[j]=s
        else:
            d_GBDT[j]=feature_importance_by_GBDT[j]

for key in d_GBDT.keys():
    avg_s=float(d_GBDT[key])/10
    print key,avg_s
sort_feature_by_GBDT=sorted(feature_importance_by_GBDT,reverse=True)
print 'feature importance by GBDT:', feature_importance_by_GBDT,sort_feature_by_GBDT
# x_new_select_by_tree=SelectFromModel(GradientBoostingClassifier()).fit_transform(X,Y)
# print 'feature selected by GBDT:',x_new_select_by_tree
# for x in x_new_select_by_tree:
#     feature_selected_by_GBDT.write(str(x)+'\n')

# select features by extratrees
clf_ECT=ExtraTreesClassifier()
d_ECT={}

print 'average feature importance by extra tree:'
for i in range(0,10):
    x_new_select_by_ETC=clf_ECT.fit(X,Y).transform(X)
    feature_importance_by_ETC=clf_ECT.feature_importances_
    for j in range(len(feature_importance_by_ETC)):
        if j in d_ECT.keys():
            s=d_ECT[j]
            s+=feature_importance_by_ETC[j]
            d_ECT[j]=s
        else:
            d_ECT[j]=feature_importance_by_ETC[j]

for key in d_ECT.keys():
    avg_s=float(d_ECT[key])/10
    print key, avg_s
# indices = np.argsort(feature_importance_by_ETC)[::-1]
# for f in range(x_new_select_by_ETC.shape[1]):
#     print("%d. feature %d (%f)" % (f + 1, indices[f], feature_importance_by_ETC[indices[f]]))
#     feature_importance_by_ETC_file.write("%d. feature %d (%f)" % (f + 1, indices[f], feature_importance_by_ETC[indices[f]])+'\n')
sort_feature_by_ETC=sorted(feature_importance_by_ETC, reverse=True)
print 'feature importance by ECT:',feature_importance_by_ETC, sort_feature_by_ETC

# select features by random forest
clf_random_forest=RandomForestClassifier()
d_rf={}
print 'average feature importance by random forest:'
for i in range(0,10):
    x_new_select_by_rf=clf_random_forest.fit(X,Y).transform(X)
    feature_importance_by_rf=clf_random_forest.feature_importances_
    for j in range(len(feature_importance_by_rf)):
        if j in d_rf.keys():
            s=d_rf[j]
            s+=feature_importance_by_rf[j]
            d_rf[j]=s
        else:
            d_rf[j]=feature_importance_by_rf[j]

for key in d_rf.keys():
    avg_s=float(d_rf[key])/10
    print key, avg_s

print 'feature importance by random forest:',feature_importance_by_rf

# select by l1 penalty
x_new_select_by_l1_lr=SelectFromModel(LogisticRegression(penalty='l1',C=0.1)).fit_transform(X,Y)
print 'feature selected by l1 penalty for logistic regression model:',x_new_select_by_l1_lr, x_new_select_by_l1_lr.shape
for x in x_new_select_by_l1_lr:
    feature_selected_by_l1_lr.write(str(x)+'\n')

# x_new_select_by_l1_NB=SelectFromModel(GaussianNB(penalty='l1',C=0.1)).fit_transform(X,Y)
# print 'feature selected by l1 penalty for Naive Bayes model:',x_new_select_by_l1_NB, x_new_select_by_l1_NB.shape
# for x in x_new_select_by_l1_NB:
#     feature_selected_by_l1_NB.write(str(x)+'\n')

x_new_select_by_l1_SVM=SelectFromModel(LinearSVC(penalty='l1',C=0.01, dual=False)).fit_transform(X,Y)
print 'feature selected by l1 penalty for SVM:',x_new_select_by_l1_SVM, x_new_select_by_l1_SVM.shape
for x in x_new_select_by_l1_SVM:
    feature_selected_by_l1_SVM.write(str(x)+'\n')

#select features by RFE
def select_by_RFE(model,n_of_feature,file):
    x_new_select_by_RFE=RFE(estimator=model, n_features_to_select=n_of_feature).fit_transform(X,Y)
    for x in x_new_select_by_RFE:
        file.write(str(x)+'\n')
    return x_new_select_by_RFE

x_new_select_by_RFE_lr=select_by_RFE(LogisticRegression(),5,feature_selected_by_RFE_lr)
#ref=RFE(estimator=LogisticRegression(),n_features_to_select=5).fit(X,Y)
print 'features selected by REF for logistic regression model',x_new_select_by_RFE_lr, x_new_select_by_RFE_lr.shape
#print 'feature importance by REF for logistic regression model', ref.ranking_
# x_new_select_by_RFE_NB=select_by_RFE(GaussianNB(), 5, feature_selected_by_RFE_NB)
# print 'features selected by REF for Naive Bayes model',x_new_select_by_RFE_NB, x_new_select_by_RFE_NB.shape

x_new_select_by_RFE_SVM=select_by_RFE(LinearSVC(), 5, feature_selected_by_RFE_SVM)
print 'features selected by REF for SVM model',x_new_select_by_RFE_SVM, x_new_select_by_RFE_SVM.shape

#select by chi2
# x_new_chi2=SelectKBest(chi2,k=5).fit_transform(X,Y)
# print 'feature selection by chi2:', x_new_chi2.shape

#select by pearson coefficient
#x_new_select_by_pearson=lambda X, Y: array(map(lambda x:pearsonr(x, Y), X.T)).T
x_new_feature_importance_by_f=f_regression(X,Y)
print 'feature importance by f correlation:',x_new_feature_importance_by_f

x_new_select_by_pearson=SelectKBest(lambda X, Y: array(map(lambda x:pearsonr(x, Y), X.T)).T, k=5).fit_transform(X, Y)
print 'features selected by pearson coefficient:',x_new_select_by_pearson

#select features by Max Information
def mic(x, y):
    m = MINE()
    m.compute_score(x, y)
    return (m.mic(), 0.5)

x_new_select_by_MIC=SelectKBest(lambda X, Y: array(map(lambda x:mic(x, Y), X.T)).T, k=5).fit_transform(X, Y)
print 'features selected by Max Information:', x_new_select_by_MIC
