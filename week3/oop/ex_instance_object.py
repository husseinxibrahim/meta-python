
# Define class MyFirstClass
class MyFirstClass():
    print("Who write this?")

    # Define string variable called index
    index="Author-Book"

    # Define function hand_list()
    def hand_list(self, philosopher, book):
        
        # variable + “ wrote the book: ” + variable
        print(MyFirstClass.index)
        print(philosopher + " wrote book: " + book)

# Call function handlist()
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War")