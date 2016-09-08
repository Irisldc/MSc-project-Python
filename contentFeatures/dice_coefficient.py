import nltk,re
from nltk import ngrams


def getNgram(str, n):
    tokenized = re.split(r'[^\w]+', str)
    ngram = ngrams(tokenized, n)

    return set(ngram)

def computeDice(set1, set2):

    intersection=set1 & set2
    print str(len(intersection))
    sum=len(set1)+len(set2)

    print 'sum='+str(sum)
    dice=(float(2*len(intersection)))/(sum)

    return dice

str1='Happy, Elegant, Modern, Perfect'
str2='Beautiful, Elegant, Modern'

set1=getNgram(str1, 1)
set2=getNgram(str2, 1)

print set1
print set2

dice=computeDice(set1, set2)

print 'dice coefficient='+str(dice)
