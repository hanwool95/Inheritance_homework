class Sentence_Box:
    def __init__(self, sentence: str = ""):
        self._sentence = ""
        self._words = []
        self.insert_sentence(sentence)

    def insert_sentence(self, sentence: str):
        self._sentence = sentence
        self._separate_sentence()

    def get_sentence(self) -> str:
        return self._sentence

    def _separate_sentence(self):
        if self._sentence:
            self._words = self._sentence.split(" ")
        else:
            print("Error, Please insert the sentence")

    def get_words(self) -> list:
        return self._words


# 1 Sentence Box 객체를 상속하는 Word_Cleaner 제작.
# stop words list를 추가. stop words list = ["은", "는", "이", "가"]
class Word_Cleaner:
    def __init__(self):
        pass

    # 2 입력한 문장의 단어 개수를 세는 내부 함수 제작
    def get_words_count(self) -> int:
        pass

    # 3 주어진 단어의 끝 문자가 stop_words에 있으면 stop word를 제거하여 반환하는 함수 제작
    def remove_stop_words(self, word: str) -> str:
        pass

    # 4 저장된 문장의 stopword를 제거하는 함수 제작. 3번에서 제작한 함수 응용
    def reform_words(self):
        pass

    # 5 insert_sentence 함수를 새롭게 제작. stop word를 제거하는 과정 추가. 4번에서 제작한 함수 응용.
    def insert_sentence(self, sentence: str):
        pass


def main_process():
    sentence = "안녕하세요 여러분 김한울입니다. 김한울은 학생입니다."
    box = Sentence_Box(sentence)
    print(box.get_words())

    cleaner = Word_Cleaner(sentence)
    print(cleaner.get_words_count())
    print(cleaner.get_words())


if __name__ == '__main__':
    main_process()
