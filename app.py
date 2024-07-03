
def fizz_buzz(number):

 if (number % 3 == 0 and number % 5 ==0):
        print('fizzbuzz') 
        return  
 if(number % 3 == 0):
        print('fizz')
        return

 if(number % 5 == 0):
        print('Buzz')
        return
    

        
   


numbers = [30, 3, 100, 15, 12, 50, 7, 9, 6, 25, 1, 13, 10, 2, 4]

for number in numbers: 
      print(number)
      fizz_buzz(number)


 
    
 


