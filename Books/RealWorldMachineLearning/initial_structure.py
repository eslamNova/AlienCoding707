### chapter 1

data = load_data("data/people.csv")
model = build_model(data, target="Marital status")
new_data = load_data("data/new_people.csv")
predictions = model.predict(new_data)


###

data = load_data(...)
training_data, testing_data = split_data(data)
model = build_model(training_data, target="Marital status")
true_values = testing_data.extract_column("Marital status")
predictions = model.predict(testing_data)
accuracy = compare_predictions(predictions, true_values)


### chapter 2

def cat_to_num(data):
categories = unique(data)
features = []
for cat in categories:
binary = (data == cat)
features.append(binary.astype("int"))
return features