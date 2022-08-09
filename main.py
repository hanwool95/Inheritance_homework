

class Sentence_Box:
    def __init__(self, sentence: str = ""):
        self.__sentence = sentence
        self.__words = []
        self.separate_sentence()

    def insert_sentence(self, sentence: str):
        self.__sentence = sentence

    def get_sentence(self) -> str:
        return self.__sentence

    def separate_sentence(self):
        if self.__sentence:
            self.__words = self.__sentence.split(" ")
        else:
            print("Error, Please insert the sentence")

    def get_words(self) -> list:
        return self.__words


def main_process():
    box = Sentence_Box("안녕하세요 여러분 김한울입니다.")
    print(box.get_words())

if __name__ == '__main__':
    main_process()

