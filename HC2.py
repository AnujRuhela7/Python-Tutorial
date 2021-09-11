'''one = [ "", "one ", "two ", "three ", "four ",
        "five ", "six ", "seven ", "eight ",
        "nine ", "ten ", "eleven ", "twelve ",
        "thirteen ", "fourteen ", "fifteen ",
        "sixteen ", "seventeen ", "eighteen ",
        "nineteen "]
ten = [ "", "", "twenty ", "thirty ", "forty ",
        "fifty ", "sixty ", "seventy ", "eighty ",
        "ninety "]

def numToWords(n,s):
    str = ""
    if (n > 19):
        str += ten[n // 10] + one[n % 10]
    else:
        str += one[n]

    if (n):
        str += s
    return str

def convertToWords(n):
    out = ""
    out += numToWords((n // 10000000),"crore ")
    out += numToWords(((n // 100000) % 100),"lakh ")
    out += numToWords(((n // 1000) % 100),"thousand ")
    out += numToWords(((n // 100) % 10),"hundred ")
 
    if (n > 100 and n % 100):
        out += "and "

    out += numToWords((n % 100),"")
    return out

n = int(input())
print(convertToWords(n))'''

ones = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
twos = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
tens = ('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred')
suffixes = ('', 'thousand', 'million', 'billion')
def p1(number, index):
    if number=='0':
        return 'zero'
    length = len(number)
    if(length > 3):
        return False
    number = number.zfill(3)
    words = ''
    hdigit = int(number[0])
    tdigit = int(number[1])
    odigit = int(number[2])
    words += '' if number[0] == '0' else ones[hdigit]
    words += ' hundred ' if not words == '' else ''
    if(tdigit > 1):
        words += tens[tdigit - 2]
        words += ' '
        words += ones[odigit]
    elif(tdigit == 1):
        words += twos[(int(tdigit + odigit) % 10) - 1]
    elif(tdigit == 0):
        words += ones[odigit]
    if(words.endswith('zero')):
        words = words[:-len('zero')]
    else:
        words += ' '
    if(not len(words) == 0):    
        words += suffixes[index]
    return words;
def p2(number):
    length = len(str(number))
    if length>12:
        return 'failed'
    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []
    for i in range(length - 1, -1, -3):
        words.append(p1(str(number)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))
        count -= 1;
    final_words = ''
    for s in reversed(words):
        temp = s + ' '
        final_words += temp
    return final_words
number = int(input())
print(p2(number))