import math #importing math library to use its functions
def giveInput(): #"Menu" Function
    result = input("\nBelow are the available functions. Choose one by typing the number that it has or type stop.\n\n 1)Easy Calculations \n 2)Loan Payments \n :") #Get input for different calculations
    if result=="stop": # exit the script if keyword "stop" is typed above
        sys.exit()
    res = float(result) #or else float the string
    if res==1: #point its number to described calculation
        easyCalc()
    elif res==2:
        loanPayments()

def easyCalc():
    custom=float(input("Do you want two numbers or a custom addition of numbers?\nChoose using 1 or 2 depending on the option (1 for two numbers, 2 for custom addition.)\n"))
    if custom==1:
        num1=float(input("Give the first number: "))
        num2=float(input("Give the second number: "))
        add=num1+num2
        sub=num1-num2
        abssub=abs(sub)
        mult= num1*num2
        num1sq= num1**2
        num2sq= num2**2
        num1tnum2= num1**num2
        num2tnum1= num2**num1
        sqrtnum1= math.sqrt(num1)
        sqrtnum2= math.sqrt(num2)
        print( "\nAddition of {:3.4f} + {:3.4f} = {:3.8f}\nSubtraction of {:3.4f} - {:3.4f} = {:3.8f}\nAbsolute Subtraction of {:3.4f} - {:3.4f} = {:3.8f}\nMultiplication of {:3.4f} * {:3.4f} = {:3.8f}\n{:3.4f} Squared = {:3.8f}\n{:3.4f} Squared = {:3.8f}\n{:3.4f} ^ {:3.4f} = {:3.8f}\n{:3.4f} ^ {:3.4f} = {:3.8f}\nSquare Root of {:3.4f} = {:3.8f}\nSquare Root of {:3.4f} = {:3.8f}" .format(num1,num2,add,num1,num2,sub,num1,num2,abssub,num1,num2,mult,num1,num1sq,num2,num2sq,num1,num2,num1tnum2,num2,num1,num2tnum1,num1,sqrtnum1,num2,sqrtnum2))
        giveInput()
    elif custom==2:
        sum=0
        isRunning=True
        while isRunning: #while loop to allow the user to give as many numbers as he wants (acts like a calculator)
            keyword=input("Give number (if you want to stop, type stop): ") #keyword check for "stop"
            if keyword == "stop":
                isRunning = False
            else:
                newnum = float(keyword) #float the keyword if its not "stop"
                sum = sum + newnum #sum all the numbers given.
        sumsqr = sum**2 #sum squared
        sumcub = sum**3 #cube of sum
        sqrtsum = math.sqrt(sum) #square root of sum
        print("{:3.4f} Squared = {:3.8f}\nCube of {:3.4f} = {:3.8f}\nSquare Root of {:3.4f} = {:3.8f}" .format(sum, sumsqr, sum, sumcub, sum, sqrtsum))
        giveInput() #return to "Menu"

def loanPayments():
    loan=float(input("Money Borrowed: "))
    n = float(input("\nNumber of Years: ")) #
    r = float(input("\nRate Percentage: "))
    paymentNumber = n * 12 #number of payments done for selected years
    rate = (r / 100)/12 #interest rate
    disFactor = (((1+rate)**paymentNumber)-1) / (rate*(1+rate)**paymentNumber) #formula for discount factor
    payments = loan/disFactor
    repaidVal = payments*360 #Money to be repaid
    print("Your monthly payment is {:,.2f}" .format(payments)) #print formatted Results
    print("Money to be repaid: {:,.2f}" .format(repaidVal))
    giveInput() #return to "Menu"
def main():
    giveInput()

main() # start the script
