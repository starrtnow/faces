from abc import ABCMeta, abstractmethod

class Network(metaclass=ABCMeta):

    @abstractmethod
    def train_epoch(self, data):
        pass

DefaultHyper = {
    ''
}