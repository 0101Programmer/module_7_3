class WordsFinder:
    def __init__(self, *some_files, file_names=None):
        if file_names is None:
            file_names = [*some_files]
            self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        not_allowed = [',', '.', '=', '!', '?', ';', ':', ' - ', '/']
        for file_ in self.file_names:
            str_list = []
            lower_list = []
            split_list = []
            final_list = []
            with open(file_, encoding='utf-8') as file_2:
                for str_ in file_2:
                    str_list.append(str_)
                    for char in not_allowed:
                        for idx, ele in enumerate(str_list):
                            str_list[idx] = ele.replace(char, '')
                for i in str_list:
                    lower_list.append(i.lower())
                for j in lower_list:
                    split_list.append(j.split())
                for ind in split_list:
                    for k in ind:
                        final_list.append(k)
                all_words.update({file_: final_list})
        return all_words

    def find(self, word):
        dict_find = {}
        for name, words in self.get_all_words().items():
            for i, str_ in enumerate(words):
                if word.lower() in str_.lower():
                    dict_find.update({name: i + 1})
                    print(dict_find)
                    break

    def count(self, word):
        dict_count = {}
        num = 0
        for name, words in self.get_all_words().items():
            for str_ in words:
                if word.lower() in str_:
                    num += 1
                    dict_count.update({name: num})
        print(dict_count)


wf = WordsFinder('captain.txt')
print(wf.get_all_words())
wf.find('caPtain')
wf.count('captain')
print()
wf_2 = WordsFinder('goose.txt')
print(wf_2.get_all_words())
wf_2.find('Child')
wf_2.count('CHild')
