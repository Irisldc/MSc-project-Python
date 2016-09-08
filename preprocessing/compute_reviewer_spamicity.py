raw_file=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/reviewer_spamicity_raw.txt','r')
reviewer_spamicity=open('./reviewer_spamicity.txt','w')

lineNum=0
spam=0
non_spam=0

for line in raw_file:
    lineNum+=1

    tokens=line.strip().split('\t')

    reviewer=tokens[0]
    scores=tokens[1].strip().split(',')

    sum=0
    cnt=0
    for s in scores:
        if s:
            sum+=float(s)
            cnt+=1

    avg=float(sum/cnt)
    if avg>=0.5:
        spam+=1
    else:
        non_spam+=1

    reviewer_spamicity.write(reviewer+':'+str(avg)+'\n')

print 'complete. num of spammer:'+str(spam)+' num of non-spammer:'+str(non_spam)