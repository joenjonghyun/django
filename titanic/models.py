from icecream import ic

from context.domains import Dataset
from context.models import Model


class TitanicModel(object):
    def __init__(self, train_fname, test_fname):
        self.model = Model()
        self.dataset = Dataset()
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # id 추출
        ic(f'트레인 컬럼{self.train.columns}')
        ic(f'트레인 헤드{self.train.head()}')
        ic(self.train)
    def preprocess(self):
        self.sib_sp_garbage()
        self.parch_garbage()
        self.ticket_garbage()
        self.cabin_garbage()
        self.creat_label()
        self.creat_train()
        self.name_nominal()
        self.pclass_ordinal()
        self.age_ratio()
        self.sex_nominal()
        self.embarked_nominal()
        self.fare_ratio()


    def creat_label(self) -> object:
        pass

    def creat_train(self) -> object:
        pass

    def drop_feature(self) -> object:
        pass

    def pclass_ordinal(self) -> object:
        pass

    def name_nominal(self) -> object:
        pass

    def age_ratio(self) -> object:
        pass

    def sib_sp_garbage(self) -> object:
        self.drop_feature()

    def parch_garbage(self) -> object:
        self.drop_feature()

    def ticket_garbage(self) -> object:
        self.drop_feature()

    def sex_nominal(self) -> object:
        pass

    def cabin_garbage(self) -> object:
        self.drop_feature()

    def embarked_nominal(self) -> object:
        pass

    def fare_ratio(self) -> object:
        pass
