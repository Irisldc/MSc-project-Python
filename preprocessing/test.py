import datetime,re
import itertools
# info_list=open('/Users/lidongchen/Documents/UCL/MSc_project/Dataset/A.Mukherjee_Amazon/spam_list.txt','r')
#
# for line in info_list:
#     items=line.split('\t')
#     print line
#     print len(items)
# str='B0000936M4	A37JD084TMM4FS;April 18, 2005;5.0|AH0DAW8CWAI0N;December 7, 2004;5.0|A2K16UBVDI236Z;February 3, 2005;5.0|A3GXK6NNRHEKKL;September 2, 2004;5.0|A3130MWD7ATB3C;November 5, 2003;4.0|AO3OIPX7RQ4KD;November 9, 2003;5.0|AJXCRMUKON1V9;August 14, 2003;1.0|A33TK2Q851W6UQ;March 17, 2004;5.0|A2GVQASGDS2MUK;November 12, 2003;5.0|A1U0NA8DWILJR6;September 1, 2005;4.0|ABCKXUPFP5LI0;February 11, 2004;4.0|A17WHBI7921035;March 11, 2004;2.0|A6MCU78WCQL9G;March 17, 2004;5.0|A1PRJKOYX5X95E;March 26, 2005;1.0|A1EIOM9O3F17UB;May 13, 2005;4.0|A1N27CNXC9VB2C;September 18, 2003;5.0|A2951WH7XHT49C;December 20, 2003;4.0|A2951WH7XHT49C;December 20, 2003;4.0|A2U2YMF0NTBP6C;January 31, 2004;5.0|A1Q18Z9DBFPYVT;September 18, 2004;5.0|A1L3KPFP117W8V;December 7, 2003;5.0|AYNS6Y6J7GK21;March 9, 2005;5.0|A1T7LZZGBVB9WE;June 12, 2005;5.0|A22JURDDGFT7GO;August 4, 2005;5.0|AMVLW7DC4VPDF;August 5, 2005;5.0|A204DIATWVZMWF;July 19, 2005;5.0|A1GWZBP7Z4PFY3;March 23, 2006;3.0|A29ZL8H327DH9I;March 23, 2004;4.0|A3LT5MUZPG76AX;January 17, 2006;5.0|A1NVBNNVZJ5N7S;June 16, 2005;5.0|A37S7VVLH874WY;September 3, 2005;4.0|A33ZEHMT9O58VE;January 3, 2004;3.0|A16SH5Z08U9F2F;July 27, 2005;5.0|A31SUKGF9BKA2G;December 16, 2004;5.0|APMMTNJOIBBZI;December 27, 2004;3.0|A2FXYMICJ0SAR3;August 16, 2005;5.0|A281GRGHU3NOCT;March 18, 2005;5.0|A12R3H910KO8Z7;September 20, 2005;5.0|A1JCE99BYXBSRE;June 29, 2005;5.0|A3E9QV7M5M8LMP;November 26, 2004;5.0|AY3U4UMSP4AUO;March 20, 2005;5.0|AMBEVM7COHAV7;August 18, 2003;5.0|A1H041RH28P70T;January 18, 2005;5.0|ADEP68XDMG1UG;January 23, 2004;5.0|A358Z4ZFY9IW4X;February 7, 2004;2.0|A2ALJTZ349G4J5;September 10, 2004;5.0|A3AS19MKY0IN7J;March 20, 2006;4.0|A1OZF769Y9S4Y5;April 2, 2006;1.0|A201DYB226RBWW;April 23, 2006;5.0|A179ZBX92TMRA9;January 29, 2006;5.0|AA9H1Q443E1PR;January 11, 2006;5.0|A18GCPWNDNAUZ;February 10, 2006;5.0|A3IM7NO12RAVZ5;February 4, 2004;5.0|A1J83X0PIELMHJ;January 24, 2006;5.0|A5NWAGGSDSZXP;July 4, 2005;1.0|A20A4TBYA9M1V6;August 29, 2005;3.0|A2TFNZYBBET7NW;January 29, 2006;5.0|A3TGU503T36P2;September 4, 2005;5.0|A2IIQ1N3HZ52SB;September 16, 2005;5.0|AB7YTSWKLROKD;October 18, 2005;5.0|A2M9107JC8URRC;January 18, 2006;5.0|A2NY6RUUUPK7ZL;May 21, 2005;5.0|A2Y1UTAMTXEQFT;February 3, 2005;5.0|A2XHZ7VYREN2DT;January 18, 2006;4.0|A27X79CCRVDXCQ;February 6, 2005;5.0|A1SH2M0LXT323;November 1, 2005;3.0|ADFRDFLRH3NL5;March 11, 2004;5.0|AMQZ92VH5W6N2;June 21, 2005;4.0|A1BGY6CNHYVLJO;September 24, 2005;4.0|A7GB9IYQNNF2T;September 19, 2003;5.0|A3UYX588IJKPB8;July 21, 2004;5.0|A3QLQXB8792YTM;March 14, 2004;3.0|A18A4K754R6RQR;March 9, 2005;4.0|AJGF1C6A6P8JP;December 27, 2005;5.0|A181XY4FUF2B7;January 3, 2004;5.0|AI6X25RRJ0F1O;July 17, 2005;4.0|A1IKU0IXTQ8I96;May 3, 2005;5.0|A3O5C9QBDX96T2;March 20, 2004;5.0|A2Y7O6SYH62N19;December 5, 2005;4.0|A2QWPC3DJ9BHEA;November 6, 2003;5.0|A2ZM657UCAK5PI;July 7, 2004;5.0|AMXCZ75YRWJDQ;September 25, 2004;4.0|A7YT298UY8GEP;February 17, 2004;5.0|A2PSP4VA2GXWB4;September 11, 2003;5.0|AE6478EA734U7;October 9, 2003;5.0|AKKP6JQ5IB9QU;September 13, 2004;5.0|A4YQI5Y1TCHRH;November 30, 2004;5.0|AR3L20G9YRQ0U;May 5, 2004;5.0|A26PP5GR94VX8P;January 7, 2004;4.0|A1RMKT5QBZRW3Z;May 19, 2004;5.0|A1PNWVK086EE2Y;February 11, 2006;5.0|A2GR3PXCASFYLC;December 9, 2005;2.0|A2Y36RG7DE4WGY;March 19, 2006;5.0|A1E8TN32HTXS3X;October 11, 2004;5.0|AE5WZV6XDYEZ8;February 25, 2006;2.0|A12EW84YK6IHM1;January 15, 2006;5.0|A1IQ8K59NZV8VM;January 4, 2006;5.0|AT59PGXS9627Q;April 22, 2006;5.0|A1KXTQ9QENYF4B;January 11, 2006;4.0|AK06ZEWC5CY09;February 23, 2006;5.0|A3EDM0TL47QTIM;August 28, 2005;5.0|A2IU1V6S3IU5B8;March 8, 2005;5.0|ASGI7E0AJ8H5X;January 13, 2005;5.0|ALAA8BMM3OIN0;August 20, 2005;5.0|A3E24FMSXLZEEG;May 23, 2004;1.0|A3C7MGYLZ7REYL;December 21, 2005;5.0|A18I5YUB8DA136;October 26, 2005;2.0|A243NDFBFTC1PF;November 11, 2005;4.0|A3E5FPO13BD8A7;March 23, 2005;5.0|ABKKIDW0UJCTH;June 25, 2005;5.0|A2Q7MORC9DD0RC;September 29, 2005;5.0|AAEDI63SPD3PU;February 21, 2004;5.0|A2QS3B1XF7UJT;September 25, 2004;5.0|A2E6QLYUC96ZZN;June 28, 2004;5.0|A17VIBT0O9LTPO;June 23, 2005;5.0|A2N8T0T055KEI7;July 20, 2005;4.0|A1JCV0XY64TZDJ;September 8, 2005;3.0|A3CHLN3U1QC4BT;October 21, 2005;1.0|A1KK73NQV8Z8TM;March 9, 2005;5.0|ADGT56CC67RZ0;February 23, 2005;1.0|A2F16DVDT9K81W;March 31, 2004;4.0|AWK3IB8VKXJ3O;April 24, 2005;3.0|A161VMTK5O0I53; 23, 2005;5.0|A255492H8X3DHK;September 9, 2005;2.0|A12DIOU00CECU;July 5, 2005;3.0|A23KQQEINDCL6;August 26, 2003;4.0|A1YQ8GSSOK6FMD;May 10, 2005;5.0|AVZ9K17APXRAB;February 26, 2005;1.0|AXJO9LCW46IYN;March 4, 2005;5.0|A2JP6EIVSGRB22;February 2, 2005;5.0|A2EK5O0F1YVZRO;October 11, 2004;5.0|A3LROLDR8SCLZA;December 2, 2004;5.0|A1Y1LOYGMNDNYB;May 31, 2004;5.0|A1OUC50VY27QV0;November 4, 2005;5.0|A1WO1FJB7CBXCL;July 27, 2005;5.0|A1ZW790PXFRCNF;July 1, 2005;5.0|A27ZKKNRUQHGED;August 13, 2005;5.0|'
# info=str.split('|')
#
# for i in info:
#     info_list=i.split(';')
#
#     temp_list=re.split(r'[,\s]+', info_list[1])
#
#     print info_list[1]
#
#     if len(temp_list)>2:
#
#         month=temp_list[0]
#         #print month
#
#         if month=='January':
#             month = '01'
#         if month == 'February':
#             month = '02'
#         if month == 'March':
#             month = '03'
#         if month == 'April':
#             month = '04'
#         if month == 'May':
#             month = '05'
#         if month == 'June':
#             month = '06'
#         if month == 'July':
#             month = '07'
#         if month == 'August':
#             month = '08'
#         if month == 'September':
#             month = '09'
#         if month == 'October':
#             month = '10'
#         if month == 'November':
#             month = '11'
#         if month == 'December':
#             month = '12'
#
#         day=temp_list[1]
#         year=temp_list[2]
#         date=year+'-'+month+'-'+day
#
#         print date
#print (datetime.date.today()+datetime.timedelta(365/12)).isoformat()

l=['hello', 'thanks', 'bye']

combined_list=itertools.combinations(l,2)

for c in combined_list:
    print c