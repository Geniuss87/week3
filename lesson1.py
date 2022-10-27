# dict
# {'key': 'value'}

#codewars, hackerrank, leetcode

dicts = {
    'name': 'Nazgul',
    'age': 13,
    'subjects': {
        'python': 67,
        'math': 80
    },
}
for i in dicts:
    if type(dicts[i]) == dict:
        for j in dicts[i]:
            print(dicts[i][j])
print(dicts['subjects'])

# python = {
#     "a": 78,
#     "b": 79,
#     "c": 80
# }
# print(sum(python.values()) / len(python))

# def get_dict(dict_one, dict_two, dict_three):
#     new_dict = {}
#     dicts = (dict_one, dict_two, dict_three)
#     for i in dicts:
#         new_dict = i.copy()
#     return new_dict
# result = get_dict({"one": 1}, {"two": 2}, {"three": 3})
# print(result)




