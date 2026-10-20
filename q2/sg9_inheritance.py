#create parent class Publication
class Publication:

  #initialize title and author attributes
  def __init__(self, title, author):
    self.__title = str(title)
    self.__author = str(author)

  #getter method for title
  def get_title(self):
    return self.__title

  #getter method for author
  def get_author(self):
    return self.__author

  #setter method for title
  def set_title(self, title):
    self.__title = title

  #setter method for author
  def set_author(self, author):
    self.__author = author

  #display basic info
  def display_info(self):
    print("Title:", self.__title)
    print("Author:", self.__author)

#create child class Book that inherits from parent class Publication 
class Book(Publication):

  #initialize book's title, author, and number of pages
  def __init__(self, title, author, number_of_pages):
    #call the parent class constructor
    super().__init__(title, author)
    
    #set initial page count to 0
    self.__number_of_pages = 0

    #use the setter to validate page count
    self.set_number_of_pages(number_of_pages)

  #getter method for number of pages
  def get_number_of_pages(self):
    return self.__number_of_pages

  #setter method for number of pages
  def set_number_of_pages(self, number_of_pages):
        #check if number of pages isn't negative
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            #display a warning if number of pages is negative
            print("Number of pages must be positive.")

  #display the book's basic info and page count 
  def display_info(self):
    #display title and author using the parent method
    super().display_info()
    #display book's additional attributes
    print("Number of pages: ", self.__number_of_pages)

#create child class Magazine
class Magazine(Publication):

  #initialize title, author, and issue number 
  def __init__(self, title, author, issue_number):
    #call the parent class constructor 
    super().__init__(title, author)
    
    #set intial issue number to 0
    self.__issue_number = 0

    #use setter to validate issue number
    self.set_issue_number(issue_number)

  #getter method for issue number 
  def get_issue_number(self):
    return self.__issue_number

  #setter method for issue number
  def set_issue_number(self, issue_number):
      #check if issue number isn't negative
    if issue_number > 0:
      self.__issue_number = issue_number
    else:
      #display a warning if issue number is negative
      print("Issue number must be positive.")

  #display magazine's basic info and issue number
  def display_info(self):
    #display title and author using parent method 
    super().display_info()

    #display magazine's additional attribute 
    print("Issue number: ", self.__issue_number)

#create 2 objects of the Publication class
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
pub2 = Publication("Science", "Various Authors")

#create 2 objects of the Book class
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Noli Me Tangere", "Jose Rizal", 480)

#create 2 objects of the Magazine class
mag1 = Magazine("The National Geographic", "Various Authors", 202)
mag2 = Magazine("TIME", "TIME Editors", 15)

#display info of 1st publication 
print("Publication Information:")
pub1.display_info()

#display info of 2nd publication
print("\nSecond Publication Information:")
pub2.display_info()

#display info of 1st book
print("\nBook Information:")
book1.set_number_of_pages(-310) #tests validation using an invalid page count 
book1.display_info()
print(book1.get_number_of_pages()) #display page count using getter method 

#display info of 2nd book
print("\nSecond Book Information:")
book2.display_info()

#display info of 1st magazine
print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number()) #display issue number using getter method

#display info of 2nd magazine 
print("\nSecond Magazine Information:")
mag2.display_info()
