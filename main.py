

class Sentence_Box:
    def __init__(self, sentence: str = ""):
        self._sentence = sentence
        self._words = []
        self.separate_sentence()

    def insert_sentence(self, sentence: str):
        self._sentence = sentence

    def get_sentence(self) -> str:
        return self._sentence

    def separate_sentence(self):
        if self._sentence:
            self._words = self._sentence.split(" ")
        else:
            print("Error, Please insert the sentence")

    def get_words(self) -> list:
        return self._words


#1 Sentence Box 객체를 상속하는 단어 분석 객체 제작.
#stop words list를 inint하면서 추가. stop words list = ["은", "는", "이", "가"]
class Word_Analyzer(Sentence_Box):
    stop_words = ["은", "는", "이", "가"]

    def __init__(self, sentence: str = ""):
        super().__init__(sentence)

    #2 입력한 문장의 단어 개수를 세는 내부 함수 제작
    def get_words_count(self) -> int:
        return len(self._words)

    #3 각 단어의 끝 문자가 stop_words에 있으면 stop word를 제거하는 함수 제작
    def remove_stop_words(self):
        for i, word in enumerate(self._words):
            if word[-1] in self.stop_words:
                self._words[i] = self._words[i][:-1]


def main_process():
    sentence = "안녕하세요 여러분 김한울입니다. 김한울은 학생입니다."
    box = Sentence_Box(sentence)
    print(box.get_words())

    analyzer = Word_Analyzer(sentence)
    print(analyzer.get_words_count())
    analyzer.remove_stop_words()
    print(analyzer.get_words())

if __name__ == '__main__':
    main_process()

