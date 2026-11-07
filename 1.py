# -----------------------masala-1-------------------------

# def majority_element(nums: list) -> int:
#     natija=-1
#     son=0

#     for i in nums:
#         if nums.count(i) > son:
#             son=nums.count(i)
#             natija=i

#     return natija


# nums=[2, 2, 1, 1, 1, 2, 2]
# print(majority_element(nums))

# -----------------------masala-2-------------------------

# def search_by_genre(cinema: list, genre: str) -> list:
#     natija=[]

#     for film in cinema:
#         if film["genre"]==genre:
#             natija.append(film)

#     return natija


# cinema=[
#     {"title": "Avatar", "genre": "Fantastika", "price": 40000},
#     {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
#     {"title": "Oq yol", "genre": "Drama", "price": 25000},
#     {"title": "Dune", "genre": "Fantastika", "price": 35000}
# ]

# print(search_by_genre(cinema, "Fantastika"))

# -----------------------masala-3-------------------------

# def merge_unique_ids (a:list,b:list)->list:
#     c=a+b
#     new=[]
#     for x in c:
#         if x not in new:
#             new.append(x)
#     print(new)
        

# a = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001'] 
# b = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']
# merge_unique_ids(a,b)

# -----------------------masala-4-------------------------

# def sorted_by_price(a: list) -> list:
#     natija = sorted(a, key=lambda x: int(x[1]), reverse=True)
#     return natija


# products = [
#     ('Olma', '12000', '50'),
#     ('Banan', '8000', '100'),
#     ('Gilos', '15000', '70'),
#     ('Apelsin', '9000', '80'),
#     ('Anor', '30000', '20'),
#     ('Uzum', '20000', '40'),
#     ('Tarvuz', '25000', '15'),
#     ('Shaftoli', '18000', '60'),
#     ('Qovun', '40000', '25'),
#     ('Qulupnay', '35000', '10')
# ]

# print(sorted_by_price(products))
































