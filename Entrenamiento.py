import pandas as pd
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from colorama import init, Fore, Back, Style

#* Inicializar colorama
init()

#* Cargar los datos (usando pandas)
data = pd.read_csv('DATOS/featuresFC6.csv')
X = data.iloc[:, :-1] #! Todas las columnas a excepcion de la ultima
y = data.iloc[:, -1] #! Ultima columna

#* Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

#* Crear y entrenar modelos
mlp = MLPClassifier(hidden_layer_sizes=(64, 64), max_iter=1000)
mlp.fit(X_train, y_train)

tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

#* Predecir en los conjuntos de prueba
mlp_pred = mlp.predict(X_test)
tree_pred = tree.predict(X_test)
svm_pred = svm.predict(X_test)

#* Calcular la precisión de cada modelo
mlp_acc = accuracy_score(y_test, mlp_pred)
tree_acc = accuracy_score(y_test, tree_pred)
svm_acc = accuracy_score(y_test, svm_pred)

print(Fore.RED + "Precisión de la red neuronal: ", mlp_acc)
print(Fore.GREEN + "Precisión del árbol de decisión: ", tree_acc)
print(Fore.BLUE + "Precisión del SVM: ", svm_acc)