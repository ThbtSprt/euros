from re import sub

chiffres = ['','uno','due','tre','quatro','cinque','sei','sette','otto','nove','dieci','undici','dodici','tredici','quattordici','quindici','sedici','diciassette','diciotto','dicianove8']
nombres = ['','dieci','venti','trenta','quaranta','cinquanta','sessanta','settanta','ottenta','novanta']

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
    One mandatory argument : a string input representing an integer
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
    elif int(x[-1]) == 3:
        dizaines = nombres[int(x[-2])]+'tré'
    elif int(x[-2:]) in [21,31,41,51,61,71,81,91]:
        dizaines = nombres[int(x[-2])][:-1]+'uno'
    elif int(x[-2:]) in [28,38,48,58,68,78,88,98]:
        dizaines = nombres[int(x[-2])][:-1]+'otto'
    elif int(x[-1])==0:
        dizaines = nombres[int(x[-2])]
    else:
        dizaines = nombres[int(x[-2])]+chiffres[int(x[-1])]

    if x[0] == '0':
        return dizaines
    else:
        if x[0] == '1':
            centaines = 'cento'
        else:
            centaines = chiffres[int(x[0])]+'cento'
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
        sp2,sp3='',''
        if unite(x[-6:-3]) != '' and len(x)>6:
            sp2 = ' '
        if unite(x[-9:-6]) != '' and len(x)>9:
            sp3 = ' '

	#MILLIERS
        if unite(x[-6:-3]) == 'uno':
            milliers = 'mille'+unite(x[-3:])
        elif x[-6:-3] == '000':
            milliers = ''+unite(x[-3:])
        else:
            milliers = unite(x[-6:-3])+'mila'+unite(x[-3:])

	#MILLIONS
        if len(x)>6:
            if unite(x[-6:-3])!='' or  unite(x[-3:])!='':
                sp2=' e '
            if unite(x[-9:-6]) == 'uno':
                millions = 'un milione'
            elif x[-9:-6] == '000':
                millions = ''
            else:
                millions = unite(x[-9:-6])+' milioni'

	#MILLIARDS
        if len(x)>9:
            if unite(x[-9:-6])!='':
                sp3=' e '
            if unite(x[-12:-9]) == 'uno':
                milliards = 'un miliardo'
            elif x[-12:-9] == '000' or len(x)>12:
                milliards = 'più di mille miliardi'
            else:
                milliards = unite(x[-12:-9])+' miliardi'

	#TOTAL
        total=milliards+sp3+millions+sp2+milliers

    return total

def conv(x):
    """
    Principal function of this package :
    It takes only one argument (int, float or str) and converts it into letters.

    Example :
    conv(10) returns 'dieci euros'
    """
    x=formater(x)
    e,c = x.split('.')[0],x.split('.')[1]
    if len(c)==1:
        c=c+'0'
    if int(c)==0:
        c=''
    elif int(c)==1:
        c='un centesimo'
    else:
        c=nombre2lettres(c)+' centesimi'
    if int(e)==0:
        if c=='':
            return 'zero euro'
        else:
            return c
    elif int(e)==1:
        e='uno euro'
    elif len(e)>6 and (e[-6:]=='000000' or e[-12:-9] == '000' or len(e)>12):
        e=nombre2lettres(e)+" di euro"
    else:
        e=nombre2lettres(e)+' euro'
    if c=='':
        return e
    else:
        return e+' e '+c

if __name__ == '__main__':
	result=conv(str(input("Inserisci l'importo in cifre   :")))
	print(result)
