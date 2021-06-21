from re import sub

chiffres = ['','un','deux','trois','quatre','cinq','six','sept','huit','neuf','dix','onze','douze','treize','quatorze','quinze','seize','dix-sept','dix-huit','dix-neuf']
nombres = ['','dix','vingt','trente','quarante','cinquante','soixante','soixante','quatre-vingt','quatre-vingt']

def formater(x):
    if type(x)==str:
        if ',' in x and len(x.split(',')[1])==3:
            x=x.replace(',','')
        elif ',' in x:
            x=x.replace(',','.')
        x=sub(r'\s*[a-zA-Z]*','',x)
    x=round(float(x),2)
    return str(x)

def unite(x):
    if len(str(x))==3:
        x = str(x)
    elif len(str(x))==2:
        x= '0'+str(x)
    elif len(str(x)) ==1:
        x = '00'+str(x)
    else:
        return ''

    if int(x[-2:])<20:
        dizaines = chiffres[int(x[-2:])]
    elif int(x[-2:]) in [21,31,41,51,61]:
        dizaines = nombres[int(x[-2])]+' et un'
    elif int(x[-2:]) == 71:
        dizaines = 'soixante et onze'
	
    elif int(x[-2]) in [7,9]:
        dizaines = nombres[int(x[-2])]+'-'+chiffres[int(x[-1])+10]
    elif int(x[-1])==0:
        dizaines = nombres[int(x[-2])]
    else:
        dizaines = nombres[int(x[-2])]+'-'+chiffres[int(x[-1])]

    if x[0] == '0':
        return dizaines
    else:
        if x[0] == '1':
            centaines = 'cent'
        elif x[0] =='0':
            centaines = ''
        else:
            centaines = chiffres[int(x[0])]+' cent'
        if dizaines!='':
            centaines+=' '
        return centaines+dizaines

def nombre2lettres(x):    
    if len(x)<=3:
        total = unite(x)
    else:
        milliards, millions, milliers = '','',''
        sp,sp2,sp3='','',''
        if unite(x[-3:]) != '':
            sp= ' '
        if unite(x[-6:-3]) != '' and (unite(x[-6:-3]) != 'un' or len(x)>6):
            sp2 = ' '
        if unite(x[-9:-6]) != '' and (unite(x[-9:-6]) != 'un' or len(x)>9):
            sp3 = ' '
	
	#MILLIERS
        if unite(x[-6:-3]) == 'un':
            milliers = 'mille'+sp+unite(x[-3:])
        elif x[-6:-3] == '000':
            milliers = ''
        else:
            milliers = unite(x[-6:-3])+' mille'+sp+unite(x[-3:])
        
	#MILLIONS
        if len(x)>6:
            if unite(x[-9:-6]) == 'un':
                millions = 'un million'
            elif x[-9:-6] == '000':
                millions = ''
            else:
                millions = unite(x[-9:-6])+' millions'	    
	
	#MILLIARDS
        if len(x)>9:
            if unite(x[-12:-9]) == 'un':
                milliards = 'un milliard'
            elif x[-12:-9] == '000' or len(x)>12:
                milliards = 'plus de mille milliards'
            else:
                milliards = unite(x[-12:-9])+' milliards'
	
	#TOTAL	
        total=milliards+sp3+millions+sp2+milliers

    if total[-4:] in ['cent','ingt'] and len(total)>5 and str(x)[-2:]!='20':
        total += 's'
    return total

def conv(x):
    x=formater(x)    
    e,c = x.split('.')[0],x.split('.')[1]
    if len(c)==1:
        c=c+'0'
    if int(c)==0:
        c=''
    elif int(c)==1:
        c='un centime'
    else:
        c=nombre2lettres(c)+' centimes'
    if int(e)==0:
        if c=='':
            return 'zéro euro'
        else:
            return c
    elif int(e)==1:
        e='un euro'
    elif len(e)>6 and (e[-6:]=='000000' or e[-12:-9] == '000' or len(e)>12):
        e=nombre2lettres(e)+" d'euros"
    else:
        e=nombre2lettres(e)+' euros'
    if c=='':
        return e
    else:
        return e+' et '+c

if __name__ == '__main__':
	result=conv(str(input('Saisissez la somme en chiffres  :')))
	print(result)
