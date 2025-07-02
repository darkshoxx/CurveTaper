Doc = App.getDocument('SharePlinth')

for object in Doc.Objects:
	Doc.removeObject(object.Label)