import datetime

class ReturnBook():
    
    def __init__(self, name="", books_borrowed='', issue_date="", returned_status="", return_date="",returned_date = "", price = "", fine = "", total_amount=""):
               
                self.name = name
                self.books_borrowed = books_borrowed
                self.issue_date = issue_date
                self.returned_status = returned_status
                self.return_date = return_date
                self.returned_date = returned_date
                self.price = price
                self.fine = fine
                self.total_amount = total_amount
    

    def returned(self, path_to_return):
                #creation of new text file and writing details on it
                txt_file = "Returned By - " + self.name +".txt"
                file = open(txt_file,'w')

                file.write ("Library Records For Return.\n")
                file.write("-"*40 + "\n")
                file.write(f'Returned By     : {self.name}\n')
                file.write(f'Books Borrowed  : {self.books_borrowed}\n')
                file.write(f'Issue Date      : {self.issue_date}\n')
                file.write(f'Returned Status : {self.returned_status}\n')
                file.write(f'Return Date     : {self.return_date}\n')
                file.write(f'Returned Date   : {self.returned_date}\n')
                file.write(f'Fine            : {self.fine}\n')
                file.write(f'Price           : {self.price}\n')
                file.write(f'Total Amount    : {self.total_amount}\n')
                

                #adding new return to the existing text file
                file = open(path_to_return, 'a')
                file.write(f'{self.name}, {self.books_borrowed}, {self.issue_date}, {self.returned_status}, {self.return_date}, {self.returned_date}, {self.price}, {self.fine}, {self.total_amount} \n')
                file.close()

    
    def getReturnlist(path_to_return):
        return_list = []

        file = open(path_to_return,"r")
        lines = file.readlines()
        

        for line in lines:
            #dictionary used to store data values of the list in pairs
            book_return = {}
            line_split = line.split(",")
            book_return['name'] = line_split[0]
            book_return['books_borrowed'] = line_split[1]
            book_return['issue_date'] = line_split[2]
            book_return['returned_status'] = line_split[3]
            book_return['return_date'] = line_split[4]
            book_return['returned_date'] = line_split[5]
            book_return['price'] = line_split[6]
            book_return['fine'] = line_split[7]
            book_return['total_amount'] = line_split[8]

            return_list.append(book_return)

        return return_list
    
     #displays the details of all returns using the stored values of dictionary
    def displayReturnList(path_to_return):
        
        return_list = ReturnBook.getReturnlist(path_to_return)

        print("\n")
        print("      Library Records For Return.")
        print("-" * 40)
        for i, person in enumerate(return_list,1):
            print(f" Borrower Number   : {i}")
            print(f" * Returned By     : {person['name']}")
            print(f" * Books           :{person['books_borrowed']}")
            print(f" * Date of Issue   :{person['issue_date']}")
 
            if bool(person['returned_status']) == False:
                print(f" * Returned Status : Not Returned")
                
		
            else:
                print(f" * Return Date     :{person['return_date']}")
                print(f" * Returned Status : Returned")
                print(f" * Returned Date   :{person['returned_date']}")
            print(f" * Price           :{person['price']}")
            print(f" * Fine            :{person['fine']}")
            print(f" * Total Amount    :{person['total_amount']}")
            print("-"*40)
        print("#"*40)

    #displays the data of the file with the name same as the input 
    def displayReturn():
        name = input("Enter name of the returner : ")
        txt_file = "Returned By - " + name + ".txt"
        try :
            with open(txt_file,"r") as file:
                lines = file.read()
                print("\n"+lines)
                print("-" * 40)
                print("#"*40)
                file.close()
        except:
            print("\nThe given name is not registered.")
            

    
