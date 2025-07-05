# import pickle
# import os

# model_path = os.path.join(os.path.dirname(__file__), "model")

# with open(os.path.join(model_path, "vectorizer.pkl"), "rb") as f:
#     vectorizer = pickle.load(f)

# with open(os.path.join(model_path, "classifier.pkl"), "rb") as f:
#     classifier = pickle.load(f)

# def classify_query(query, threshold=0.6):
#     vec = vectorizer.transform([query])
#     probs = classifier.predict_proba(vec)[0]
#     max_prob = max(probs)
#     predicted_label = classifier.classes_[probs.argmax()]

#     if max_prob < threshold:
#         return 'general'
#     return predicted_label



import pickle

# Load trained model and vectorizer
with open('chatbot/model/classifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('chatbot/model/vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Function to classify a query
def classify_query(query):
    # Transform the query using the vectorizer
    query_vec = vectorizer.transform([query])
    
    # Predict the department
    department = model.predict(query_vec)[0]
    
    return department
