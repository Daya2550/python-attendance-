import datetime
import name

current_date = datetime.datetime.now()
formatted_date = current_date.strftime('%d-%m-%Y')
formatted_time = current_date.strftime('%H:%M')

file_name="sy2024="+str(formatted_date)+".txt"

prsent = [1] * 5
check =[True]*5
spre=[0]*5
apre=[0]*5
total=4

subject=input("Please enter the subject : ")
file = open(file_name, "w")
file.write(subject)
file.write("\n")
file.write(formatted_date)
file.write("\n")
file.write(formatted_time)
file.close()


print (subject)
print("Current Date (day-month-year):", formatted_date)
print("Current Time (hour-minute):", formatted_time)
i=0
while i<4:
    i=i+1
    print("\nroll NO : ",i)
    print("present for 1 and absent for 0")
    pp =int(input("p=1 $ AB =0 : ") )
    if(pp==1 or pp==0):
        check[i]=pp
    else:
        print("please enter 1 or 0\n")
        i=i-1

for i in range(1, 5):
    acount=0
    pcount=0
    if prsent[i] == check[i]:
           pcount=pcount+1
           spre[i]=i
    else:
        acount=acount+1
        apre[i]=i      



print("")
file = open(file_name, "a")
file.write("\nPresent Students : \n")
file.close()
print("Present Students")
no_p=0
for i in range(1,5):
    if spre[i] != 0:
       no_p=no_p+1
       print(str(i),":",end="" )
       print(name.stuname (i))
       file = open(file_name, "a")
       file.write(str(i))
       file.write(" :")
       file.write(name.stuname (i))
       file.write("\n")
       file.close()
print("Total number of present : ",no_p)


print("\n")
file = open(file_name, "a")
file.write("Total number of present : ")
file.write(str(no_p))
file.write("\n")
file.write("\n")
file.close()


file = open(file_name, "a")
file.write("Absent students : \n")
file.close()
print("Absent students")
for i in range(1,5):
    if apre[i]!= 0:
        print(str(i),":",end="" )
        print(name.stuname (i))
        file = open(file_name, "a")
        file.write(str(i))
        file.write(" :")
        file.write(name.stuname (i))
        file.write("\n")
        file.close()
print("Total number of Absent : ",total-no_p) 
file = open(file_name, "a")
file.write("Total number of Absent : ")
file.write(str(total-no_p))
file.write("\n")
file.close()

        


