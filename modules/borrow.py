class BorrowBook:

        def __init__(self, firstname="", lastname="", books_borrowed="", issue_date="", returned_status="", return_date="", price=""):
                self.firstname = firstname
                self.lastname = lastname
                self.books_borrowed = books_borrowed
                self.issue_date = issue_date
                self.returned_status = returned_status
                self.return_date = return_date
                self.price = price

        def borrow(self, path_to_borrowers):
                #creation of new text file and writing details on it
                txt_file = "Borrowed By - " + self.firstname +" "+ self.lastname +".txt"
                file = open(txt_file,'w')

                file.write ("Library Records For Borrow.\n")
                file.write("-"*50 + "\n")
                file.write(f'Borrowed By     : {self.firstname} {self.lastname}\n')
                file.write(f'Books Borrowed  : {self.books_borrowed}\n')
                file.write(f'Issue Date      : {self.issue_date}\n')
                file.write(f'Returned Status : {self.returned_status}\n')
                file.write(f'Return Date     : {self.return_date}\n')
                file.write(f'Price           : {self.price}\n')
                file.close()  

                #adding new borrower to the existing text file
                file2 = open(path_to_borrowers, 'a')
                file2.write(f'{self.firstname}, {self.lastname}, {self.books_borrowed}, {self.issue_date}, {self.returned_status}, {self.return_date}, {self.price} \n')
                file2.close()      
                

        def getBorrowersList(path_to_borrowers):
                borrowers_list = []

                file = open(path_to_borrowers,"r")
                lines = file.readlines()
                
                for line in lines:
                        #dictionary used to store data values of the list in pairs
                        borrower = {}
                        line_split = line.split(",")
                       
                        borrower['firstname'] = line_split[0]
                        borrower['lastname'] = line_split[1]
                        borrower['books_borrowed'] = line_split[2]
                        borrower['issue_date'] = line_split[3]
                        borrower['returned_status'] = line_split[4]
                        borrower['return_date'] = line_split[5]
                        borrower['price'] = line_split[6]

                        borrowers_list.append(borrower)

                    
                return borrowers_list

        #displays the details of all borrowers using the stored values of dictionary
        def displayBorrowersList(path_to_borrowers):
                borrowers_list = BorrowBook.getBorrowersList(path_to_borrowers)
                print("\n")
                print("\nLibrary Records For Borrow.")
                print("-" * 50)
                        
                for i, person in enumerate(borrowers_list,1):
                                
                        print(f" Borrower Number   : {i}")
                        print(f" * Borrowed By     : {person['firstname']}{person['lastname']}")
                        print(f" * Books           :{person['books_borrowed']}")
                        print(f" * Date of Issue   :{person['issue_date']}")
         
                        if bool(person['returned_status']) == True:
                                print(f" * Returned Status : Not Returned")
                                print(f" * Return Date     :{person['return_date']}")
                                
                        print(f" * Price           :{person['price']}")
                                
                        print("-"*50) 
                print("#"*50)

        #displays the data of the file with the name same as the input 
        def displayBorrower():
                name = input("Enter name of the borrower : ")
                txt_file = "Borrowed By - " + name + ".txt"
                try :
                        with open(txt_file,"r") as file:
                                lines = file.read()
                                print("\n"+lines)
                                print("-"*40)
                                print("#"*40)
                                file.close()
                
                except:
                        print("\nThe borrower is not registered.")


                        
		
	
                 

