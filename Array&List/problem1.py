
# find number of days above average temperature


inp = int(input("How many day's temperature? "))


temp = []

i = 1 
while i <= inp : 
    value = int(input(f"Day + {i}'s high temp: ")) 
    temp.append(value) 
    i +=1 

avr = sum(temp) / len(temp)

print(f"Average = {float(avr)} \n 1 day (s) above average ")
