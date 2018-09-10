steps = [
    ("tfidf", TfidfVectorizer(
                        min_df=1,
                        max_df=.75,
                        analyzer='word',
                        stop_words='english',
                        token_pattern=r'\w{1,}',
                        strip_accents='unicode')),
    ("lr", LogisticRegression(
                        C=1,
                        max_iter=100,
                        solver='saga',
                        random_state=42))
]

pipe = Pipeline(steps)

param_grid = {
    "tfidf__max_features":[500,1000,1500,2000,4000]
}

gs = GridSearchCV(pipe,param_grid,verbose=0,cv=3,return_train_score=True,n_jobs=3)
model = gs.fit(X_train,y_train)