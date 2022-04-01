import re

lista = ['23 + 22', '12 - 2', '22 - 543', '22 - 2', '152 + 64']

def numbervalidation(lista):  #Validate that argument contains only numbers.
    for list in lista:
        if re.search ('[a-zA-Z]',list):
            return True
def operandvalidation(lista): #Validate that operators are NOT * or /
    for list in lista:
        if re.search ('[*|/]',list):
            return True
def charlongitude(lista): #Validate that each operand has a maximum of 4 digits.
    for list in lista:
           pos = re.search('[+|\-]', list).start()
           firstnumber = list[0:pos].rstrip()
           secondnumber = list[pos+1:].lstrip()
           if len(firstnumber) > 4 or len(secondnumber) > 4:
                return 0

while True:
    if len(lista) > 5:
        print ("Too many problems.")
        print ('Max number of problems is FIVE')
    if numbervalidation(lista):
        print("Error: Numbers must only contain digits")
    if operandvalidation(lista):
        print("Error: Operator must be '+' or '-'.'")
    if  charlongitude(lista) == 0:
        print('Error: Numbers cannot be more than four digits.')
    break
    
for list in lista:
    pos = re.search('[+|\-]', list).start()
    firstnumber = list[0:pos].rstrip()
    secondnumber = list[pos+1:].lstrip()
    if len(firstnumber) >= len(secondnumber):
        longestnumber = firstnumber.rjust(len(firstnumber)+2)
        shortestnumber = secondnumber.rjust(len(firstnumber))
        print(f'{longestnumber}\n{list[pos]} {shortestnumber}\n{"-"*(len(firstnumber)+2)}', end=" ")
    elif len(secondnumber) > len(firstnumber):
        longestnumber = firstnumber.rjust(len(secondnumber)+2)
        print(f'{longestnumber}\n{list[pos]} {secondnumber}\n{"-"*(len(secondnumber)+2)}', end=" ")
