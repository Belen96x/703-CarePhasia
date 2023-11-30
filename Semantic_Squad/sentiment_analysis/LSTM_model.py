# -*- coding: utf-8 -*-
"""remove_stutter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tCuYnFdfIgreoPMO_3ro39X9Miz-_roi
"""

import pandas as pd
from google.colab import files

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import re

# Charger le fichier CSV des patients
df_patients = pd.read_csv('/content/drive/MyDrive/703_Project/patient_data_clean.csv')
print(df_patients)

# Fonction pour supprimer les mots répétés correspondant au bégaiement
def remove_stutter(sentence):
  if isinstance(sentence, str):
    sentence = re.sub(r'\b(\w+)( \1\b)+', r'\1', sentence)
    # Supprimer les groupes de mots (2 mots ou plus) répétés
    sentence = re.sub(r'\b(\w+\s\w+)( \1\b)+', r'\1', sentence)
    return sentence
  else:
    return sentence

# Appliquer la fonction sur la colonne contenant les phrases des patients
df_patients['text'] = df_patients['text'].apply(remove_stutter)

# Afficher le DataFrame modifié
print(df_patients)

# Sauvegarder le DataFrame modifié dans un nouveau fichier CSV
df_patients.to_csv('/content/drive/MyDrive/703_Project/patient_data_clean_nostutter.csv', index=False)

import nltk
nltk.download('stopwords')
nltk.download('wordnet')

"""
# Importation des bibliothèques nécessaires
import pandas as pd
import numpy as np
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split

# Chargement des données
patients_data = pd.read_csv('/content/drive/MyDrive/703_Project/patient_data_clean_nostutter.csv')
control_data = pd.read_csv('/content/drive/MyDrive/703_Project/control_data_clean.csv')

# Ajout d'une colonne 'sentences' pour être cohérent avec votre code existant
patients_data['sentences'] = patients_data['text']
control_data['sentences'] = control_data['text']

# Prédire les sentiments à l'aide de TextBlob
patients_data['sentiment'] = patients_data['sentences'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
control_data['sentiment'] = control_data['sentences'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Convertir les sentiments en labels (positif si sentiment > 0, neutre si sentiment == 0, négatif sinon)
patients_data['label'] = patients_data['sentiment'].apply(lambda x: 'positive' if x > 0 else ('neutral' if x == 0 else 'negative'))
control_data['label'] = control_data['sentiment'].apply(lambda x: 'positive' if x > 0 else ('neutral' if x == 0 else 'negative'))


# Prétraitement du texte
def cleaning(df, stop_words):
    df['sentences'] = df['sentences'].apply(lambda x: ' '.join(x.lower() for x in str(x).split()))
    # Remplacement des chiffres/numéros
    df['sentences'] = df['sentences'].str.replace('\d+', '')
    # Suppression des stop words
    df['sentences'] = df['sentences'].apply(lambda x: ' '.join(x for x in x.split() if x not in stop_words))
    # Lemmatisation
    df['sentences'] = df['sentences'].apply(lambda x: ' '.join([Word(x).lemmatize() for x in x.split()]))
    return df

stop_words = stopwords.words('english')

# Appliquer le nettoyage aux données des patients
patients_cleaned = cleaning(patients_data, stop_words)
# Appliquer le nettoyage aux données du groupe contrôle
control_cleaned = cleaning(control_data, stop_words)

# Réinitialisation de l'index du DataFrame control_cleaned
control_data = control_data.reset_index(drop=True)
control_cleaned = control_cleaned.reset_index(drop=True)



# Génération des embeddings en utilisant un tokenizer
tokenizer = Tokenizer(num_words=100, split=' ')
tokenizer.fit_on_texts(patients_cleaned['sentences'].values)

X_patients = tokenizer.texts_to_sequences(patients_cleaned['sentences'].values)
X_patients = pad_sequences(X_patients)

X_control = tokenizer.texts_to_sequences(control_cleaned['sentences'].values)
X_control = pad_sequences(X_control)

# Labels pour les patients et le groupe contrôle
labels_patients = pd.get_dummies(patients_data['label']).values
labels_control = pd.get_dummies(control_data['label']).values


# Diviser les données en ensembles d'entraînement et de test
# Assurez-vous que vous avez les labels (y_patients et y_control) en conséquence.
X_train_patients, X_test_patients, y_train_patients, y_test_patients = train_test_split(X_patients, labels_patients, test_size=0.2, random_state=42)
X_train_control, X_test_control, y_train_control, y_test_control = train_test_split(X_control, labels_control, test_size=0.2, random_state=42)

# Construction du modèle LSTM
model = Sequential()
model.add(Embedding(100, 30, input_length=X_patients.shape[1]))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(64, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())

# Entraînement du modèle sur les données des patients
model.fit(X_train_patients, y_train_patients, epochs=2, batch_size=32, verbose=1)

# Évaluation du modèle sur les données de contrôle
model.evaluate(X_test_control, y_test_control)
"""

