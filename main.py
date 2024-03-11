def main():
    filepath = "books/frankenstein.txt"
    document = read_document(filepath)
    print(f"{words(document)} words found in the document.")
    print(f"There are {count_letters(document)} letters in the document.")
    

def read_document(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents
        

def words(contents):
    word_count = contents.split()
    return len(word_count)

def count_letters(contents):
    letter_count = [{"letter" : "num"}]
    lowercase_content = contents.lower()
    for letter in lowercase_content:
        if letter in letter_count:
            letter_count ["letter":"num"] +=1
        else:
            letter_count["letter":"num"] = 1
    letter_count.sort(key=letter_count["num"])
    return letter_count
main()
