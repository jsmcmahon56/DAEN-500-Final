##Jim McMahon
##DAEN 500 Final
##Problem 2

#this is the class that will manipulate the input string
class StringManipulator:
    def __init__(self, currString = ''):
        self.currString = currString

    #method for getting user string input
    def getString(self):
        print('Enter a string')
        user_input = input()
        myString = str(user_input)
        self.currString = myString

    #method for making input all caps
    def printString(self):
        self.currString = self.currString.upper()
        print(self.currString)

#methods are repeated below to test all cases mentioned in problem statement
if __name__ == '__main__':
    newManipulator = StringManipulator()
    newManipulator.getString()
    newManipulator.printString()
    newManipulator.getString()
    newManipulator.printString()
    newManipulator.getString()
    newManipulator.printString()

