from dataclasses import dataclass

@dataclass   # __init__ 매서드를 내부적으로 자동 생성해준다
             # 'self._변수명'도 자동 생성된다
class Dataset(object):

    # propety : 외부에서 들어오는 값을 담아놓는 '컵'이라고 할 수 있다

    context: str
    fname: str
    train: object
    test: object
    id: str
    label: str

    @property           # Getter
    def context(self) -> str: return self.context

    @context.setter     # Setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self.fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> object: return self.train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object: return self.test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self.id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self.label

    @label.setter
    def label(self, label): self._label = label