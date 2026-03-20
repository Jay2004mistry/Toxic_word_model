# Toxic Comment Detection System

This project is a machine learning-based web application that detects whether a given text is toxic or not. It uses natural language processing (NLP) techniques and a trained classification model to analyze user input and provide a toxicity score.

## 🚀 Features

* Detects toxic and non-toxic comments
* Provides a toxicity score out of 10
* Classifies text as:

  * Non-Toxic
  * Toxic
  * Highly Toxic
* Simple web interface using HTML and CSS
* Backend powered by Flask

## 🧠 Technologies Used

* Python
* Machine Learning (Scikit-learn)
* TF-IDF Vectorization
* Random Forest Classifier
* Flask (Backend)
* HTML & CSS (Frontend)

## 📊 Model Details

* Text preprocessing (cleaning, removing special characters, etc.)
* TF-IDF used for feature extraction
* Multiple models were tested:

  * Logistic Regression
  * Naive Bayes
  * Support Vector Machine
  * Decision Tree
  * Random Forest
* Random Forest achieved the best performance (AUC ≈ 0.80)

## 📁 Project Structure

```
toxic-comment-detector/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── toxic_comment_analysis.ipynb
│
└── templates/
    └── index.html
```

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/toxic-comment-detector.git
```

2. Install dependencies:

```
pip install flask scikit-learn joblib
```

3. Run the application:

```
python app.py
```

4. Open in browser:

```
http://127.0.0.1:5000/
```

## 💡 Example

Input:

```
You are stupid and useless
```

Output:

```
Result: Toxic
Score: 7/10
```

## 🎯 Future Improvements

* Improve UI design
* Add user authentication
* Deploy
