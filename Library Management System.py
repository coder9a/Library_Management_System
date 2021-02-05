class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def display_books(self):
        for book in self.booklist:
            print(book)

    def lend_books(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print('You can borrow the book, database updated successfully')
        else:
            print(f'Book is already used by {self.lendDict[book]}')

    def add_books(self, book):
        self.booklist.append(book)
        print('Book has been added to the library')

    def return_books(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    lib = Library(['Python', 'C++', 'C#', 'Ruby', 'JAVA'], 'Public Library')
    while(True):
        print(f'Welcome to {lib.name} Library. Enter your choice ')
        print('1. Display Books')
        print('2. Lend Books')
        print('3. Add Books')
        print('4. Return Books')
        user_choice = int(input('Enter your  choice '))
        if user_choice not in [1, 2, 3, 4]:
            print('Enter valid choice ')
            continue

        if user_choice == 1:
            lib.display_books()

        elif user_choice == 2:
            book = input("Enter book name ")
            user = input('Enter your name ')
            lib.lend_books(user, book)

        elif user_choice == 3:
            book = input('Enter book name ')
            lib.add_books(book)

        elif user_choice == 4:
            book = input('Enter book name ')
            lib.return_books(book)

        else:
            print('Not a valid option ')

        print('Enter q to quit and c to continue ')
        user_choice2 = input()
        if user_choice2 == 'c' or user_choice2 == 'C':
            continue
        elif user_choice2 == 'q' or user_choice2 == 'Q':
            exit()