# Importation des bibliothèques nécessaires
import pandas as pd
import numpy as np
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from keras.models import Sequential
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split

# Chargement des données
patients_data = pd.read_csv('/content/drive/MyDrive/703_Project/patient_data_clean_nostutter.csv')
control_data = pd.read_csv('/content/drive/MyDrive/703_Project/control_data_clean.csv')

# Ajout d'une colonne 'sentences' pour être cohérent avec votre code existant
patients_data['sentences'] = patients_data['text']
control_data['sentences'] = control_data['text']

# Prédire les sentiments à l'aide de TextBlob
patients_data['sentiment'] = patients_data['sentences'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
control_data['sentiment'] = control_data['sentences'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Convertir les sentiments en labels (positif si sentiment > 0, neutre si sentiment == 0, négatif sinon)
patients_data['label'] = patients_data['sentiment'].apply(lambda x: 'positive' if x > 0 else ('neutral' if x == 0 else 'negative'))
control_data['label'] = control_data['sentiment'].apply(lambda x: 'positive' if x > 0 else ('neutral' if x == 0 else 'negative'))

# Prétraitement du texte
def cleaning(df, stop_words):
    df['sentences'] = df['sentences'].apply(lambda x: ' '.join(x.lower() for x in str(x).split()))
    # Remplacement des chiffres/numéros
    df['sentences'] = df['sentences'].str.replace('\d+', '')
    # Suppression des stop words
    df['sentences'] = df['sentences'].apply(lambda x: ' '.join(x for x in x.split() if x not in stop_words))
    # Lemmatisation
    df['sentences'] = df['sentences'].apply(lambda x: ' '.join([Word(x).lemmatize() for x in x.split()]))
    return df

stop_words = stopwords.words('english')

# Appliquer le nettoyage aux données des patients
patients_cleaned = cleaning(patients_data, stop_words)

# Appliquer le nettoyage aux données du groupe contrôle
control_cleaned = cleaning(control_data, stop_words)

# Réinitialisation de l'index du DataFrame control_cleaned
control_data = control_data.reset_index(drop=True)
control_cleaned = control_cleaned.reset_index(drop=True)

# Génération des embeddings en utilisant un tokenizer
tokenizer = Tokenizer(num_words=100, split=' ')
tokenizer.fit_on_texts(patients_cleaned['sentences'].values)

X_patients = tokenizer.texts_to_sequences(patients_cleaned['sentences'].values)
X_patients = pad_sequences(X_patients)

X_control = tokenizer.texts_to_sequences(control_cleaned['sentences'].values)
X_control = pad_sequences(X_control)

# Labels pour les patients
labels_patients = pd.get_dummies(patients_data['label']).values

# Diviser les données en ensembles d'entraînement et de test
X_train_patients, X_test_patients, y_train_patients, y_test_patients = train_test_split(X_patients, labels_patients, test_size=0.2, random_state=42)

# Construction du modèle LSTM
model = Sequential()
model.add(Embedding(100, 30, input_length=X_patients.shape[1]))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(64, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())

# Entraînement du modèle sur les données des patients
model.fit(X_train_patients, y_train_patients, epochs=2, batch_size=32, verbose=1)

#Prédiction des sentiments pour les données du groupe contrôle
predictions_control = model.predict(X_control)
predicted_labels_control = [np.argmax(prediction) for prediction in predictions_control]

# Ajouter les prédictions au DataFrame control_data
control_data['predicted_label'] = predicted_labels_control



# Évaluation du modèle sur les données de contrôle
y_test_control = pd.get_dummies(control_data['label']).values
model.evaluate(X_control, y_test_control)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt

# Évaluation du modèle sur les données de contrôle
predictions_control = model.predict(X_control)
predicted_labels_control = [np.argmax(prediction) for prediction in predictions_control]

# Ajouter les prédictions au DataFrame control_data
control_data['predicted_label'] = predicted_labels_control

# Convertir les vraies étiquettes en indices de classe
true_labels_control = [np.argmax(label) for label in y_test_control]

# Définir les noms des catégories
categories = ['negative', 'neutral', 'positive']

# Afficher la matrice de confusion
conf_matrix = confusion_matrix(true_labels_control, predicted_labels_control)
# Créer un DataFrame avec les noms des catégories
confusion_df = pd.DataFrame(conf_matrix, index=categories, columns=categories)

# Afficher la matrice de confusion avec seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_df, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Prédictions')
plt.ylabel('Vraies étiquettes')
plt.title('Matrice de Confusion - Groupe Contrôle')
plt.show()

#print("Matrice de confusion pour le groupe contrôle:")
#print(conf_matrix)



# Définir une correspondance entre les indices de classe et les noms de classe
class_mapping = {0: 'negative', 1: 'neutral', 2: 'positive'}

# Remplacer les indices par les noms de classe dans les vraies étiquettes et les étiquettes prédites
true_labels_control_names = [class_mapping[label] for label in true_labels_control]
predicted_labels_control_names = [class_mapping[label] for label in predicted_labels_control]

# Afficher le rapport de classification avec les noms de classe
class_report_names = classification_report(true_labels_control_names, predicted_labels_control_names)
print("Rapport de classification pour le groupe contrôle:")
print(class_report_names)


# Calculer et afficher la précision, le rappel et la F1-score
precision = precision_score(true_labels_control, predicted_labels_control, average='weighted')
recall = recall_score(true_labels_control, predicted_labels_control, average='weighted')
f1 = f1_score(true_labels_control, predicted_labels_control, average='weighted')

print(f"Précision pour le groupe contrôle: {precision:.4f}")
print(f"Rappel pour le groupe contrôle: {recall:.4f}")
print(f"F1-score pour le groupe contrôle: {f1:.4f}")

# Calculer et afficher la précision globale (accuracy)
accuracy = accuracy_score(true_labels_control, predicted_labels_control)
print(f"Précision globale pour le groupe contrôle: {accuracy:.4f}")

# Correspondance des valeurs prédites aux catégories réelles
# Prédiction des sentiments pour les données du groupe contrôle
predictions_control = model.predict(X_control)
predicted_labels_control = [np.argmax(prediction) for prediction in predictions_control]

# Ajouter les prédictions au DataFrame control_data
control_data['predicted_label'] = predicted_labels_control

label_mapping = {0: 'negative', 1: 'neutral', 2: 'positive'}

# Ajouter une colonne "predicted_category" au DataFrame control_data
control_data['predicted_category'] = control_data['predicted_label'].map(label_mapping)

# Afficher les statistiques de prédiction avec les catégories réelles
print("Statistiques de prédiction pour le groupe contrôle:")
print(control_data['predicted_category'].value_counts())

prediction_counts_control = control_data['predicted_category'].value_counts(normalize=True)

for category, percentage in prediction_counts_control.items():
    print(f"Pourcentage de {category}: {percentage * 100:.2f}%")

# Prédiction des sentiments pour les données des patients
predictions_patients = model.predict(X_patients)
predicted_labels_patients = [np.argmax(prediction) for prediction in predictions_patients]

# Ajouter les prédictions au DataFrame patients_data
patients_data['predicted_label'] = predicted_labels_patients

# Correspondance des valeurs prédites aux catégories réelles
label_mapping = {0: 'negative', 1: 'neutral', 2: 'positive'}

# Ajouter une colonne "predicted_category" au DataFrame patients_data
patients_data['predicted_category'] = patients_data['predicted_label'].map(label_mapping)

# Afficher les statistiques de prédiction avec les catégories réelles pour le groupe des patients
print("Statistiques de prédiction pour le groupe des patients:")
print(patients_data['predicted_category'].value_counts())

prediction_counts_patient = patients_data['predicted_category'].value_counts(normalize=True)

for category, percentage in prediction_counts_patient.items():
    print(f"Pourcentage de {category}: {percentage * 100:.2f}%")

import matplotlib.pyplot as plt
import numpy as np

# Fonction pour afficher un graphique à barres des pourcentages
def plot_percentage_comparison(data_control, data_patients, title):
    categories = data_control.index

    fig, ax = plt.subplots(figsize=(10, 6))

    bar_width = 0.35
    opacity = 0.8

    # Convertir les valeurs en nombres flottants
    data_control = data_control.astype(float)
    data_patients = data_patients.astype(float)

    # Positions des barres pour le groupe contrôle
    positions_control = np.arange(len(categories))

    # Positions des barres pour le groupe de patients (décalées)
    positions_patients = positions_control + bar_width

    rects1 = ax.bar(positions_control, data_control, bar_width, alpha=opacity, color='b', label='Contrôle')
    rects2 = ax.bar(positions_patients, data_patients.tolist(), bar_width, alpha=opacity, color='r', label='Patient')

    ax.set_xlabel('Catégories')
    ax.set_ylabel('Pourcentage')
    ax.set_title(title)
    ax.set_xticks(positions_control + bar_width/2)
    ax.set_xticklabels(categories)
    ax.legend()

    plt.show()

# Afficher un graphique de comparaison des pourcentages pour le groupe contrôle et le groupe de patients
plot_percentage_comparison(prediction_counts_control, prediction_counts_patient, "Comparaison des pourcentages de prédictions")

"""**Interpétration évaluation du modèle :**
La matrice de confusion est une représentation tabulaire des résultats du modèle. Chaque colonne de la matrice représente le nombre d'instances dans une classe prédite, tandis que chaque ligne représente le nombre d'instances dans une classe réelle. Dans ce cas :

    Pour la classe réelle 'negative' :
        Le modèle a prédit 691 instances correctement comme 'negative' (Vrais négatifs).
        Le modèle a prédit 3247 instances de 'negative' comme 'neutral' (Faux positifs).
        Le modèle a prédit 217 instances de 'negative' comme 'positive' (Faux positifs).

    Pour la classe réelle 'neutral' :
        Le modèle a prédit 16 instances de 'neutral' comme 'negative' (Faux négatifs).
        Le modèle a prédit 19590 instances correctement comme 'neutral' (Vrais positifs).
        Le modèle a prédit 21 instances de 'neutral' comme 'positive' (Faux positifs).

    Pour la classe réelle 'positive' :
        Le modèle a prédit 132 instances de 'positive' comme 'negative' (Faux négatifs).
        Le modèle a prédit 4608 instances de 'positive' comme 'neutral' (Faux négatifs).
        Le modèle a prédit 1865 instances correctement comme 'positive' (Vrais positifs).

Rapport de classification :

yaml

              precision    recall  f1-score   support
    negative       0.82      0.17      0.28      4155
     neutral       0.71      1.00      0.83     19627
    positive       0.89      0.28      0.43      6605

    Précision : La proportion d'instances correctement prédites parmi toutes les instances prédites pour une classe donnée. Par exemple, pour la classe 'negative', 82% des instances prédites comme 'negative' sont réellement 'negative'.

    Rappel (Recall) : La proportion d'instances correctement prédites parmi toutes les instances réelles de la classe. Par exemple, pour la classe 'neutral', 100% des instances réelles de 'neutral' ont été correctement prédites.

    F1-score : La moyenne pondérée de la précision et du rappel. C'est une mesure globale de la performance du modèle.

    Support : Le nombre total d'instances pour chaque classe.

Moyennes globales :

markdown

    accuracy                           0.73     30387
   macro avg       0.81      0.48      0.51     30387
weighted avg       0.77      0.73      0.67     30387

    Précision globale (Accuracy) : La proportion d'instances correctement prédites parmi toutes les instances. Dans ce cas, 72.88% des prédictions du modèle sont correctes.

    Macro avg : La moyenne non pondérée des métriques par classe.

    Weighted avg : La moyenne pondérée des métriques par classe, pondérée par le nombre d'instances de chaque classe.

En résumé, le modèle semble avoir une précision élevée pour la classe 'neutral', mais il a des difficultés à prédire correctement les classes 'negative' et 'positive'. La faible précision pour 'negative' est probablement due à un grand nombre de faux positifs, tandis que la faible précision pour 'positive' est due à un grand nombre de faux négatifs. Cela peut être exploré davantage pour comprendre les raisons spécifiques de ces erreurs et améliorer le modèle en conséquence.
"""
