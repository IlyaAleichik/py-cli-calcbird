greenBirdTime = 50
yellowBirdTime = 500
browBirdTime = 2500
darkBlueBirdTime = 7500
redBirdTime = 45000


print("Введите кол-во Зеленых")
greenBird = int(input())
print("Введите кол-во Желтых")
yellowBird = int(input())
print("Введите кол-во Коричневых")
browBird = int(input())
print("Введите кол-во Синих")
darkBlueBird = int(input())
print("Введите кол-во Красных")
redBird = int(input())


print("Зеленые-------------------------------------------")
inHours = greenBirdTime * greenBird
inDay = inHours * 24
inMounth = inDay * 30
inYear = inMounth * 12

inHoursSilverSum = inHoursSilver = 0.01 * inHours * 0.5
inDaySilverSum = inDaySilver =  0.01 * inDay * 0.5
inMounthSilverSum = inMounthSilver =  0.01 * inMounth * 0.5
inYearSilverSum = inYearSilver =  0.01 * inYear * 0.5

inHourSum = inHoursMonay = 0.0001 * inHours * 0.5
inDaySum = inDayMonay =  0.0001 * inDay * 0.5
inMounthSum = inMounthMonay =  0.0001 * inMounth * 0.5
inYearSum = inYearMonay =  0.0001 * inYear * 0.5

# print(
# "Прибыль (серебро):\n"+ 
# "в час: "+  str(inHoursSilverSum)   + "\n"+ 
# "в день: "+  str(inDaySilverSum) + "\n"+
# "в мес: "+ str(inMounthSilverSum)  +"\n"+
# "в год: " + str(inYearSilverSum)  +"\n"
# )

# print(
# "Прибыль (яйца):\n"+ 
# "в час: "+  str(inHours)   + "\n"+ 
# "в день: "+  str(inDay) + "\n"+
# "в мес: "+ str(inMounth)  +"\n"+
# "в год: " + str(inYear)  +"\n"
# )

# print(
# "Прибыль (рубли):\n"+ 
# "в час: "+  str(inHoursSilver)   + "\n"+ 
# "в день: "+  str(inDaySilver) + "\n"+
# "в мес: "+ str(inMounthSilver)  +"\n"+
# "в год: " + str(inYearSilver)  +"\n"
# )

print("Желтые-------------------------------------------")

inHours = yellowBirdTime * yellowBird
inDay = inHours * 24
inMounth = inDay * 30
inYear = inMounth * 12

inHoursSilver = 0.01 * inHours * 0.5
inDaySilver =  0.01 * inDay * 0.5
inMounthSilver =  0.01 * inMounth * 0.5
inYearSilver =  0.01 * inYear * 0.5

inHoursMonay = 0.0001 * inHours * 0.5
inDayMonay =  0.0001 * inDay * 0.5
inMounthMonay =  0.0001 * inMounth * 0.5
inYearMonay =  0.0001 * inYear * 0.5



inHoursSilverSum += inHoursSilver 
inDaySilverSum += inDaySilver 
inMounthSilverSum += inMounthSilver 
inYearSilverSum += inYearSilver 

inHourSum += inHoursMonay
inDaySum += inDayMonay 
inMounthSum += inMounthMonay
inYearSum += inYearMonay 

# print(
# "Прибыль (серебро):\n"+ 
# "в час: "+  str(inHoursSilverSum)   + "\n"+ 
# "в день: "+  str(inDaySilverSum) + "\n"+
# "в мес: "+ str(inMounthSilverSum)  +"\n"+
# "в год: " + str(inYearSilverSum)  +"\n"
# )

# print(
# "Прибыль (яйца):\n"+ 
# "в час: "+  str(inHours)   + "\n"+ 
# "в день: "+  str(inDay) + "\n"+
# "в мес: "+ str(inMounth)  +"\n"+
# "в год: " + str(inYear)  +"\n"
# )

# print(
# "Прибыль (рубли):\n"+ 
# "в час: "+  str(inHoursSilver)   + "\n"+ 
# "в день: "+  str(inDaySilver) + "\n"+
# "в мес: "+ str(inMounthSilver)  +"\n"+
# "в год: " + str(inYearSilver)  +"\n"
# )

print("Коричневые-------------------------------------------")

inHours = browBirdTime * browBird
inDay = inHours * 24
inMounth = inDay * 30
inYear = inMounth * 12

inHoursSilver = 0.01 * inHours * 0.5
inDaySilver =  0.01 * inDay * 0.5
inMounthSilver =  0.01 * inMounth * 0.5
inYearSilver =  0.01 * inYear * 0.5

inHoursMonay = 0.0001 * inHours * 0.5
inDayMonay =  0.0001 * inDay * 0.5
inMounthMonay =  0.0001 * inMounth * 0.5
inYearMonay =  0.0001 * inYear * 0.5



