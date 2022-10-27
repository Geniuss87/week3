# set

student = {
    "name": "Nazgul",
    "age": 18,
    "year": None,
    "subject": {
        "math": (80, 90, 50),
        "python": (56, 88, 90),
        "html": (76, 93, 55),
        "css": (76, 67, 87)
    },
    "total": None
}
# subtotal = []
# for i in student:
#     if i == "year":
#         student[i] = 2022 - student["age"]
#     if type(student[i]) == dict:
#         for j in student[i]:
#             subtotal.append(sum(student[i][j]) / len(student[i][j]))
#             student[i][j] = int(sum(student[i][j]) / len(student[i][j]))
#     if i == "total":
#         student[i] = int(sum(subtotal) / len(subtotal))
# print(student)

for key, value in student["subject"].items():
    student["subject"][key] = sum(value) / len(value)
student["total"] = sum(student["subject"].values()) / len(student["subject"])
print(student)



