# pythonweb
contents of templates folder 
  1. login.html
  2. index.html
  3. bookdetails.html
  4. more.html
  5. layout.html
Contents of static folder
  1. css - contains the stylesheet
  2. images - contains images
  
index.py - contains backend python code

This is a simple website to login, see the list of books and explore more details of the books like Author, publisher. This also provides
a page to read first few pages of the book.

The login is handled using login.html. This is a simple login without any backend validations. This shows the form post method
List of books is displayed using index.html. User can select a book to see more details
bookdetails.html displayes details of the selected book from index.html. It also shows an image and brief description. Clicking on more
will take the user to more.html which shows more details of the book.

All pages has back link and logout link . back will take the user to previous page and logout will take the user back to login page
