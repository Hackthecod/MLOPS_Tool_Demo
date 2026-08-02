import os


with open ("artifacts/text.txt", "r") as f:
    content = f.read()
    print(content)


with open ("artifacts/stage_02.txt", "w") as f:
    f.write("This is a new content written to the file.")