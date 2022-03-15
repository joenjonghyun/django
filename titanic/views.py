from context.domains import Dataset
from context.models import Model

class TitanicView:
    model = Model()
    dataset = Dataset()

    def modeling(self, train, test):
        model = self.model


    def preprocess(self, train, test) -> object:
        self.model = Model()
        self.dataset = Dataset()
        self.train = self.model.new_model(train)
        self.test = self.model.new_model(test)
        # id 추출
        print(f'트레인 컬럼{self.train.columns}')
        print(f'트레인 헤드{self.test.head()}')


