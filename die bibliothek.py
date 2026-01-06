books = []
own_books = input("enter the name of a book your own :\n")
books.append(own_books)

own_books = input(
    "enter the name of another book you own (or press enter to skip):\n")
if own_books:
  books.append(own_books)
print("\nyour library:", books)

wishlist = []
own_books = input( "enter the name of a book you wish to have in the future :\n")
wishlist.append(own_books)
own_books = input("enter the name of another book you wish to have (or press enter to skip):\n")


if own_books:
  wishlist.append(own_books)
print(f"\nyour wishlist: {wishlist}")

acquired_book = input( "enter the name of a book from your wishlist that you´ve acquired (or press enter to skip): \n")

if acquired_book in wishlist:
  books.append(acquired_book)
  print(f"\nyour updated library: {books}")
  wishlist.remove(acquired_book)
  print(f"\nyour updated wishlist: {wishlist}")

donated_books = input("enter the name of a book from your library you wish to donate (or press enter to skip):\n")

if donated_books in books:
  books.remove(donated_books)

print(f"\nfinal library after donnations: {books}")
