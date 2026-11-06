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

def search_by_genre(cinema: list, genre: str) -> list:
    natija=[]

    for film in cinema:
        if film["genre"]==genre:
            natija.append(film)

    return natija


cinema=[
    {"title": "Avatar", "genre": "Fantastika", "price": 40000},
    {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
    {"title": "Oq yol", "genre": "Drama", "price": 25000},
    {"title": "Dune", "genre": "Fantastika", "price": 35000}
]

print(search_by_genre(cinema, "Fantastika"))

# -----------------------masala-3-------------------------







































