class WordFilter(object):
    def __init__(self, word):
        self.ng = word

    def detect(self, text):
        return self.ng in text


def main():
    my_filter = WordFilter('アーセナル')
    flag = my_filter.detect("昨日のアーセナルの試合アツかった")
    print(flag)

    flag2 = my_filter.detect("昨日のリバプールの試合アツかった")
    print(flag2)


if __name__ == "__main__":
    main()