inHoursSilverSum += inHoursSilver 
inDaySilverSum += inDaySilver 
inMounthSilverSum += inMounthSilver 
inYearSilverSum += inYearSilver 

inHourSum += inHoursMonay
inDaySum += inDayMonay 
inMounthSum += inMounthMonay
inYearSum += inYearMonay 

# print(
# "Прибыль (яйца):\n"+ 
# "в час: "+  str(inHours)   + "\n"+ 
# "в день: "+  str(inDay) + "\n"+
# "в мес: "+ str(inMounth)  +"\n"+
# "в год: " + str(inYear)  +"\n"
# )

# print(
# "Прибыль (рубли):\n"+ 
# "в час: "+  str(inHoursSilver)   + "\n"+ 
# "в день: "+  str(inDaySilver) + "\n"+
# "в мес: "+ str(inMounthSilver)  +"\n"+
# "в год: " + str(inYearSilver)  +"\n"
# )

print("Синие-------------------------------------------")

inHours = darkBlueBirdTime * darkBlueBird
inDay = inHours * 24
inMounth = inDay * 30
inYear = inMounth * 12

inHoursSilver = 0.01 * inHours * 0.5
inDaySilver =  0.01 * inDay * 0.5
inMounthSilver =  0.01 * inMounth * 0.5
inYearSilver =  0.01 * inYear * 0.5

inHoursMonay = 0.0001 * inHours * 0.5
inDayMonay =  0.0001 * inDay * 0.5
inMounthMonay =  0.0001 * inMounth * 0.5
inYearMonay =  0.0001 * inYear * 0.5



inHoursSilverSum += inHoursSilver 
inDaySilverSum += inDaySilver 
inMounthSilverSum += inMounthSilver 
inYearSilverSum += inYearSilver 

inHourSum += inHoursMonay
inDaySum += inDayMonay 
inMounthSum += inMounthMonay
inYearSum += inYearMonay 


# print(
# "Прибыль (яйца):\n"+ 
# "в час: "+  str(inHours)   + "\n"+ 
# "в день: "+  str(inDay) + "\n"+
# "в мес: "+ str(inMounth)  +"\n"+
# "в год: " + str(inYear)  +"\n"
# )

# print(
# "Прибыль (рубли):\n"+ 
# "в час: "+  str(inHoursSilver)   + "\n"+ 
# "в день: "+  str(inDaySilver) + "\n"+
# "в мес: "+ str(inMounthSilver)  +"\n"+
# "в год: " + str(inYearSilver)  +"\n"
# )

print("Красные-------------------------------------------")

inHours = redBirdTime * redBird
inDay = inHours * 24
inMounth = inDay * 30
inYear = inMounth * 12

inHoursSilver = 0.01 * inHours * 0.5
inDaySilver =  0.01 * inDay * 0.5
inMounthSilver =  0.01 * inMounth * 0.5
inYearSilver =  0.01 * inYear * 0.5

inHoursMonay = 0.0001 * inHours * 0.5
inDayMonay =  0.0001 * inDay * 0.5
inMounthMonay =  0.0001 * inMounth * 0.5
inYearMonay =  0.0001 * inYear * 0.5



inHoursSilverSum += inHoursSilver 
inDaySilverSum += inDaySilver 
inMounthSilverSum += inMounthSilver 
inYearSilverSum += inYearSilver 

inHourSum += inHoursMonay
inDaySum += inDayMonay 
inMounthSum += inMounthMonay
inYearSum += inYearMonay 

# print(
# "Прибыль (яйца):\n"+ 
# "в час: "+  str(inHours)   + "\n"+ 
# "в день: "+  str(inDay) + "\n"+
# "в мес: "+ str(inMounth)  +"\n"+
# "в год: " + str(inYear)  +"\n"
# )

# print(
# "Прибыль (рубли):\n"+ 
# "в час: "+  str(inHoursSilver)   + "\n"+ 
# "в день: "+  str(inDaySilver) + "\n"+
# "в мес: "+ str(inMounthSilver)  +"\n"+
# "в год: " + str(inYearSilver)  +"\n"
# )

print("Итого-------------------------------------------\n")

print(
"Прибыль (серебро):\n"+ 
"в час: "+  str(inHoursSilverSum)   + "\n"+ 
"в день: "+  str(inDaySilverSum) + "\n"+
"в мес: "+ str(inMounthSilverSum)  +"\n"+
"в год: " + str(inYearSilverSum)  +"\n"
)

print(
"Прибыль (рубли):\n"+ 
"в час: "+  str(inHourSum)   + "\n"+ 
"в день: "+  str(inDaySum) + "\n"+
"в мес: "+ str(inMounthSum)  +"\n"+
"в год: " + str(inYearSum)  +"\n"
)

