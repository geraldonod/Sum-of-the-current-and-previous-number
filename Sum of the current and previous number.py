#for loop for the first 10 numbers
for i in range(10):
#if else statement to identify current and previous number
    if i == 0:
        previous_num = 0
    else:
        previous_num = i - 1

    current_num = i
#get the sum by adding current and previous number
    number_sum = current_num + previous_num

#print out result
    print(f"Current: {current_num}, Previous: {previous_num}, Sum: {number_sum}")