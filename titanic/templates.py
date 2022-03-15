from icecream import ic

from context.domains import Dataset
from context.models import Model
from titanic import TitanicModel


class TitanicTemp(object):
    def __init__(self):
        self.model = Model()
        self.dataset = Dataset()
        self.titanic = TitanicModel(train_fname='train.csv',
                                    test_fname='test.csv')


