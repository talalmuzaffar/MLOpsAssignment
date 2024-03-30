# Import necessary libraries
from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Create a Flask app
app = Flask(__name__)

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.json
    features = data['features']
    
    # Make prediction
    prediction = clf.predict([features])[0]
    
    # Map prediction to class label
    class_label = iris.target_names[prediction]
    
    # Return the prediction as JSON response
    return jsonify({'prediction': class_label})

# Define a route for checking the model accuracy (for testing purposes)
@app.route('/accuracy')
def get_accuracy():
    # Make predictions on the test set
    y_pred = clf.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Return accuracy as JSON response
    return jsonify({'accuracy': accuracy})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
