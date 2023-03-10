FirstNumber=1
FirstNumber = float(input("Введите первое число: "))
SecondNumber=1
SecondNumber = float(input("Введите второе число: "))
NumberOperation=1
NumberOperation =float( input("Введите колличество операций: "))
Operation = input("Введите знак операции: ")
result = 0.0
def calc(firstnumber,secondnumber,operation):
    global result
    if operation=="-":
        result=firstnumber-secondnumber
    if Operation=="+":
        result=firstnumber+secondnumber
    if Operation=="*":
        result=firstnumber*secondnumber
    if Operation=="/":
        if secondnumber==0:
            return input("Делить на ноль нельзя, введите другое число")
        elif secondnumber!=0:
            result=firstnumber/SecondNumber
    if Operation=="^":
        result=FirstNumber**SecondNumber
calc(FirstNumber,SecondNumber,Operation)
i=1
while i<NumberOperation:
    Operation = input("Введите знак операции: ")
    SecondNumber = float(input("Введите второе число: "))
    calc(result,SecondNumber,Operation)
    i+=1
print(f"Резуьтат: {result}")