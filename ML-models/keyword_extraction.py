from newspaper import fulltext
import requests
from nltk.tokenize import regexp_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from yake import KeywordExtractor

def get_full_text_from_url(url):
    response = requests.get(url)
    html = response.text
    return fulltext(html)

def clean_data(text, lang):
    tokens = regexp_tokenize(text, r'\w+')
    lemmatizer = WordNetLemmatizer()
    tokens_no_stop = [lemmatizer.lemmatize(t.lower(), pos='a') for t in tokens if t not in stopwords.words(lang)]
    clean_text = " ".join(tokens_no_stop)
    return clean_text

def get_keywords(text, lang):
    extractor = KeywordExtractor(lan=lang, n=3, top=10)
    return extractor.extract_keywords(text)

def main():
    url = input("Enter URL: ")
    text = get_full_text_from_url(url)
    clean_text = clean_data(text, 'english')
    keywords = get_keywords(text, 'en')
    print(keywords)
    
if __name__=="__main__":
    main()