import itertools
import glob
#find combinations of 2 elements in the list
def combine2elements(list):
    return itertools.combinations(list,2)

def splitFile(file):
    #count the number of lines
    cnt=0
    #store the temp lines: 10 lines
    l_temp = []
    chuck_num=0
    l_all=[]

    for lin in file:
        l_all.append(lin)

    for line in l_all:
        cnt += 1
        l_temp.append(line)

        if cnt%10==0:
            chuck_num=cnt/10
            f=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_body_parts/reviewer_body_part'+str(chuck_num)+'.txt','w')
            for l in l_temp:
                f.write(l)
            l_temp=[]

        elif cnt==len(l_all):
            start_pos=chuck_num*10
            end_pos=len(l_all)
            chuck_num+=1
            f=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_body_parts/reviewer_body_part'+str(chuck_num)+'.txt','w')

            for i in range(start_pos, end_pos):
                f.write(l_all[i])

#the longest common subsequence
def lcs_length(a, b):
    table = [[0] * (len(b) + 1) for _ in xrange(len(a) + 1)]
    for i, ca in enumerate(a, 1):
        for j, cb in enumerate(b, 1):
            table[i][j] = (
                table[i - 1][j - 1] + 1 if ca == cb else
                max(table[i][j - 1], table[i - 1][j]))
    return table[-1][-1]

# the longest common substring
def lcsubstring_length(a, b):
    table = [[0] * (len(b) + 1) for _ in xrange(len(a) + 1)]
    l = 0
    for i, ca in enumerate(a, 1):
        for j, cb in enumerate(b, 1):
            if ca == cb:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > l:
                    l = table[i][j]
    return l

def normalizedLCS(str1, str2,lcs):

    n1=pow(lcs,2)
    n2=len(str1)*len(str2)

    return float(n1)/n2

def writeToFile(num):

    review_body=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_body_parts/reviewer_body_part'+str(num)+'.txt','r')
    #reviewer_body_parts = glob.glob(path + '*.txt')
    reviewer_body_normlcs = open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_body_normlcs/reviewer_body_normlcs_part'+str(num)+'.txt', 'w')

    for line in review_body:

        author,reviews=line.rstrip().split('\t')
        review_list=reviews.split('///')
        review_list = filter(None, review_list)

        print author+':'+str(len(review_list))

        combined_list=combine2elements(review_list)

        cnt=0
        dup=0
        for c in combined_list:

            lcs=lcs_length(c[0], c[1])
            lcstring=lcsubstring_length(c[0], c[1])
            norm_lcs=normalizedLCS(c[0], c[1], lcs)

            cnt+=1
            dup+=norm_lcs

            print c[0]
            print c[1]
            print 'the longest common subsequence length:'+str(lcs)
            print 'the longest common substring length:'+str(lcstring)
            print 'the normalized common subsequence:'+str(norm_lcs)

        avg_dup=float(dup)/cnt
        reviewer_body_normlcs.write(author+'\t'+str(avg_dup)+'\n')

    #print 'the percentage of content similarity:'+str(float(c/(len(str1))))

#review_body=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_body.txt','r')
#record=open('reviewer_body_record.txt','w')
#splitFile(review_body)
# for i in range(12,84):
#     writeToFile(i)
#     print 'complete'+str(i)

writeToFile(12)