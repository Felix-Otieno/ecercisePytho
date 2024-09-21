import pickle

# phoneBook = {
#     "a":"1",
#     "b":"2",
#     "c":"3"
# }

# with open('binary/phoneBook.dat', 'wb') as bin:
#     pickle.dump(phoneBook, bin)

with open('binary/phoneBook.dat', 'rb') as bin:
    data = pickle.load(bin)
    print(data)

