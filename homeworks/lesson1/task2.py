sec_input = input("Введите время в секундах\n")
if sec_input.isdigit():
    sec_input = int(sec_input)
    hours = sec_input//3600
    minutes = ((sec_input//60)%60)
    sec_output = (sec_input%60)

print (hours,minutes,sec_output,sep=":")
