# CTI-110
# P4HW1 - Score List
# Brittany Reynolds 
# 3/25/22
#

count=int(input("How many scores do you want to enter? "))
print("\n")

i,mylist=1,[]

while(True):   
    if(len(mylist)==count):        
        break
     
    print("Enter score #"+str(i)+": ",end="")     

    score = int(input())
    
    if(score<0 or score>100):        
        print("\nINVALID Score entered!!!!")        
        print("Score should be between 0 and 100")
    
    else:        
        mylist.append(float(score))         
        i+=1 
 
mylist.sort()
lowest_score = mylist[0]
mylist.remove(lowest_score)
score_avg=sum(mylist)/len(mylist)

if(score_avg>90):     
    grade = "A"
 
elif(score_avg>=80 and score_avg<90):   
    grade = "B"
 
elif(score_avg>=70 and score_avg<80):
    grade = "C"
 
else:
    grade = "F"


print("\n\n--------------Results-----------")
print("Lowest Score      :",lowest_score)
print("Modified List     :",mylist)
print("Scores Average    :",score_avg)
print("Grade             :",grade)
print("-----------------------------------")
