import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn.metrics import accuracy_score

# Define the file path
file_path = 'spam.csv'

# Load data from the CSV file
spam = pd.read_csv(file_path)
# Print the column names to verify their names
print("Column names in the dataset:", spam.columns)
# Use the appropriate column names based on your data
z = spam['v2']  # Update to the correct column name for email text
y = spam['v1']  # Update to the correct column name for labels
# Split the data into training and test sets
z_train, z_test, y_train, y_test = train_test_split(z, y, test_size=0.2, random_state=42)
# Create a CountVectorizer to convert text data to numerical data
cv = CountVectorizer()
# Fit the vectorizer on the training data and transform it
features_train = cv.fit_transform(z_train)
# Create an SVM model with a linear kernel
model = svm.SVC(kernel='linear')
# Train the model using the training data
model.fit(features_train, y_train)
# Transform the test data using the same vectorizer
features_test = cv.transform(z_test)
# Predict labels for the test data using the trained model
y_pred = model.predict(features_test)
# Count the total number of messages and the number of spam messages
total_messages = len(z_test)
spam_messages = sum(y_pred == 'spam')

# Display each message and its classification (spam or not spam)
print("Messages and their classifications:")
for idx, message in enumerate(z_test):
    classification = "spam" if y_pred[idx] == 'spam' else "not spam"
    print(f"Message: {message}")
    print(f"Classification: {classification}\n")

# Display the total number of messages and the count of spam messages
print(f"Total number of messages: {total_messages}")
print(f"Number of spam messages: {spam_messages}")
# Evaluate the model's performance using accuracy score
accuracy = accuracy_score(y_test, y_pred)
# Convert accuracy to percentage
accuracy_percentage = accuracy * 100
# Print the accuracy in percentage
print(f"Accuracy: {accuracy_percentage:.2f}%")
