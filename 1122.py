def write_text(text, filename):
    #file open mode: w-write, r-read, a-append
    with open(filename, "w") as f:
        f.write(text)

write_text("hello world111","hello.txt")