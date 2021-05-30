import re
import pysrt
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import RegexpTokenizer

stop_words = set(stopwords.words('english')) 

def main():
    subs = pysrt.open("sample.srt")
    output = ''
    for sub in subs:
        output += ' ' + sub.text.lower()
    tokens = RegexpTokenizer(r'\w+').tokenize(output)
    print('having stopwords: ', len(set(tokens)));
    filtered_tokens = [w for w in tokens if not w in stop_words] 
    print('filtered vocabulary in this movies: ', len(set(filtered_tokens)));
    # print(len(set(filtered_tokens)))
    # print(set(filtered_tokens))
main()
