from pycipher import SimpleSubstitution as SimpleSub
import random
import re
from ngram_score import ngram_score

fitness = ngram_score('english_quadgrams.txt') # load our quadgram statistics

ctext='''KVU HQBINKWALU DNBAURG BWO AU YUGHRCAUY ARCUPLO WG KVU RUWL DNBAURG ZVQGU
UTIRUGGCQDG WG W YUHCBWL WRU HWLHNLWALU AO PCDCKU BUWDG. WLKVQNJV KVU GNAEUHK
QP KVCG IWIUR CG QGKUDGCALO KVU HQBINKWALU DNBAURG. CK CG WLBQGK UFNWLLO
UWGO KQ YUPCDU WDY CDXUGKCJWKU HQBINKWALU PNDHKCQDG QP WD CDKUJRWL XWRCWALU
QR W RUWL QR HQBINKWALU XWRCWALU, HQBINKWALU IRUYCHWKUG, WDY GQ PQRKV. KVU
PNDYWBUDKWL IRQALUBG CDXQLXUY WRU, VQZUXUR, KVU GWBU CD UWHV HWGU, WDY C VWXU
HVQGUD KVU HQBINKWALU DNBAURG PQR UTILCHCK KRUWKBUDK WG CDXQLXCDJ KVU LUWGK
HNBARQNG KUHVDCFNU. C VQIU GVQRKLO KQ JCXU WD WHHQNDK QP KVU RULWKCQDG QP KVU
HQBINKWALU DNBAURG, PNDHKCQDG, WDY GQ PQRKV KQ QDU WDQKVUR. KVCG ZCLL CDHLNYU W
YUXULQIBUDK QP KVU KVUQRO QP PNDHKCQDG QP W RUWL XWRCWALU UTIRUGGUY CD KURBG
QP HQBINKWALU DNBAURG. WHHQRYCDJ KQ BO YUPCDCKCQD, W DNBAUR CG HQBINKWALU
CP CKG YUHCBWL HWD AU ZRCKKUD YQZD AO W BWHVCDU. C JCXU GQBU WRJNBUDKG ZCKV
KVU CDKUDKCQD QP GVQZCDJ KVWK KVU HQBINKWALU DNBAURG CDHLNYU WLL DNBAURG
ZVCHV HQNLY DWKNRWLLO AU RUJWRYUY WG HQBINKWALU. CD IWRKCHNLWR, C GVQZ KVWK
HURKWCD LWRJU HLWGGUG QP DNBAURG WRU HQBINKWALU. KVUO CDHLNYU, PQR CDGKWDHU,
KVU RUWL IWRKG QP WLL WLJUARWCH DNBAURG, KVU RUWL IWRKG QP KVU MURQG QP KVU
AUGGUL PNDHKCQDG, KVU DNBAURG IC, U, UKH. KVU HQBINKWALU DNBAURG YQ DQK,
VQZUXUR, CDHLNYU WLL YUPCDWALU DNBAURG, WDY WD UTWBILU CG JCXUD QP W YUPCDWALU
DNBAUR ZVCHV CG DQK HQBINKWALU. WLKVQNJV KVU HLWGG QP HQBINKWALU DNBAURG
CG GQ JRUWK, WDY CD BWDO ZWOG GCBCLWR KQ KVU HLWGG QP RUWL DNBAURG, CK CG
DUXURKVULUGG UDNBURWALU. C UTWBCDU HURKWCD WRJNBUDKG ZVCHV ZQNLY GUUB KQ IRQXU
KVU HQDKRWRO. AO KVU HQRRUHK WIILCHWKCQD QP QDU QP KVUGU WRJNBUDKG, HQDHLNGCQDG
WRU RUWHVUY ZVCHV WRU GNIURPCHCWLLO GCBCLWR KQ KVQGU QP JQYUL. KVUGU RUGNLKG
VWXU XWLNWALU WIILCHWKCQDG. CD IWRKCHNLWR, CK CG GVQZD KVWK KVU VCLAURKCWD
UDKGHVUCYNDJGIRQALUB HWD VWXU DQ GQLNKCQD.
'''
ctext = re.sub('[^A-Z]','',ctext.upper())

maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
maxscore = -99e9
parentscore,parentkey = maxscore,maxkey[:]
print ("Substitution Cipher solver, you may have to wait several iterations")
print ("for the correct result.")
# keep going until we are killed by the user
i = 0
while 1:
    i = i+1
    random.shuffle(parentkey)
    deciphered = SimpleSub(parentkey).decipher(ctext)
    parentscore = fitness.score(deciphered)
    if (parentscore > maxscore):
        count = 0
        while count < 1000:
            a = random.randint(0,25)
            b = random.randint(0,25)
            child = parentkey[:]
            # swap two characters in the child
            child[a],child[b] = child[b],child[a]
            deciphered = SimpleSub(child).decipher(ctext)
            score = fitness.score(deciphered)
            # if the child was better, replace the parent with it
            if score > parentscore:
                parentscore = score
                parentkey = child[:]
                count = 0
            count = count+1
        # keep track of best score seen so far
        if parentscore>maxscore:
            maxscore,maxkey = parentscore,parentkey[:]
            print ('\nbest score so far: ', maxscore, 'on iteration ', i)
            ss = SimpleSub(maxkey)
            print ('    best key: '+''.join(maxkey))
            print ('    plaintext: '+ss.decipher(ctext))
    else:
        break

