# Chapter 01 - Exercise Questions #


### 1.) How would you define machine learning?

Machine Learning is the practice of feeding a computer a dataset whereby it learns via 
an algorithm without necessarily being programmed.


### 2.) Can you name four types of applications where it shines?

Fraud detection, spam filtering, price prediction, and insurance.

### 3.) What is a labeled training set?

A set of data where the data points are labeled with what they are i.e. Spam vs Ham for emails.

### 4.) What are the two most common supervised tasks?

Classification and regression.

### 5.) Can you name four common unsupervised tasks?

No labels, clustering algorithms, visualization algorithms, dimensionality reduction, anomaly detection. There is also 
association rule learning


### 6.) What type of algorithm would you use to allow a robot to walk in various unknown terrains?

Reinforcement learning

### 7.) What type of algorithm would you use to segment your customers into multiple groups?

Classification algorithm or clustering

### 8.) Would you frame the problem of spam detection as a supervised learning problem or an unsupervised learning problem?

Supervised, as people click spam they label the data and the algorithm starts to learn the patters from what humans determine
to be spam, it can then flag similar types of emails as spam.

### 9.) What is an online learning system?

Feeding data in mini-batch instances such as gradient descent.

### 10.) What is out-of-core learning?

Using an online learning algorithm to trains models on huge datasets that can't fit on one machine's memory.

### 11.) What type of algorithm relies on a similarity measure to make predictions?

Instance-based learning

### 12.) What is the difference between a model parameter and a model hyperparameter?

A parameter is a model variable that be estimated by fitting the given data to the model (it belongs to the data). A hyperparmeter is a parameter
value that is set before the model starts training (it belongs to the algorithm), they cannot be learned via fitting the data to the model.

### 13.) What do model-based algorithms search for? What is the most common strategy they use to succeed? How do they make predictions?

Optimal parameter values, minimizing cost function, their ability to generalize. Searching for  amodel that generalizes well.

### 14.) Can you name four of the main challenges in machine learning?

Insufficient quantity of training data, nonrepresentative training data, poor-quality data, overfitting of data.

### 15.) If your model performs great on the training data but generalizes poorly to new instances, what is happening? Can you name three possible solutions?
Overfitting, simplify, gather more data, reduce noise

### 16.) What is a test set, and why would you want to use it?

A test set is a sample set of the original data that the model has no been exposed to,  we use it to see how well the 
model generalizes to unseen data.

### 17.) What is the purpose of a validation se
t
Model selection and hyperparameter tuning

### 18.) What is the train-dev set, when do you need it, and how do you use it

 A small subset of data taken from the same distribution as the trianing set, but it is not the same used to train the model.
dev/test when trianing data and dev/test data come from different distributions, you use it to decouple variance and data mismatch.

### 19.) What can go wrong if you tune hyperparameters using the test set?

Data leakage, false sense-of security, unbiased evaluation ability, poor realworld performance.

Data snooping bias.