"""
===============================================================================
Module 01: Introduction to Machine Learning & Algorithm Classifications
===============================================================================
Machine Learning (ML) enables computers to learn patterns from data and make
predictions or decisions without being explicitly programmed.

-------------------------------------------------------------------------------
1. SUPERVISED LEARNING
-------------------------------------------------------------------------------
Supervised learning algorithms learn from labeled data where input features (X)
and expected output labels (y) are provided during training.

Types of Supervised Learning:
a) Classification:
   - Used to predict categorical output labels/classes (e.g., Iris species,
     disease diagnosis, spam detection).
   - Algorithms: K-Nearest Neighbors (KNN), Naive Bayes, Decision Trees,
     Random Forest, XGBoost.

b) Regression:
   - Used to predict continuous numerical values (e.g., house prices, temperature,
     sales revenue).
   - Algorithms: Linear Regression, Polynomial Regression.

-------------------------------------------------------------------------------
2. UNSUPERVISED LEARNING
-------------------------------------------------------------------------------
Unsupervised learning algorithms learn underlying patterns and structures from
unlabeled data without predefined target labels.
- Examples: Customer Segmentation, Anomaly Detection.
- Algorithms: K-Means Clustering, PCA.

-------------------------------------------------------------------------------
3. K-NEAREST NEIGHBORS (KNN) ALGORITHM THEORY
-------------------------------------------------------------------------------
KNN is a non-parametric, supervised learning algorithm used for classification and
regression.

How KNN Works:
1. Calculates the distance (Euclidean distance) between a new input data point (x1, y1)
   and all existing points (x2, y2) in the training dataset.
2. Euclidean Distance Formula:
   Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
3. Selects the 'k' nearest neighbors.
4. Performs a majority vote among the k neighbors to classify the new point.
===============================================================================
"""

print("=== Machine Learning Foundations & Theory Loaded ===")
print("Topics Covered: Supervised vs Unsupervised, Classification vs Regression, KNN & Euclidean Distance.")
