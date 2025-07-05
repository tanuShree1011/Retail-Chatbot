# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.metrics import accuracy_score
# import pickle

# # Load dataset
# df = pd.read_csv('sample_queries.csv')

# # Prepare data
# X = df['query']  # Features (queries)
# y = df['category']  # Target (departments)

# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Vectorize text data
# vectorizer = TfidfVectorizer(stop_words='english')  # You can try using CountVectorizer as well

# X_train_vec = vectorizer.fit_transform(X_train)
# X_test_vec = vectorizer.transform(X_test)

# # Train a Naive Bayes classifier
# model = MultinomialNB()
# model.fit(X_train_vec, y_train)

# # Save the model and vectorizer
# with open('chatbot/model/classifier.pkl', 'wb') as model_file:
#     pickle.dump(model, model_file)

# with open('chatbot/model/vectorizer.pkl', 'wb') as vectorizer_file:
#     pickle.dump(vectorizer, vectorizer_file)

# # Test and evaluate the model
# y_pred = model.predict(X_test_vec)
# print(f"Accuracy: {accuracy_score(y_test, y_pred)}")




import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle

# Load dataset
df = pd.read_csv('sample_queries.csv')

# Prepare data
X = df['query']  # Features (queries)
y = df['category']  # Target (departments)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize text data
vectorizer = TfidfVectorizer(stop_words='english')

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save the model and vectorizer
with open('chatbot/model/classifier.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('chatbot/model/vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

# Test and evaluate the model
y_pred = model.predict(X_test_vec)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
