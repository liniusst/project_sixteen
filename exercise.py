from random_word import RandomWords
from typing import List
import logging
logging.basicConfig(level=logging.DEBUG,filename='data_edvio.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
random_words = RandomWords()

def generate_random_words(list_length: int) -> List[str]:
    random_words_list=[]
    for i in range(list_length):
        random_words_list.append(random_words.get_random_word())
        sorted_list = sorted(random_words_list)
    logging.info(f"Logged: {[value.upper() for value in sorted_list]}")
    return [value.upper() for value in sorted_list]

print(generate_random_words(5))