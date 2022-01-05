from functools import reduce
#from operator import add
def summarize(data):
    #extract necessary infomation form list data
    lower=int(data[0]) # lower bound
    upper=int(data[1]) # upper bound
    operant_and_base=data[2] # operate sign and calculate base number
    results_array=[]
    #loop up to upper value
    for n in range(lower,upper+1):

        result_str=str(n)+operant_and_base
        #use eval function to evaluate express
        result=eval(result_str)
        results_array.append(result)
    #method 1: use add operator operator
    #return reduce(add,result_arrays)
    #method 2 : use lambda expression
    return reduce(lambda n1,n2:n1+n2 , results_array)
#from input data , remove both ends spaces and split by blank to make a  list of 3 string members
expr=input('chuoi ').strip().split()
print(summarize(expr))