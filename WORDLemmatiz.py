from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
print("rocks:",lemmatizer.lemmatize("rocks"))
print("buckets:",lemmatizer.lemmatize("buckets"))
print("better:",lemmatizer.lemmatize("better",pos="a"))
print("stonger:",lemmatizer.lemmatize("stronger",pos="a"))

