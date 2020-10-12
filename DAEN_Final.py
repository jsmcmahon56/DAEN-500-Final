##Jim McMahon
##DAEN 500 Final
##Problem 1

def find_nums(num1, num2):
    #First ID which number is lower
    if num1 > num2:
        clean_num1 = num2 #clean_num1 is low end
        clean_num2 = num1 #clean_num2 is high end
    elif num2 > num1:
        clean_num1 = num1 #clean_num1 is low end
        clean_num2 = num2 #clean_num2 is high end
    else:
        clean_num1 = num1 #for when nums are equal
        clean_num2 = num2 #for when nums are equal

    #Now find nums div. by 7 and but not mult. of 5
    solution_nums = []  # for storing nums that fit criteria
    if clean_num1 == clean_num2:
        if clean_num1 % 5 != 0 and clean_num1 % 7 == 0:
            solution_nums.append(clean_num1)
            return solution_nums
    elif clean_num1 != clean_num2:
        myRange = range(clean_num1, clean_num2 + 1)
        for item in myRange:
            if item % 5 !=0 and item % 7 == 0:
                solution_nums.append(item)
        return solution_nums
    else:
        print('ERROR')

if __name__ == '__main__':
    answer = find_nums(2000, 3200)
    print(answer)

