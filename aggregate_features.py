
def getFeatures(path):

    file=open(path,'r')
    d={}
    for line in file:
        author,feature=line.rstrip().split('\t')
        d[author]=feature

    return d

#timely behaviours
timely_path='/Users/lidongchen/PycharmProjects/MSc_project/timely_behaviours/'
early_review_ratio=timely_path+'reviewer_early_ratio.txt'
life_time=timely_path+'reviewer_life_time.txt'
max_numOf_reviews_daily=timely_path+'max_numOf_reviews_daily.txt'

#rating behaviours
rating_path='/Users/lidongchen/PycharmProjects/MSc_project/rating_behaviours/'
rating_distribution=rating_path+'reviewer_rating_distribution.txt'
repeated_rating=rating_path+'reviewer_repeated_rating.txt'

#content duplicate
content_path='/Users/lidongchen/PycharmProjects/MSc_project/contentFeatures/'
#tfidf cosine similarity
summary_duplicate=content_path+'reviewer_summary_tfidfcos.txt'
#summary_duplicate=content_path+'reviewer_summary_cosine.txt'

#network properties
network_path='/Users/lidongchen/PycharmProjects/MSc_project/network_properties/'
#helpfulness_score=network_path+'reviewer_helpfulness_ratio_norm.txt'
helpfulness_score=network_path+'reviewer_helpfulness_weight.txt'
rating_deviation_ratio=network_path+'reviewer_rating_deviation_ratio.txt'

#network projection
projection_path='/Users/lidongchen/PycharmProjects/MSc_project/network_projection/'
cc=projection_path+'reviewer_simple_weighted_projection_cc.txt'
bc=projection_path+'reviewer_simple_weighted_projection_bc.txt'
degree=projection_path+'reviewer_simple_weighted_projection_degree.txt'
#features_dic={}

true_reviewer_spamicity=open('/Users/lidongchen/Documents/workspace/MapReduceAssignment/reviewer_spamicity.txt','r')
#true_reviewer_spamicity_dic=getFeatures(true_reviewer_spamicity)

true_reviewer_labels={}

for line in true_reviewer_spamicity:

    author,spamicity=line.rstrip().split(':')
    spamicity=float(spamicity)
    # if spamicity <= 0.4:
    #     label = -1
    # elif spamicity > 0.4 and spamicity < 0.7:
    #     label = 0
    # elif spamicity >= 0.7:
    #     label = 1

    if spamicity<0.5:
        label=0
    else:
        label=1

    true_reviewer_labels[author]=label

early_review_ratio_dic=getFeatures(early_review_ratio)
life_time_dic=getFeatures(life_time)
max_numOf_reviews_daily_dic=getFeatures(max_numOf_reviews_daily)

rating_distribution_dic=getFeatures(rating_distribution)
repeated_rating_dic=getFeatures(repeated_rating)

summary_duplicate_dic=getFeatures(summary_duplicate)

helpfulness_score_dic=getFeatures(helpfulness_score)
rating_deviation_ratio_dic=getFeatures(rating_deviation_ratio)

cc_dic=getFeatures(cc)
bc_dic=getFeatures(bc)
degree_dic=getFeatures(degree)

reviewer_features=open('reviewer_features.csv','w')
reviewer_features.header=('id,life_time,max_numOf_reviews_daily,early_review_ratio,rating_distribution,'
                        'repeated_rating,review_summary_duplicate,helpfulness_score,rating_deviation,'
                        'clustering_coefficient,betweeness,degree,label'+'\n')
for key in life_time_dic.keys():

    s=life_time_dic[key]+','+max_numOf_reviews_daily_dic[key]+','+early_review_ratio_dic[key]\
      +','+rating_distribution_dic[key]+','+repeated_rating_dic[key]+','+summary_duplicate_dic[key]\
      +','+helpfulness_score_dic[key]+','+rating_deviation_ratio_dic[key]+','+cc_dic[key]+','+bc_dic[key]\
      +','+degree_dic[key]+','+str(true_reviewer_labels[key])
    reviewer_features.write(key+','+s+'\n')
