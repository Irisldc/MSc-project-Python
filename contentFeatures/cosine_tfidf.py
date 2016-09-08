from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy import spatial
import itertools

def combine2elements(list):
    return itertools.combinations(list, 2)

reviewer_summary = open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_summary.txt','r')
reviewer_summary_tfidfcos=open('reviewer_summary_tfidfcos.txt','w')

for line in reviewer_summary:
    author, summary=line.rstrip().split('\t')
    documents=summary.split('///')
    #stopWords=stopwords.words('english')
    #vectorizer = CountVectorizer(stop_words = stopWords)
    #transformer = TfidfTransformer()
    documents=filter(None, documents)
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents).toarray()
    #print tfidf_matrix

    combined_list=combine2elements(tfidf_matrix)
    #print cosine_similarity(tfidf_matrix[0:1],tfidf_matrix)

    cnt=0
    total_cos=0
    for c in combined_list:
        #tfidf_cosine = 1-spatial.distance.cosine(c[0], c[1])
        tfidf_cosine=cosine_similarity(c[0], c[1])
        cnt+=1
        total_cos+=tfidf_cosine

    avg_tfidfcos=float(total_cos)/cnt

    reviewer_summary_tfidfcos.write(author+'\t'+str(avg_tfidfcos)+'\n')

print 'complete'