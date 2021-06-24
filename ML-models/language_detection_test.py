import pickle5 as pickle

model = pickle.load(open('language_detection_model.sav', 'rb'))
vectorizer = pickle.load(open('language_detection_dict.sav', 'rb'))
encoder = pickle.load(open('language_detection_classes.sav', 'rb'))

print(model)
print(vectorizer)
print(encoder)

text = input("Enter text: ")
X = vectorizer.transform([text]).toarray()
lang = model.predict(X)
lang = encoder.inverse_transform(lang)
print(lang)