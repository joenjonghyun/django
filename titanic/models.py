from icecream import ic

from context.domains import Dataset
from context.models import Model


class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']

        this.train = this.train.drop('Survived', axis=1)
        # id 추출
        # ic(f'트레인 컬럼{self.train.columns}')
        # ic(f'트레인 헤드{self.train.head()}')
        # ic(self.train)
        this = self.drop_feature(this, 'SibSp', 'Parch', 'Ticket', 'Cabin')
        '''
        this = self.creat_this(self.dataset)
        self.print_this(this)
        this = self.creat_train(this)
        this = self.name_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.age_ratio(this)
        this = self.sex_nominal(this)
        this = self.embarked_nominal(this)
        this = self.fare_ratio(this)
        '''
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*' * 100)
        ic(f'1. train 의 타입: {type(this.train)}\n')
        ic(f'2. train 의 컬럼: {(this.train.columns)}\n')
        ic(f'3. train 의 상위 1개: {(this.train.head(1))}\n')
        ic(f'4. train 의 null의 갯수: {(this.train.isnull().sum())}\n')
        ic(f'5. test 의 타입: {type(this.test)}\n')
        ic(f'6. test 의 컬럼: {(this.test.columns)}\n')
        ic(f'7. test 의 상위 1개: {(this.test.head(1))}\n')
        ic(f'8. test 의 null의 갯수: {(this.test.isnull().sum())}\n')
        ic(f'9. id 의 타입: {type(this.id)}\n')
        ic(f'10. id 의 상위 10개: {this.id[: 10]}\n')
        print('*' * 100)

    def creat_this(self, dataset) -> object:
        this = dataset
        this.train = self.train
        this.test = self.test
        this.id = self.id
        return this

    @staticmethod
    def drop_feature(this, *feature) -> object:

        for i in feature:
            this.train = this.train.drop(i, axis=1)
            this.test = this.test.drop(i, axis=1)


        '''
        self.sib_sp_garbage(df)
        self.parch_garbage(df)
        self.ticket_garbage(df)
        self.cabin_garbage(df)
        '''
        return this

    '''
       Categorical vs. Quantitative
       Cate -> nominal (이름) vs. ordinal (순서)
       Quan -> interval (상대) vs. ratio (절대)
    '''

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def name_nominal(this) -> object:
        return this

    @staticmethod
    def age_ratio(this) -> object:
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        return this
