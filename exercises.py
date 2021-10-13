
# Exercise #1
countriesList = ['', '', 'Argentina', '', 'San Diego', 'Boston', '', 'New York']

def cleanUpCountries(countriesList):
    inputList = ['', '', 'Argentina', '', 'San Diego', 'Boston', '', 'New York']

    return list(filter(None, inputList))




# Exercise #2
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

def sortAuthors(author):
    author.sort(key=lambda name: name.split(" ")[-1].lower())
    return(author)




# Exercise #3
tempsList = [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
# F = (9/5)*C + 32
# C = (5/9)*(F-32)

def fToC(tempsList):
    return list(map(lambda tup: int((5/9)*(tup[-1]-32)), tempsList))





#Exercise #4
previous_nums = [1,1]

def fib(n, count=0):
    if n < 1:
        print("0 : 1")
        return
    
    else:
        print(count, ':', previous_nums[0])
        previous_nums.append(previous_nums[0] + previous_nums[1])
        del previous_nums[0]
        
        if count < n:
            fib(n, count=count+1)
        else:
            return

#fib(2100)