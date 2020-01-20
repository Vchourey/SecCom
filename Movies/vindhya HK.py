# K-Nearest Neighbors (K-NN)

# importing library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing dataset
dataset = pd.read_csv(r"C:\Users\Welcome\Desktop\Vindhya MLHackathon\train.csv")

X_train = dataset.iloc[:, 1:17].values
y_train = dataset.iloc[:, 17:].values

try:
    f = open(r"C:\Users\Welcome\Desktop\Vindhya MLHackathon\write.text", "a+")
    for i in str(X_train):
        f.write(i+"/n")
    f.close()
except EOFError as e:
    print('file not exist', e)

Y_train = y_train.sum(axis=1)


# feature scaling
from sklearn.preprocessing import LabelEncoder,  StandardScaler

le = LabelEncoder()
encoded_series = X_train[X_train[:]]
print(encoded_series.head())

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
# X_test = sc.fit_transform(X_test)




# fitting K-NN with training data and making classifier
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
classifier.fit(X_train, Y_train)

# Predict the test values
Y_pred = classifier.predict(X_train)

# creating confusion martix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_train, Y_pred)
print(cm)

# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('K-NN (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('K-NN (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()
