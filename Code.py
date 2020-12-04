import nltk
nltk.download('stopwords') # WORDS LIKE  I THE AM
nltk.download('popular')   # A COMMON DATASET
import re

with open('E:/Python1/Similar projects/1/sensorics.txt', 'r',encoding="utf8") as file:
    s = file.read().replace('\n', '')
print(s)
s = ''.join([i for i in s if not i.isdigit()])
s = re.sub(r'[^A-Za-z0-9 /\.,]+','', s)  # Cleaning because of bad pdf data

## Making the string length less for processing times

len(s)
s = s[10000:15000]


from summarizer import Summarizer
model = Summarizer()
result = model(s, min_length=60, max_length = len(s) , ratio = 0.6)
summarized_text = ''.join(result)
print (summarized_text)



import pke #Python keyword extraction
import string
from nltk.corpus import stopwords

def get_nouns(text):
    out=[]

    extractor = pke.unsupervised.MultipartiteRank()
    extractor.load_document(input=text)
   
    pos = {'PROPN','NOUN'} #Because these are the answers mostly
    # Igonring the left out puncuations from data cleaning
    stoplist = list(string.punctuation)
    stoplist += ['-lrb-', '-rrb-', '-lcb-', '-rcb-', '-lsb-', '-rsb-','x'] 
    stoplist += stopwords.words('english')
    extractor.candidate_selection(pos=pos, stoplist=stoplist)
    
    extractor.candidate_weighting(alpha=1.1,
                                  threshold=0.75,
                                  method='average')
    keyphrases = extractor.get_n_best(n=30)
    for key in keyphrases:
        out.append(key[0])
    return out

keywords = get_nouns(s) 
print (keywords)
filtered_keys=[]

for keyword in keywords:
    if keyword.lower() in summarized_text.lower():
        filtered_keys.append(keyword)
        
print (filtered_keys)

from nltk.tokenize import sent_tokenize
from flashtext import KeywordProcessor

def tokenize_sentences(text):
    sentences = [sent_tokenize(text)]
    sentences = [y for x in sentences for y in x]
    # Remove any short sentences less than 20 letters.
    sentences = [sentence.strip() for sentence in sentences if len(sentence) > 20]
    return sentences

# Finding sentences for keywords and combiling them
def get_sentences_for_keyword(keywords, sentences):
    keyword_processor = KeywordProcessor()
    keyword_sentences = {}
    for word in keywords:
        keyword_sentences[word] = []
        keyword_processor.add_keyword(word)
    for sentence in sentences:
        keywords_found = keyword_processor.extract_keywords(sentence)
        for key in keywords_found:
            keyword_sentences[key].append(sentence)

    for key in keyword_sentences.keys():
        values = keyword_sentences[key]
        values = sorted(values, key=len, reverse=True)
        keyword_sentences[key] = values
    return keyword_sentences

sentences = tokenize_sentences(summarized_text)

keyword_sentence_mapping = get_sentences_for_keyword(filtered_keys, sentences)  
print(keyword_sentence_mapping.keys())
print (keyword_sentence_mapping.values())
print(filtered_keys)

from gensim.models import KeyedVectors

glove_file = 'E:/Python1/Similar projects/1/data/embeddings/glove.6B.300d.txt'
tmp_file = 'E:/Python1/Similar projects/1/data/embeddings/word2vec-glove.6B.300d.txt'

from gensim.scripts.glove2word2vec import glove2word2vec
glove2word2vec(glove_file, tmp_file)
model = KeyedVectors.load_word2vec_format(tmp_file)


def generate_distractors(answer, count):
    answer = str.lower(answer)
    
    ##Extracting closest words for the answer. 
    try:
        closestWords = model.most_similar(positive=[answer], topn=count)
    except:
        #In case the word is not in the vocabulary, or other problem not loading embeddings
        return []

    #Return count many distractors
    distractors = list(map(lambda x: x[0], closestWords))[0:count]
    
    return distractors

## MCQS
for key in keyword_sentence_mapping.keys():
    for value in keyword_sentence_mapping.values():
        for a in value:
            if key in a:
                key.lower()
                str1 = "".join(a)
                lkey = key.lower()
                lstr1 = str1.lower()
                print(lstr1.replace(lkey,"________"))
                print('A)',key.upper())
                print(generate_distractors(lkey, 8))
                print('\n')
              
                

    
