def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_report(file_contents)

def count_words(string):
    return len(string.split())

def count_characters(string):
    chars_count = {}
    for c in string.lower():
        if c in chars_count:
            chars_count[c] += 1
        else:
            chars_count[c] = 1
    
    return chars_count

def print_report(string):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(string)} words found in the document")
    print()
    chars_count = count_characters(string)
    alpa_chars = get_alpha_chars(chars_count)
    alpa_chars.sort(reverse=True, key=sort_on)
    for dict in alpa_chars:
        print(f"The '{dict["letter"]}' character was found {dict["count"]} times")
    
    print("--- End report ---")

def get_alpha_chars(dict):
    result = []
    for k in dict:
        if(k.isalpha()):
            result.append({"letter": k, "count": dict[k]})
    
    return result

def sort_on(dict):
    return dict["count"]

main()