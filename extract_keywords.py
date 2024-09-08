from utils import find_keyaords

"""
[For personal use only]

Instructions
- copy and paste the job descriptions or additional information to job_description.txt
- (optional) play with the paramaters
    - change focus, top and ignore below
    - to specifically ignore certain words, edit data/stopwords.txt
    - edit the data/keywordlist.txt if necessary
- run this file

"""



if __name__ == "__main__":
    """
    focus: how much emphasize to put on the words from keyword list (0-10)
    top: return the top n important words
    ignore: additional tokens to ignore, like special punctuations if they spoil the result
    to specifically ignore certain words, edit data/stopwords.txt 
    """
    keywords = find_keyaords(focus=1, top=20, ignore="")
    print(keywords)