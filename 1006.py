def Open(file_name, mode):
    try:
        file = open(file_name, mode)
    except:
        print("File", file_name, "wasn't opened!")
        return None
    else:
        print("File", file_name, "was opened!")
        return file


# --- а) створення файлу TF17_1 ---
file1_w = Open("TF17_1.txt", "w")

if file1_w is not None:
    file1_w.write("Hello12345World6789!\n")
    file1_w.write("Python2025isGreat!\n")
    file1_w.write("TestFile17Task3\n")
    print("Information was successfully added to TF17_1.txt!")
    file1_w.close()
    print("File TF17_1.txt was closed!")


# --- б) переписування у TF17_2 через TF17_3 ---
file1_r = Open("TF17_1.txt", "r")
file3_w = Open("TF17_3.txt", "w")

if file1_r is not None and file3_w is not None:
    data = file1_r.read()
    digits = "".join(ch for ch in data if ch.isdigit())
    others = "".join(ch for ch in data if not ch.isdigit())

    file3_w.write(digits + others)
    print("Data successfully written to TF17_3.txt!")

    file1_r.close()
    file3_w.close()
    print("Files TF17_1.txt and TF17_3.txt were closed!")


# --- формування TF17_2: по 10 символів у рядку ---
file3_r = Open("TF17_3.txt", "r")
file2_w = Open("TF17_2.txt", "w")

if file3_r is not None and file2_w is not None:
    text = file3_r.read()
    for i in range(0, len(text), 10):
        file2_w.write(text[i:i + 10] + "\n")
    print("Data successfully written to TF17_2.txt!")

    file3_r.close()
    file2_w.close()
    print("Files TF17_3.txt and TF17_2.txt were closed!")


# --- в) зчитування TF17_2 і друк по рядках ---
file2_r = Open("TF17_2.txt", "r")

if file2_r is not None:
    print("\nContents of TF17_2.txt:")
    for line in file2_r:
        print(line.strip())
    file2_r.close()
    print("File TF17_2.txt was closed!")
