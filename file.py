with open("asdf.txt", "r") as f:
    quiz_dict = dict(line.strip().split(", ") for line in f)

print(quiz_dict)
