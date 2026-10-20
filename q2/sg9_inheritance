#create parent class Publication
class Publication:

  #initialize private attributes
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

#create child class Book
class Book(Publication):

  #initialize private attributes
  def __init__(self, title, author, number_of_pages):
    super().__init__(title, author)
    self.__number_of_pages = 0
    self.number_of_pages = (number_of_pages)

  def get_number_of_pages(self):
    return self.__number_of_pages

  def set_number_of_pages(self, number_of_pages):
        #check if number of pages isn't negative
        if number_of_pages >= 0:
            self.__number_of_pages = number_of_pages
        else:
            #display a warning if number of pages is negative
            print("Number of pages must be positive.")

  def display_info(self):
    super().display_info()
    print("Number of pages: ", self.__number_of_pages)

#create child class Magazine
class Magazine(Publication):
  
  def __init__(self, title, author, issue_number):
    super().__init__(title, author)
    self.__issue_number = 0
    self.set_issue_number(issue_number)

  def get_issue_number(self):
    return self.__issue_number

  def set_issue_number(self, issue_number):
      #check if issue number isn't negative
    if issue_number >= 0:
      self.__issue_number = issue_number
    else:
      #display a warning if issue number is negative
      print("Issue number must be positive.")

  def display_info(self):
    super().display_info()
    print("Issue number: ", self.__issue_number)

#create objects
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("The National Geographic", "Various Authors", 202)

#print info
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
