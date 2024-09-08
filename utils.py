from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import string
import csv
from typing import Dict, Union, List

nltk.download('stopwords')
nltk.download('punkt_tab')

def proprocess_text(text : str, ignore : str) -> tuple[List[str], Dict[str, Dict[str, int]]]:
    # remove punctuations
    more = '，。！？：；“”‘’《》【】（）……￥——•–'
    translator = str.maketrans('', '', string.punctuation + more + ignore)
    # Remove punctuation using the translate method
    text = text.translate(translator)


    words = word_tokenize(text)
    # Load NLTK stop words
    stop_words = set(stopwords.words('english'))
    more_stop_words = set(open("data/stopwords.txt").read().splitlines())
    # Filter out stop words
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words.union(more_stop_words) and not str.isdigit(word)]

    # build word table
    wordtable = dict()
    for w in filtered_words:
        if w in wordtable:
            wordtable[w]["freq"] += 1
        else:
            wordtable[w] = dict()
            wordtable[w]["freq"] = 1

    return filtered_words, wordtable

def weight(word : str, freq_table : Dict[str, int], wordlist : List[str], focus : int) -> float:
    word = word.lower()
    # return weight based on general frequency and sp wordlist
    if word in freq_table:
        freq = freq_table[word]
    else:
        freq = 12711 # this is the minimum frequency on list

    # normalized by a randomly chosen word from the unigram list
    # magical numbers, feel free to play with them
    w = 596623239/int(freq)
    if word in wordlist:
        return w + focus*2000
    return w

def top_n_words_by_score(data_dict : Dict[str, Dict[str, Union[float, int]]], n : int) -> Dict[str, Dict[str, Union[float, int]]]:
    # Sort the dictionary by the "score" value in descending order
    sorted_words = sorted(data_dict.items(), key=lambda x: x[1]['score'], reverse=True)
    # Extract the top n words
    return dict(sorted_words[:n])

def rank(wordtable : Dict[str, Dict[str, Union[float, int]]], top : int) -> List[str]:
    # return top top words based on weight * frequency
    for word in wordtable:
        wordtable[word]["score"] = wordtable[word]["freq"] * wordtable[word]["weight"]
    return top_n_words_by_score(wordtable, top)


def find_keyaords(ignore="", focus=1, top=10) -> List[str]:

    description = open("job_description.txt", "r", encoding='utf8').read()

    wordlist = open("data/keywordlist.txt", 'r').read().splitlines()
    with open("data/unigram_freq.csv", 'r') as file:
        # Create a CSV reader object
        reader = csv.reader(file)
        # Convert each row into a key-value pair in the dictionary
        freq_table = {rows[0]: rows[1] for rows in reader}

    # content : list[str] 
    # wordtable : dict(str : dict("freq":int))
    content, wordtable = proprocess_text(description, ignore=ignore)

    for word in content:
        wordtable[word]["weight"] = weight(word, freq_table, wordlist, focus=focus)

    return list(rank(wordtable, top=top))


