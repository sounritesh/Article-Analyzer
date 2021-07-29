# Article-Analyzer
### Description
It is a tool to analyze articles online. It takes article text or URL as input and processes the article and produces a word cloud, extracts keywords, produces a summary and calculates the word count. It leverages techniques like **web scraping, data cleaning, text preprocessing, tokenization, text summarization and classification**.

It supports 9 languages which includes **English, Arabic, German, French, Portuguese, Italian, Spanish, Dutch and Turkish**.

The end to end application is made using **Django** and is deployed using **Heroku**.

### Working
One of the primary functions of the tool is **to detect the language of the text**.
It uses **Mutinomial Naive Bayes model** trained using a [language dataset](https://www.kaggle.com/basilb2s/language-detection) that contains data samples for 17 languages. The model is implemented using the [Scikit-Learn](https://scikit-learn.org/stable/) library.

Models are dumped and loaded for use in the Django app using [Pickle](https://pypi.org/project/pickle5/).

Although the classifier can detect 17 languages, due to the limitations of the keyword extractor used, the tool can only support 9 of these languages. **Keyword extraction** is implemented using [yake](https://github.com/LIAAD/yake) which is fed with the text and language detected.

The **word cloud** is produced using [Zingcharts' word cloud](https://www.zingchart.com/docs/chart-types/wordcloud). It is fed **clean data** to do so. The raw text is tokenized, lemmatized and ridded of stopwords. This **text preprocessing** is done using [NLTK](https://www.nltk.org/).

The **text summarization** is done using **Text Rank** algorithm where in the sentences in the article are represented as nodes in a graph and ranked on the basis of **cosine similarity** using **Page Rank**. This is done with the help of [NLTK](https://www.nltk.org/) and [Networkx](https://networkx.org/).

### Getting Started
To get a copy of the project up and running, go to the [django-app](https://github.com/sounritesh/ai-article-analyzer/tree/f90962e955f698ac8249ed09f9a0b5d2a726d696) submodule.

#### Requirements
All libraries required to get the models trained can be installed from **requirements.txt** file inside the **ML-models** folder. To get the project up and running, training the models is not required as they are already saved for the django project.

### Author
[Ritesh Soun](https://github.com/sounritesh/)
