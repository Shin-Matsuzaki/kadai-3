class WordFilter(object):
    def __init__(self, word_list):
        self.ng_list = word_list

    def detect(self, text):
        # NGワードを1つずつ確認
        for ng in self.ng_list:
            # 1つでも合致したらTrueを返す
            if ng in text:
                return True
        return False

    def censor(self, text, censor):
        text_censored = text
        # 1つでもNGワードが見つかれば，replaceを実行
        if self.detect(text):
            for ng in self.ng_list:
                text_censored = text_censored.replace(ng, censor)
        return text_censored


def main():
    ng_word = input('NGワードを入力してください(スペース区切り):')
    ng_list = list(map(str, ng_word.split(' ')))
    censor_word = input('Censorワードを入力してください:')

    my_filter = WordFilter(ng_list)
    flag = my_filter.censor("昨日のアーセナルの試合アツかった", censor_word)
    print(flag)

    flag2 = my_filter.censor("昨日のリバプールの試合アツかった", censor_word)
    print(flag2)

    flag3 = my_filter.censor("昨日のACミランの試合アツかった", censor_word)
    print(flag3)


if __name__ == '__main__':
    main()
