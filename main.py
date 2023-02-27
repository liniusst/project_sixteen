# Lesson 16: Virtual Environments
# python3 -m venv .venv

# source .venv/bin/activate

# Use any of virtual environment option , install random-word package and create shot python script 
# which would print out 5 random word (names must be all capital letter and sorted.)
import logging
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
from random_word import RandomWords
from typing import List

def get_name_surname() -> List[str]:
    values = 0
    while values < 5:
        word = RandomWords()
        name = word.get_random_word()
        surname = word.get_random_word()
        data = sorted([name.capitalize(), surname.capitalize()])
        logging.info(f'Random name and surname: "{data[0]} {data[1]}" - sorted by alphabetic')
        values += 1
    return data

if __name__ == "__main__":
    get_name_surname()
