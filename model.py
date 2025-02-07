import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Reading the data
iris = sns.load_dataset('iris')
print(iris.columns)  # Check column names
y = iris['species']
iris.drop(columns='species', inplace=True)
x = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]  # Corrected column names

# Training the model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
model = LogisticRegression(max_iter=100)
model.fit(x_train, y_train)

pickle.dump(model, open('model.pkl', 'wb'))
