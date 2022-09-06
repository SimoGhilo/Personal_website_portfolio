class Calculator():
    def __init__():
        self.Add = Add
        self.Subtract = Subtract
        self.Multiply = Multiply
        self.Divide = Divide
        
    
    def Add(x,y):
        return (x + y)
            
    def Subtract(x,y):
        if (y > x):
            return ('Subtraction not possible')
        else:
            return(x-y)
                
    def Multiply(x,y):
        return (x*y)
            
    def Divide(x,y):
        if (y == 0):
            return('Division by 0 not allowed')
        else:
            return (x/y)







while True:
    
    choice = int(input('What would you like to do ? 1 - Add, 2 - Subtract, 3 - Multiply, 4 - Divide'))
    
    if choice == 1:
        a = int(input('Enter first number here'))
        b = int(input('Enter second number here'))
        print(Calculator.Add(a,b))
    if choice == 2:
        c = int(input('Enter first number here'))
        d = int(input('Enter second number here'))
        print(Calculator.Subtract(c,d))
    if choice == 3:
        e = int(input('Enter first number here'))
        f = int(input('Enter second number here'))
        print(Calculator.Multiply(e,f))
    if choice == 4:
        g = int(input('Enter first number here'))
        h = int(input('Enter second number here'))
        print(Calculator.Divide(g,h))





        
        
