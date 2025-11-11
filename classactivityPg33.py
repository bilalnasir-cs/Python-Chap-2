bookList = ["To Kill a Mockingbird","1984","The Great Gatsby","Pride and Prejudice"]
print(bookList)

#Add "Moby Dick" to the book list
bookList.append("Moby Dick")
print(bookList)

# Replace "1984" with  "Brave New World"
bookList[1] = "Brave New World"
print(bookList)

#Remove "The Great Gatsby" from the list
bookList.remove("The Great Gatsby")
print(bookList)

#Second Book list
secondBookList = ["War and Peace","Hamlet"]
print(secondBookList)

#Merge with original list
# bookList.append("War and Peace")
# bookList.append("Hamlet")
# print(bookList)

#Can also merge in another list
finalList = bookList + secondBookList
print(finalList)
