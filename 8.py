#Write a python program to determine weather a student is eligible for a scholarship.
#The scholarship should be granted if the student satisfies either of the following conditions:
#a) The student has a CGPA of 8.5 or above and attendance of 85 percent or above.
#b) The student has won a national-level competition.
# The program should take CGPA, attendance percentage, and national-level competition status as input, then display whether the student is eligible for the scholarship.


#Write a Pyothan program to simulate a digital lock system.
#The lock should ask the user to enter the 4-digit PIN. if the entered PIN does not contain 

#Write a python program to calculate the final bill amount after applying a discount. The program should take the total bill amount as input 
# from user and apply the discount according to the following rules. After calculating the discount , the program should display the discount 
#amount and the final bill amount payable by the customer.





#bill = float(input("Enter total bill amount: "))
#if bill > 5000:
#    discount = bill * 20/100
#elif bill >= 3000 and bill <= 5000:
#    discount = bill * 10/100
#else:
#    discount = 0
#    final_bill = bill - discount
#    print("Discount:", discount)
#    print("Final bill:", final_bill)




#Write a python program to the input marks of 5 students.
#For each student,the program should check weather the entered marks are valid or invalid. Marks are considered
#valid only if they are between 0 and 100. if the marks are invalid , the program should display "Invalid marks skipped "
# and move to the next student without printing those marks.
#If the marks are invalid , the program should dispay the marks valid.

for i in range (1,6):
    marks = int(input("Enter marks:"))
    if marks < 0 or marks > 100:
        print("invalid marks skipped")
        continue
    print ("valid marks")

#Write a python program to input four numbers from the user and find the greatest number among them.