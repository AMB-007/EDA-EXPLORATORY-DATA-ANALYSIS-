"""
===============================================================================
Module 01: Probability Theory & Bayes Theorem Foundations
===============================================================================
Naive Bayes classifiers are probabilistic algorithms based on applying Bayes'
theorem with strong (naive) independence assumptions between features.

-------------------------------------------------------------------------------
1. PROBABILITY FUNDAMENTALS
-------------------------------------------------------------------------------
Probability P(Event) = Number of Favorable Outcomes / Total Number of Outcomes

Types of Probability:
a) Marginal Probability P(A):
   - Probability of a single event occurring independently.
   - Example: P(Head) = 1/2 = 0.5.

b) Joint Probability P(A and B) or P(A ∩ B):
   - Likelihood of two events happening together at the same time.
   - Example: P(Student likes Python AND Django).

c) Conditional Probability P(A | B):
   - Likelihood of event A occurring given that event B has already occurred.
   - Formula: P(A | B) = P(A and B) / P(B)

-------------------------------------------------------------------------------
2. BAYES THEOREM FORMULA
-------------------------------------------------------------------------------
P(Target | Features) = [ P(Features | Target) * P(Target) ] / P(Features)

Where:
- P(Target | Features) : Posterior probability
- P(Features | Target) : Likelihood
- P(Target)            : Prior probability
- P(Features)          : Evidence (Marginal probability)
===============================================================================
"""

print("=== Probability Theory & Bayes Theorem Notes Loaded ===")
