from modules.stocks import Stocks
from modules.borrow import BorrowBook
from modules.returned import ReturnBook
from datetime import datetime, timedelta

def Main():
        #runs the program continuously
        while(True):
                print("\n\n"+"-"*60)
                print("\t Welcome to Library Management System")
                print("-"*60)
                print("Choose Options")
                print("1. Show Stocks")                                                  
                print("2. Display Borrowers")
                print("3. Return List")
                print("4. Issue Book")
                print("5. Return Book")
                print("6. Exit")

                opt = input("Enter (1/2/3/4/5/6): ")
                        
                if opt == '1':
                        #calling method displayStock from Stocks on object stocks to display the stock details
                        stocks  = Stocks("files/stock.txt")
                        stocks.displayStock()
                                
                                
                elif opt == '2':
                        print("\nChoose Options")
                        print("A. Show details of an individual.")
                        print("B. Display borrowed list.")
                        options = input("Enter (A or B) : ")

                        if options == 'A':
                                #calling method displayBorrower of class BorrowBook on object borrower to display the details of a single borrower
                                borrower = BorrowBook.displayBorrower()                      

                        elif options == 'B':
                                #calling method displayBorrowersList of class BorrowBook on object borrower to display the details of all the borrowers
                                borrower = BorrowBook.displayBorrowersList("files/borrowers.txt")

                        else:
                                print("\nPlease enter the valid option.")
                                

                elif opt == '3':
                        print("\nChoose Options")
                        print("A. Show details of an individual.")
                        print("B. Display returned list.")

                        options = input("Enter (A or B) : ")

                        if options == 'A':
                                #calling method displayReturn of class ReturnBook on object returnBook to display the details of a single returner
                                returnBook = ReturnBook.displayReturn()
                                
                        elif options == 'B':
                                #calling method displayReturnList of class ReturnBook on object returnBook to display the details of all the returners
                                returnBook = ReturnBook.displayReturnList("files/return.txt")

                        else:
                                print("\nPlease enter the valid option.")
                                
                                
                elif opt == '4':
                        
                        #for issuing books      
                        firstname = input("First Name : ").strip()
                        lastname = input("Last Name : ").strip()

                        #to check if the inputs provided are in alphabets
                        if firstname.isalpha() or lastname.isalpha():
                                
        
                                bookname = input("Books (if multiple books, separate it by ','): ")
                                books = bookname.split(",")     
                                        
                                concatenated_books = ""
                                price = 0
                
                                stock = Stocks("files/stock.txt")

                                try:
                                        for book in books:
                                                #adding price and concatenating names if multiple books are issued
                                                price += stock.getPrice(book.strip())
                                                concatenated_books += book + " & "
                                        price = price
                                        books = concatenated_books.strip(" & ")
                                              
                                        issue_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                        returned_status = str(False)
                                        return_date = (datetime.now() + timedelta(days=10) ).strftime('%Y-%m-%d')

                                        '''creating new borrower with the values assigned above and initializing it to the variable new_borrower.
                                        running the function borrow from class BorrowBook to write the values stored in the variable in a text file'''
                                        new_borrower = BorrowBook(firstname, lastname, ''.join(books), issue_date, returned_status, return_date, price)
                                        new_borrower.borrow('files/borrowers.txt')

                                        #function updateStock from class Stocks is called for updating the stocks
                                        stock.updateStock(books)
                                        
                                        print("\nThe book is successfully issued.")
                                        print("#" * 40)
                                        
                                except:
                                        print("\nThe book is not available.")
                                               
                        else:
                                print("Please enter alphabet A-Z.")


                elif opt == '5':
                        #for returning the books               
                        name = input("Enter the name of the borrower : ").strip()
                        txtFile="Borrowed By - " + name + ".txt"
                        #checks if the file with the input name is available
                        try:
                                with open(txtFile,"r") as file:
                                    data=file.read()
                                   
                        except:
                                print("\nThe borrower name is not in the list.")


                        borrowers_list = BorrowBook.getBorrowersList('files/borrowers.txt')

                                
                        for borrowers in borrowers_list:
                                borrowed = borrowers['firstname'] +  borrowers['lastname']
                                        
                                if name ==  borrowed:
                                        returned_status = str(True)
                                        books = borrowers['books_borrowed'].lstrip()
                                        price = float(borrowers['price'])
                                        issue_date = borrowers['issue_date'].lstrip()
                                        return_date= borrowers['return_date'].lstrip()
                                        returned_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                        late = input("Was the book returned late y/n? ")
                                        try:
                                                if (late == 'y'):
                                                        additional_days = int(input("The book was returned late by how many days? "))
                                                        fine = float(2 * additional_days)
                                                        total_amount = fine + price
                                                elif(late == 'n'):
                                                        fine = 0
                                                        total_amount = price

                                                        
                                                '''creating new return with the values assigned above and initializing it to the variable new_return.
                                                running the function returned from class ReturnBook to write the values stored in the variable in a text file'''
                                                new_return = ReturnBook(name,  ''.join(books), issue_date, returned_status, return_date, returned_date, price, fine, total_amount)
                                                new_return.returned("files/return.txt")
                                                 
                                                
                                                #function updateAfter from class Stocks is called for updating the stocks
                                                stock  = Stocks("files/stock.txt")
                                                stock.updateAfter(books)
                                                
                                                print("\nThe book is successfully returned.")
                                                print("The total price will be" ,total_amount)
                                                print("#"*60)

                                        except:
                                                print("\nERROR : Please provide valid input.")
                                        

                        
                elif opt == "6":
                        continue_status = input("Do you want to exit? (y/n): ")
                        if continue_status == 'n':
                                continue
                        else:
                                print("\n"+"-" * 50)
                                print("\t\t THANK YOU ")
                                break
                        
                else :
                        print("\nERROR : Please input as suggested.")
                        	

 
if __name__ == "__main__":
        #if the current file is being run directly function main is executed
	Main()	
