class WordFilter(object):
    def __init__(self, word_list):
        self.ng_list = word_list

    def detect(self, text):
        for ng in self.ng_list:
            if ng in text:
                return True
        return False

    def censor(self, text, censor_word):
        text_censored = text
        if self.detect(text):
            for ng in self.ng_list:
                text_censored = text_censored.replace(ng, censor_word)
        return text_censored


def main():
    my_filter = WordFilter(["アーセナル", "リバプール"])
    flag = my_filter.censor("昨日のアーセナルの試合アツかった", "<censored>")
    print(flag)

    flag2 = my_filter.censor("昨日のリバプールの試合アツかった", "<censored>")
    print(flag2)

    flag3 = my_filter.censor("昨日のACミランの試合アツかった", "<censored>")
    print(flag3)


if __name__ == "__main__":
    main()
