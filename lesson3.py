#1 list comprehentions
#generator spiskov

# number_list = [i if i % 100 != 0 else "Null" for i in range(1, 1001) if i % 2 == 0]
# print(number_list)

# lists = ["apple", "banana", "cherry", "orange"]
# new_list = [f[:3] if f != "banana" else "potato"[:3] for f in lists]
# print(new_lis

# number_id = [ord(i) for i in "Python"]
# chars = [chr(i) for i in number_id]
# print(number_id)
# print("".join(chars))

#2 date

# from datetime import timedelta, datetime
# before = datetime.now()
# def find_outlier(ints):
#     odd_count = 0
#     even_count = 0
#     for i in range(len(ints)):
#         if ints[i] % 2 == 0:
#             even_count += 1
#             even = ints[i]
#         else:
#             odd_count += 1
#             odd = ints[i]
#     if even_count < odd_count:
#         return even
#     else:
#         return odd
# # def find_outlier(int):
# #     odds = [x for x in int if x%2!=0]
# #     evens= [x for x in int if x%2==0]
# #     return odds[0] if len(odds)<len(evens) else evens[0]
# result = find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])
# print(result)
# now = datetime.now() - before
# print(now)
# #
# # before = datetime.now()
# # lists = []
# # for i in range(1, 10001):
# #     lists.append(i)
# # now = datetime.now() - before
# # print(now)

# before = datetime.now()
# number_lis = [i for i in range(1, 10001)]
# now = datetime.now() - before
# print(now)

#git
# git --version
# git init
# git status
# git add lesson1.py
# git status
# git add .
#git rm -r --cached .idea
# ls -la
# git commit -m "Added all files from week3"
# git config --global user.name "Geniuss87"
# git config --global user.email "ashyrov.n@mail.ru"
# git config - -list
# git remote add origin https: // github.com / Geniuss87 / test.git
# git remote
# git remote remove origin
# git pull origin main
# git push origin master

# from datetime import timedelta, datetime
# before = datetime.now()
#
# print(r)
# now = datetime.now() - before
# print(now)

s = "HjKoPlY"
for i in range(len(s)):
    print((s[i] * (i + 1)).capitalize())

for i, c in enumerate(s):
    print(c.upper() + c.lower() * i)

for i, c in enumerate(s, 1):
    print((c * i).title())

# f = "the-stealth-warrior"
# l = ""
# for i in range(len(f)):
#     if f[i] == "-" or f[i] == "_":
#         f[i + 1].upper()
#     if f[i] != "-" and f[i] != "_":
#         l = l + f[i]
#
# print(l)

