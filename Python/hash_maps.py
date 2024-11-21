# demo_dict = {}
# demo_dict['apple'] = 'red'
# demo_dict['lemon'] = 'yellow'
# demo_dict['carrot'] = 'orange'
# for fruit in demo_dict.keys():
#     print(fruit)

# for fruit_colors in demo_dict.values():
#     print(fruit_colors)
    
# for fruit, fruit_color in demo_dict.items():
#     print(fruit, fruit_color)

# demo_dict.get('carrt', 0)

class Books:
    def __init__(self, id, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.id = id
    
    def __str__(self) -> str:
        return f'{self.id}, {self.title}, {self.author}, {self.genre}'
    
    def getAuthor(self):
        return self.author

book1 = Books("1","Me Before You", "Jojo Moyes", "Romance")
book2 = Books("2","1984", "George Orwell", "Dystopian")
book3 = Books("3","The Great Gatsby", "F. Scott Fitzgerald", "Classic")


books_dict = {
    book1.id : book1,
    book2.id : book2,
    book3.id : book3
}

print(books_dict['1'].getAuthor())
for book in books_dict.items():
    print(book)

