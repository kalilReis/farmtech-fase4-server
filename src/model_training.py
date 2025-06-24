
import pandas as pd
import numpy as np
import oracledb
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

import os
from dotenv import load_dotenv
import oracledb
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

load_dotenv()

dsn = os.getenv("DB_DSN")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

def load_data_from_db():
    connection = oracledb.connect(user=user, password=password, dsn=dsn)
    cursor = connection.cursor()
    query = """
        SELECT timestamp, sensor_id, soil_moisture, humidity, phosphorus, potassium
        FROM irrigation_data
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0].lower() for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    cursor.close()
    connection.close()
    return df

df = load_data_from_db()

# Simular coluna alvo: necessidade de irrigação (1 = irrigar, 0 = não irrigar)
# Exemplo: irrigar se soil_moisture < 30 ou potassium < 20 ou humidity < 65 ou phosphorus < 18
df['irrigate'] = (
    (df['soil_moisture'] < 30) |
    (df['potassium'] < 20) |
    (df['humidity'] < 65) |
    (df['phosphorus'] < 18)
).astype(int)

# Features e target
X = df[['soil_moisture', 'humidity', 'phosphorus', 'potassium', 'sensor_id']]
y = df['irrigate']

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Avaliação
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# Salvar modelo
joblib.dump(clf, '../data/irrigation_model.joblib')
