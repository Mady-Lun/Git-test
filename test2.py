class Rectangle:
    # a class to represent a rectangle
    def data(self, length, width):
        # a method to assign the length and width attributes
        self.length = length
        self.width = width
       
    def take_data(self):
         # a method to get the length and width from the user input
        self.length = int(input("Enter a length: "))
        self.width = int(input("Enter a width: "))
    def area(self):
        # a method to calculate and return the area of the rectangle
        return self.length * self.width
    
rect = Rectangle()
rect.take_data() # call the take_data method to get the inputs from the user
print("The area is: ", rect.area()) # print out the result using the area method