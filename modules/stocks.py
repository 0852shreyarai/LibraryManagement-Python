class Stocks:

    def __init__(self, path_to_stock):
        self.path_to_stock = path_to_stock
        

    def getStocks(self):
        #Creation of array list
        books = []
        file = open(self.path_to_stock, "r")
        lines = file.readlines()

        for line in lines:
            book = {}
            details = line.split(",")
            book["title"] = details[0]
            book["author"] = details[1]
            book["quantity"] = details[2]
            book["price"] = details[3]
            books.append(book)
        file.close()
        return books
   
    
    def getPrice(self, bookname):
        books = self.getStocks()
        #to get the price if the book input and book name in the stock is compared
        for book in books:
            if book["title"] == bookname:
                if int(book['quantity']) > 0:
                    return float(book["price"].split("$")[1].strip())
                  
               
    #displays the details of the stock using the stored values of dictionary                 
    def displayStock(self):
        books = self.getStocks()
        
        print("\n\tList of Books Available.")
        print("-" * 40)
        for i, book in enumerate(books,1):
                        
                        print(f" Book Number : {i}")
                        print(f" * Title     : {book['title']}")
                        print(f" * Author    : {book['author']}")
                        print(f" * Quantity  : {book['quantity']}")
                        print(f" * Price     : {book['price']}")
                        print("-"*40)
        print("#"*40)         
                
    #while issuing a book if the input book name is same as book title in stock quantity is reduced by 1
    def updateStock(self, bookname):

        books = self.getStocks()

        for book in books:
            if book['title'] in bookname:
                book['quantity'] = str(int(book['quantity']) - 1)

        file = open(self.path_to_stock, 'w') 

        for book in books:
            line = f'{book["title"]},{book["author"]},{book["quantity"]},{book["price"]}'
            file.writelines(line)

        file.close()
        
    #while returning a book if the input book name is same as book title in stock quantity is increased by 1    
    def updateAfter(self, bookname):
        books = self.getStocks()

        for book in books:
            if book['title'] in bookname:
                book['quantity'] = str(int(book['quantity']) + 1)

        file = open(self.path_to_stock, 'w') 

        #updated details are written in the file
        for book in books:
            line = f'{book["title"]},{book["author"]},{book["quantity"]},{book["price"]}'
            file.writelines(line)
        file.close()
           
        

