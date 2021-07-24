from re import sub

chiffres = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
nombres = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

def formater(x):
    """
    Function to clean up the string input and convert it into a float
    One mandatory arg : int, float, Decimal, or str representing numbers
    """
    if type(x)==str:
        if ',' in x and len(x.split(',')[1])==3:
            x=x.replace(',','')
        elif ',' in x:
            x=x.replace(',','.')
        x=sub(r'\s*[a-zA-Z]*','',x)
    x=round(float(x),2)
    return str(x)

def unite(x):
    """
    Converts x into letters when int(x)<1000
    One mandatory argument : any string input representing an integer < 1000
    """
    x = str(x)
    if len(x)==2:
        x= '0'+x
    elif len(x) ==1:
        x = '00'+x
    elif len(x) !=3:
        return ''

    if int(x[-2:])<20:
        dizaines = chiffres[int(x[-2:])]
    elif int(x[-1])==0:
        dizaines = nombres[int(x[-2])]
    else:
        dizaines = nombres[int(x[-2])]+'-'+chiffres[int(x[-1])]

    if x[0] == '0':
        return dizaines
    else:
        centaines = chiffres[int(x[0])]+' hundred'
        if dizaines!='':
            centaines+=' and '
        return centaines+dizaines

def nombre2lettres(x):
    """
    This function converts an integer into letters.
    It is called twice by conv() : firstly, for the integer part of the input, and secondly for the decimals if there are some.
    """
    x=str(x)
    if len(x)<=3:
        total = unite(x)
    else:
        milliards, millions, milliers = '','',''
        sp,sp2,sp3='','',''
        if unite(x[-3:]) != '':#nécessité d'un espace avant les centaines
            sp= ', '
        if unite(x[-6:-3]) != '' and len(x)>6:#nécessité d'un espace avant les milliers
            sp2 = ', '
        if unite(x[-9:-6]) != '' and len(x)>9:#nécessité d'un espace avant les millions
            sp3 = ', '

	#MILLIERS
        if x[-6:-3] == '000':
            milliers = ''+sp+unite(x[-3:])
        elif x == '1000':
            milliers = 'a thousand'
        else:
            milliers = unite(x[-6:-3])+' thousand'+sp+unite(x[-3:])

	#MILLIONS
        if len(x)>6:
            if x[-9:-6] == '000':
                millions = ''
            else:
                millions = unite(x[-9:-6])+' million'

	#MILLIARDS
        if len(x)>9:
            if x[-12:-9] == '000' or len(x)>12:
                milliards = 'more than trillion'
            else:
                milliards = unite(x[-12:-9])+' billion'

	#TOTAL
        total=milliards+sp3+millions+sp2+milliers

    return total

def conv(x):
    """
    Principal function of this package :
    It takes only one argument (int, float or str) and converts it into letters.

    Example :
    conv(10) returns 'ten euros'
    """
    x=formater(x)
    e,c = x.split('.')[0],x.split('.')[1]
    if len(c)==1:
        c=c+'0'
    if int(c)==0:
        c=''
    elif int(c)==1:
        c='one cent'
    else:
        c=nombre2lettres(c)+' cents'
    if int(e)==0:
        if c=='':
            return 'zero euro'
        else:
            return c
    elif int(e)==1:
        e='one euro'
    else:
        e=nombre2lettres(e)+' euros'
    if c=='':
        return e
    else:
        return e+' and '+c

if __name__ == '__main__':
	result=conv(str(input('Enter here the amount in figures   :')))
	print(result)
