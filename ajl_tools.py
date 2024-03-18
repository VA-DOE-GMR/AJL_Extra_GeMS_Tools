from os.path import exists
from random import choice

def decimalEncrypt(entry_string : str) -> str:
    '''Encrypt input string into base-10 string.'''

    chr_dict = {' ':'032','!':'033','"':'034','#':'035','$':'036','%':'037','&':'038',"'":'039','(':'040',')':'041','*':'042','+':'043',',':'044','-':'045','.':'046','/':'047','0':'048','1':'049','2':'050','3':'051','4':'052','5':'053','6':'054','7':'055','8':'056','9':'057',':':'058',';':'059','<':'060','=':'061','>':'062','?':'063','@':'064','A':'065','B':'066','C':'067','D':'068','E':'069','F':'070','G':'071','H':'072','I':'073','J':'074','K':'075','L':'076','M':'077','N':'078','O':'079','P':'080','Q':'081','R':'082','S':'083','T':'084','U':'085','V':'086','W':'087','X':'088','Y':'089','Z':'090','[':'091','\\':'092',']':'093','^':'094','_':'095','`':'096','a':'097','b':'098','c':'099','d':'100','e':'101','f':'102','g':'103','h':'104','i':'105','j':'106','k':'107','l':'108','m':'109','n':'110','o':'111','p':'112','q':'113','r':'114','s':'115','t':'116','u':'117','v':'118','w':'119','x':'120','y':'121','z':'122','{':'123','|':'124','}':'125','~':'126'}

    output_string = ""

    for n in range(len(entry_string)):
        output_string = f"{output_string}{chr_dict[entry_string[n]]}"

    return output_string

def decimalDecrypt(entry_string : str) -> str:
    '''Decrypt input string that is in base-10.'''

    chr_dict = {'032':' ','033':'!','034':'"','035':'#','036':'$','037':'%','038':'&','039':"'",'040':'(','041':')','042':'*','043':'+','044':',','045':'-','046':'.','047':'/','048':'0','049':'1','050':'2','051':'3','052':'4','053':'5','054':'6','055':'7','056':'8','057':'9','058':':','059':';','060':'<','061':'=','062':'>','063':'?','064':'@','065':'A','066':'B','067':'C','068':'D','069':'E','070':'F','071':'G','072':'H','073':'I','074':'J','075':'K','076':'L','077':'M','078':'N','079':'O','080':'P','081':'Q','082':'R','083':'S','084':'T','085':'U','086':'V','087':'W','088':'X','089':'Y','090':'Z','091':'[','092':'\\','093':']','094':'^','095':'_','096':'`','097':'a','098':'b','099':'c','100':'d','101':'e','102':'f','103':'g','104':'h','105':'i','106':'j','107':'k','108':'l','109':'m','110':'n','111':'o','112':'p','113':'q','114':'r','115':'s','116':'t','117':'u','118':'v','119':'w','120':'x','121':'y','122':'z','123':'{','124':'|','125':'}','126':'~'}

    output_string = ""

    for n in range(0,len(entry_string),3):
        output_string = "%s%s" % (output_string,chr_dict[entry_string[n:n+3]])

    return output_string

def listComputerDrives() -> tuple:
    '''Detects drives on a computer and outputs them as a tuple'''

    import win32api

    return tuple(win32api.GetLogicalDriveStrings().split('\000')[:-1])

def randAlphaNumStr(length = 6,censor=False) -> str:

    chars = tuple(sorted(['0','1','2','3','4','5','6','7','8','9'] + [chr(n) for n in range(65,91)] + [chr(n) for n in range(97,123)]))

    if censor:
        profanity = tuple([line.rstrip("\n") for line in open("profane_filter.txt").readlines()])
        no_profanity = False
        while not no_profanity:
            no_profanity = True
            random_name = ""
            for _ in range(length):
                random_name = f"{random_name}{choice(chars)}"
            for word in profanity:
                if word in random_name:
                    no_profanity = False
                    break
    else:
        random_name = ""
        for _ in range(length):
            random_name = f"{random_name}{choice(chars)}"

    return random_name

def to_list(tple : tuple) -> list:
    '''Converts nested tuple into nested list.
    This mainly exists with the idea of modifying items in a nested tuple
    before converting it back into a nested tuple via to_tuple.'''

    # works with non-nested tuples as well.

    return list(to_list(i) if isinstance(i,tuple) else i for i in tple)

def to_tuple(lst : list) -> tuple:
    '''Converts nested list into nested tuple
    Nested tuples are excellent for reducing memory-usage
    as well as efficiency of loops using the outputed
    nested tuple.'''

    # works with non-nested lists as well.

    return tuple(to_tuple(i) if isinstance(i,list) else i for i in lst)
