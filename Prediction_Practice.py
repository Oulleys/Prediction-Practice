from sklearn import tree

#Return a prediction of the person's gender based on their win, loss, draws.

#Wins, Loss, Draws
x = [[320,109,55], [50,2,3], [21, 12, 0], [209, 88, 32], [251, 98, 22], [421, 109, 43]]

#Genders
y = ['male', 'female', 'female', 'male', 'male', 'male']

classifier = tree.DecisionTreeClassifier()

classifier = classifier.fit(x,y)

prediction = classifier.predict([[4, 30, 2]])

print(prediction)