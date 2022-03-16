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
        df = self.train

        df = self.drop_feature(df)
        df = self.creat_label(df)
        df = self.creat_train(df)
        df = self.name_nominal(df)
        df = self.pclass_ordinal(df)
        df = self.age_ratio(df)
        df = self.sex_nominal(df)
        df = self.embarked_nominal(df)
        df = self.fare_ratio(df)

    @staticmethod
    def creat_label(df) -> object:
        return df

    @staticmethod
    def creat_train(df) -> object:
        return df

    def drop_feature(self, df) -> object:
        self.sib_sp_garbage(df)
        self.parch_garbage(df)
        self.ticket_garbage(df)
        self.cabin_garbage(df)
        return df

    '''
       Categorical vs. Quantitative
       Cate -> nominal (이름) vs. ordinal (순서)
       Quan -> interval (상대) vs. ratio (절대)
    '''

    @staticmethod
    def pclass_ordinal(df) -> object:
        return df

    @staticmethod
    def name_nominal(df) -> object:
        return df

    @staticmethod
    def age_ratio(df) -> object:
        return df

    @staticmethod
    def sex_nominal(df) -> object:
        return df

    @staticmethod
    def embarked_nominal(df) -> object:
        return df

    @staticmethod
    def fare_ratio(df) -> object:
        return df
