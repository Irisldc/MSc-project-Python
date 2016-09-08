origin_file=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/A.Mukherjee_Amazon/reviewsNew.txt','r')
spam_list=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/A.Mukherjee_Amazon/reviewer_spamicity.txt','r')
#spam_list=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/A.Mukherjee_Amazon/labelled_users_reviewed_items.txt','r')
#info_list=open('reviwer_info_list.txt','w')
info_list=open('item_info.txt','w')

authors=[]

for line in spam_list:
    items=line.split(':')
    authors.append(items[0])

print 'num of individual spammers:'+str(len(authors))

print 'start'

record=0
s=set()

for line in origin_file:
    items=line.split('\t')
    author=items[0]
    #item=items[1]
    print author
    if author in authors:
        s.add(author)
        info_list.write(line)
        record+=1

print 'complete. num of records found:'+str(record)
print 'num of individual spammer found:'+str(len(s))




