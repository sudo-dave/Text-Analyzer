import string
import regex
alphabet = dict.fromkeys(string.ascii_letters, 0)

def main():
    
    print("Enter input")
    text = input()
    word_list = text.split(" ")



    for letter in alphabet:
        for val  in text:
            if  letter == val:
                alphabet[letter] = alphabet[letter] + 1
                
    print(word_list)
if __name__ == '__main__':
    main()