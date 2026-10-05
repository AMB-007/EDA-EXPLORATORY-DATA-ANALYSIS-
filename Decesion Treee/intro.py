# Decision Tree
# ===============

# supervied ml algorithm

# Decesion tree can be used in classification,regression

# dataset >>> input,output


# using this dataset(features and target) we build a tree like structure

# using this data structure we make the predicitions
# ==================================================

# node >> root node, intermediate node

# node >>> features
# leafs >> target classes


# branches
# leaf
# root



# using this data structure we make the predictions
# =================================================

# Age       Ex      pizza       fit/unfit
# 30        no      yes         unfit
# 40        yes     yes         fit
# 35        no      no          fit
# 32        yes     no          fit






# Divide and conquer method
# =========================
#  the top down strategy used to build a tree by splitting  a dataset into smaller based on the features






# impurity always in b/w 0 and 1
# 1 >> target in mixed classes
# 0 >> target remain in single class


# parent entropy
# ---------------


# 0 = 14
# 1 - 9
# p(0) = 0.60
# p(1) = 0.39



# Entropy(S) = p(0)log2p(0)-p(1)log2p(1)



# H(S)=−p(0)log
# 2
# 	​

# H(S)=−p(0)log2​p(0)−p(1)log2​p(1)

# p(0)=0.60

# p(1)=0.39

# H(S)=−0.60log2​(0.60)−0.39log2​(0.39) = 
# −0.60(−0.737)−0.39(−1.360) = 
# = 0.4422+0.5304
# 0.9726