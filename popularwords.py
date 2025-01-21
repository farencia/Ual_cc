
#might have to remove this 

import string
from collections import Counter

def main():
    input_file = 'thestory.txt'
    output_file = 'mostpopularwords.txt'
    edited_file = 'edited_story.txt'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        
        translator = str.maketrans('','', string.punctuation)
        clean_text = text.translate(translator)

        clean_text = clean_text.lower()
        
        words = clean_text.split()
        word_counts = Counter(words)

        most_common_words = word_counts.most_common(10)

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('Top 10 most popular words in the text:\n\n')
            for word, count in most_common_words:
                file.write(f'{word}: {count}\n')

        replacement_map = {word: f"{word}_replaced" for word, _ in most_common_words}
        edited_text = text 
        for word, replacement in replacement_map.items():
            edited_text = edited_text.replace(word, replacement)

            
            edited_text = text.replace("Peter", "Jake");

            with open(edited_file, 'w', encoding='utf-8') as file:
                file.write(edited_text)

        print(f"The words have been replaced, it's saved in  '{edited_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' doesn't exist. Make sure the file is in the same directory as the script.")

if __name__ == '__main__':
    main()



