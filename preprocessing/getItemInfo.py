origin_file=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/A.Mukherjee_Amazon/reviewsNew.txt','r')

labelled_item_list=open('/Users/lidongchen/PycharmProjects/MSc_project/preprocessing/item_info.txt','r')
item_info_full=open('item_info_all.txt','w')

item_set=set()

for l in labelled_item_list:

    record_list=l.split('\t')
    item=record_list[1]

    item_set.add(item)

print 'num of item been reviewed='+str(len(item_set))

record_count=0

for line in origin_file:
    records=line.split('\t')
    item_name=records[1]

    if item_name in item_set:
        item_info_full.write(line)
        record_count+=1

print 'num of records found='+str(record_count)