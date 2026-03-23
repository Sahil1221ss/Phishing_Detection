import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# STEP 1: Load dataset
df = pd.read_csv("phishing_email.csv")

# STEP 2: Prepare data
df = df.rename(columns={'text_combined': 'text'})
df = df[['text', 'label']]
df = df.dropna()

# STEP 3: Convert text → numbers
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(df['text'])
y = df['label']

# STEP 4: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# STEP 5: Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# STEP 6: Predict
y_pred = model.predict(X_test)

# STEP 7: Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# FUNCTION TO PREDICT NEW EMAIL
def predict_email(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]
    
    if prediction == 1:
        return "🚨 Phishing Email Detected"
    else:
        return "✅ Safe Email"

# TEST INPUT
while True:
    user_input = input("\nEnter email text (or type 'exit'): ")
    
    if user_input.lower() == 'exit':
        break
    
    result = predict_email(user_input)
    print("Result:", result)