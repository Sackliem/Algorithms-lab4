from abc import abstractmethod, ABC


class BaseSort(ABC):
    def __init__(self):
        self.words = []
        self.word_count = {}

    @abstractmethod
    def sort(self):
        pass

    @abstractmethod
    def count_words(self):
        pass

