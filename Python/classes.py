class MyClass:
    # constructor
    def __init__(self, nums): #self is always the first argument in a class functon
        print(len(nums))
        # creating a member variable
        self.size = len(nums)
    
    # each function in a class needs self param
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength() #calling other member functions in a member function