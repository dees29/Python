q1="""Is python case sensitive when dealing with identifiers?
a. Yes
b. No
c. Machine Dependent
d. None"""
q2="""Which of the following is not a keyword?
a. eval
b. assert
c. local
d. pass"""
q3="""Which one of this floor division?
a. /
b. //
c. %
d. None"""
q4="""What is the output of 3*1**3?
a. 27
b. 9
c. 3
d. 1"""
q5=""""a"+"bc"=??
a. a
b. bc
c. bca
d. abc"""

questions = {q1:"a", q2:"a", q3:"b", q4:"c", q5:"d"}

score=0
for i in questions:
    print()
    flag2 = input("Do you want to quit the quiz (yes/no): ")
    if flag2=="yes":
        break
    print(i)
    flag1 = input("Enter do you want to skip the quiz (yes/no):")
    if flag1=="yes":
        continue
    ans=input("Enter the ans a/b/c/d: ")
    if ans == questions[i]:
        print("Your ans is correct you got 1 point")
        score=score+1
        print("your score is:",score)
    else:
        print("Your ans is wrong you lost 1 point")
        score=score-1
        print("your score is:",score)
        
    
print("your final score is:",score)
