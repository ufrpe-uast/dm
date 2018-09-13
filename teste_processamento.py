import pandas as pd
import dm.pre_processamento as pp
import dm.classificador as c

from sklearn.metrics import accuracy_score

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier

dataset = pd.read_csv("/home/d/data/opinioes.csv", usecols=['opiniao', 'polaridade'])

ops_tokenizadas = pp.tokenizar(dataset['opiniao'].values)
ops_stopwords = [pp.rem_stopwords(" ".join(o)) for o in ops_tokenizadas]

# Modelos
# MultinomialNB()
# GaussianNB()
# KNeighborsClassifier()
# svm.SVC()
# QuadraticDiscriminantAnalysis()
# MLPClassifier()
# DecisionTreeClassifier()
# RandomForestClassifier()
# GaussianProcessClassifier()

cl = c.classificar(ops_stopwords, dataset['polaridade'].values, pp.tokenizar_string("este candidato é totalmente despreparado"), modelo=GaussianNB())

if cl['pols_pred_teste'][0] == 1:
    print('Positivo')
elif cl['pols_pred_teste'][0] == 2:
    print('Negativo')
else:
    print('Invalido')

acc = accuracy_score(cl['pols_val'], cl['pols_pred_val']) * 100
print('Acuracia: {0:.2f} %'.format(acc))
