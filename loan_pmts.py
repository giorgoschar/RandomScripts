def loanPayments(loan, n, r):
    paymentNumber = n * 12 #number of payments done for selected years
    rate = (r / 100)/12 #interest rate
    disFactor = (((1+rate)**paymentNumber)-1) / (rate*(1+rate)**paymentNumber) #formula for discount factor
    payments = loan/disFactor
    repaidVal = payments*360 #Money to be repaid
    print("Your monthly payment is {:,.2f}" .format(payments)) #print formatted Results
    print("Money to be repaid: {:,.2f}" .format(repaidVal))
