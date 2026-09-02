"""
DEMO 4: Basic Inheritance
=============================================================
Goal: reuse a generic class's attributes/behaviors in a more
specific class, instead of rewriting the same code, using
inheritance and super().__init__().
"""

# -------------------------------------------------
# 1. The generic (parent/base) class
# -------------------------------------------------
class MachineLearningModel:
    def __init__(self, task, train_data, test_data):
        self.task = task
        self.train_data = train_data
        self.test_data = test_data

    def train(self):
        print(f"Training a {self.task} model on {self.train_data}")

    def test(self):
        print(f"Testing the {self.task} model on {self.test_data}")

# -------------------------------------------------
# 2. The specific (child/derived) class
# -------------------------------------------------
# RegressionModel has the same structure as MachineLearningModel
# (it can train() and test()), but it also needs its own extra
# attribute and behavior. Instead of rewriting train/test, it
# INHERITS them from MachineLearningModel.
class RegressionModel(MachineLearningModel):
    def __init__(self, train_data, test_data):
        # super().__init__() runs the parent's __init__ for us,
        # so we don't have to repeat self.task/train_data/test_data.
        super().__init__(task="regression", train_data=train_data, test_data=test_data)
        self.error_function = "r2"   # specific to RegressionModel

    def multicolinearity_test(self):
        print("Running multicolinearity test...")

# -------------------------------------------------
# 3. Using the child class
# -------------------------------------------------
model = RegressionModel(train_data="house_prices_train.csv", test_data="house_prices_test.csv")

print(model.task)              # regression       -> inherited attribute
print(model.error_function)    # r2               -> specific attribute

model.train()                  # inherited method
model.test()                   # inherited method
model.multicolinearity_test()  # specific method

print("-" * 40)

# -------------------------------------------------
# 4. Why we need inheritance
# -------------------------------------------------
# Without inheritance, ClassificationModel would need to copy
# __init__, train(), and test() all over again. With inheritance,
# it only has to add what's DIFFERENT.
class ClassificationModel(MachineLearningModel):
    def __init__(self, train_data, test_data):
        super().__init__(task="classification", train_data=train_data, test_data=test_data)
        self.error_function = "accuracy"

    def confusion_matrix(self):
        print("Building confusion matrix...")

clf_model = ClassificationModel(train_data="spam_train.csv", test_data="spam_test.csv")
clf_model.train()               # inherited from MachineLearningModel
clf_model.confusion_matrix()    # specific to ClassificationModel
