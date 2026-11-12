"""Independent model demonstration on reconstructed public IBM sample."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

df=pd.read_csv(Path(__file__).with_name("spacex_sample_90_reconstructed.csv"))
X=df[["FlightNumber","Year","LaunchSite","Orbit","PayloadMass_kg"]]
y=df["Class"]
pre=ColumnTransformer([
    ("cat",OneHotEncoder(handle_unknown="ignore"),["LaunchSite","Orbit"]),
    ("numeric",StandardScaler(),["FlightNumber","Year","PayloadMass_kg"])
])
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
models={"Logistic regression":LogisticRegression(max_iter=1000),
        "Decision tree":DecisionTreeClassifier(random_state=42),
        "SVM (RBF)":SVC(),
        "KNN (k=5)":KNeighborsClassifier(n_neighbors=5)}
rows=[]
for name,clf in models.items():
    model=Pipeline([("preprocess",pre),("model",clf)])
    model.fit(X_train,y_train)
    pred=model.predict(X_test)
    rows.append({"model":name,"test_accuracy":accuracy_score(y_test,pred),
      "test_balanced_accuracy":balanced_accuracy_score(y_test,pred),
      "test_f1":f1_score(y_test,pred,zero_division=0)})
out=pd.DataFrame(rows)
out.to_csv("model_results_reproduced.csv",index=False)
print(out.to_string(index=False))
