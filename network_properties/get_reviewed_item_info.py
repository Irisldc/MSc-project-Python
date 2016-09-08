all_info=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/A.Mukherjee_Amazon/reviewsNew.txt','r')
labelled_reviewer_info=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/A.Mukherjee_Amazon/reviewer_spamicity.txt','r')
labelled_item_info=open('labelled_item_info_raw.txt','w')

labelled_reviewers=[]
for l in labelled_reviewer_info:
    author,score=l.split(':')

    labelled_reviewers.append(author)

print labelled_reviewers

for line in all_info:

    info_list=line.rstrip().split('\t')
    info_list=filter(None,info_list)

    author=info_list[0]
    #print author

    if author in labelled_reviewers:
        labelled_item_info.write(line)
        print 1