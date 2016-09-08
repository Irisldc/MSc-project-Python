import re,math
from collections import Counter
import itertools

word=re.compile(r'\w+')

def combine2elements(list):
    return itertools.combinations(list,2)

def string_to_vector(str):
    words=word.findall(str)
    #print words
    return Counter(words)


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

reviewer_file=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_summary.txt','r')
reviewer_summary_duplicate=open('reviewer_summary_cosine.txt','w')
#record=open('record.txt','w')

for line in reviewer_file:
    author,summaries=line.rstrip().split('\t')
    summary_list=summaries.split('///')
    summary_list=filter(None, summary_list)
    combined_list=combine2elements(summary_list)

    #print author + ':' +str(len(summary_list))
    #record.write(author + ':' +str(len(summary_list))+'\n')

    cnt=0
    cos_sum=0
    for c in combined_list:
        vec1=string_to_vector(c[0])
        vec2=string_to_vector(c[1])
        cos=get_cosine(vec1, vec2)

        #print c[0]+','+c[1]+':'+str(cos)
        #record.write(c[0]+','+c[1]+':'+str(cos)+'\n')
        cos_sum+=cos
        cnt+=1

    cos_avg=float(cos_sum)/cnt
    reviewer_summary_duplicate.write(author+'\t'+str(cos_avg)+'\n')

# str1='Happy, Elegant, Modern, Perfect'
# str2='Beautiful, Elegant, Modern'
#
# vec1=string_to_vector(str1)
# vec2=string_to_vector(str2)
#
# print 'cosine similarity='+str(get_cosine(vec1,vec2))