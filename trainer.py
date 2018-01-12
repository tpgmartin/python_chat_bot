class Trainer(object):

    def __init__(self):
        pass

    def get_or_create(self, text):
        statement = Statement(text)

        return statement

    def train(self, conversation):
        for str in conversation:
            print(str)
