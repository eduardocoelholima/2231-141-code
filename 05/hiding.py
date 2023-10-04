"""
file: hiding.py
language: python3
authors: R. Zanibbi, A. Nunes-Harwitt, ben k steele
description: Hide information in a file
purpose: file lecture
"""

def hide( text_file, hidden_word):
    """
    hide: File String -> NoneType
    Effect: Display the file with modifications.
    """
    for current_word in text_file:
       if current_word.strip() == hidden_word:
           print( "---") 
       else:
           print( current_word, end="")








def hide_using_file_name( text_file_name, hidden_word):
    """
    hide_using_file_name: String String -> NoneType
    Effect: Display the file with modifications.
    """
    hide( open( text_file_name), hidden_word)









def test_hide():
    """
    test_hide runs the hide function on several files.
    """
    print( "Testing hide_using_file_name and hide text that is 'not there'")
    hide_using_file_name( "words2.txt", "word0")

    print( "Testing hide_using_file_name and hide text that is 'there once'")
    hide_using_file_name( "words2.txt", "word1")

    print( "Testing hide_using_file_name and hide text that is 'there twice'")
    hide_using_file_name( "words2.txt", "word2")

if __name__ == "__main__":
    test_hide()

