def main():
    filepath = "books/frankenstein.txt"
    document = read_document(filepath)
    print(f"{words(document)} words found in the document.")
    print("")
    count_letters(document)
    

def read_document(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents
        

def words(contents):
    word_count = contents.split()
    return len(word_count)

def count_letters(contents):
    letter_count = {}
    lowercase_content = contents.lower()
    for letter in lowercase_content:
        if letter in letter_count:
            letter_count [letter] +=1
        else:
            letter_count[letter] = 1
    list_of_letter_dicts = [letter for letter in letter_count.items()]
    list_of_letter_dicts.sort(key=lambda item: item[1])
    for item in list_of_letter_dicts:
        print(f"The letter '{item[0]}' appears {item[1]} times in the document.")
    
main()
