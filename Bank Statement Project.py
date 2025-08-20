#Ryan Edwards - Bank Statement Project

with open('transaction.txt', 'r') as input_file, open('bank_statement.txt', 'w') as output_file: #open both files, input for reading and output for writing

    output_file.write('Type....Amount......Balance'+'\n') #write header to output

    balance = float(input_file.readline().rstrip('\n')) #read first line of input file to get balance

    totalNum_With = 0 #create variables for running totals and sums
    totalNum_Dep = 0
    sumOfWith = 0
    sumOfDep = 0

    for line in input_file: #go through input

        line = line.strip() #strip line

        if line == 'W': 
            withAmount = float(input_file.readline()) #if W is found read next line for with amount
            balance -= withAmount #subtract withAm from balance
            output_file.write('W......' + f'{withAmount:.2f}.......' + f'{balance:.2f}'+'\n') #write the transaction information to output file
            totalNum_With += 1 #keep track of times a withdrwl is made
            sumOfWith += withAmount #sum of dollar amount of withdrwls

        elif line == 'D':
            depAmount = float(input_file.readline()) #if D is found read nxt line
            balance += depAmount # add to balance
            output_file.write('D......' + f'{depAmount:.2f}.......' + f'{balance:.2f}'+'\n') #write the transact information to output 
            totalNum_Dep += 1 #keep track of times a deposit is made
            sumOfDep += depAmount #keep total dollar amount of deposits

    output_file.write('\n') 
    output_file.write(f'Ending Balance: ${balance:.2f}'+'\n') #write the final balance to output
    output_file.write(f'Total Number of Withdrawals: {totalNum_With}'+'\n') #write total num of withs to output
    output_file.write(f'Total Withdrawals: ${sumOfWith:.2f}'+'\n') #write dollar sum of withs to output
    output_file.write(f'Total Number of Deposits: {totalNum_Dep}'+'\n') #write total num of deps to output
    output_file.write(f'Total Deposits: ${sumOfDep:.2f}') #write dollar sum of deps to output

#Type....Amount......Balance
#W......200.00.......4800.00
#W......800.00.......4000.00
#W......40.00.......3960.00
#D......90.00.......4050.00
#D......100.00.......4150.00
#D......1000.00.......5150.00
#W......20.00.......5130.00

#Ending Balance: $5130.00
#Total Number of Withdrawals: 4
#Total Withdrawals: $1060.00
#Total Number of Deposits: 3
#Total Deposits: $1190.00