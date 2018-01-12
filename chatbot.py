from trainer import Trainer

class ChatBot(object):

    def __init__(self, name):
        self.name = name
        self.trainer = Trainer()

    @property
    def train(self):
        return self.trainer.train

    def get_response(self):
        pass
