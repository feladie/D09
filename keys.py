"""
Write three functions:
sort1(langauges)
sort2(languages)
sort3(langauges)
Goal: Print exactly the below w/ three functions:
1:
    Arabic
    English
    Koine Greek
    Latin
    Romanian
    C++
    JavaScript
    Python
    R
2:
    R
    C++
    Latin
    Arabic
    Python
    English
    Romanian
    JavaScript
    Koine Greek
3:
    JavaScript
    R
    Latin
    Python
    Romanian
    Koine Greek
    English
    Arabic
    C++
"""
languages = {'JavaScript': 'P',
             'Arabic': 'N',
             'R': 'P',
             'Python': 'P',
             'C++': 'P',
             'Koine Greek': 'N',
             'Latin': 'N',
             'Romanian': 'N',
             'English': 'N'}

def sort1(d):
    # lst = sorted(sorted(d), key=d.__getitem__)
    # print('1:')
    # for x in lst:
    #     print('\t' + x)

    import operator
    lst = sorted(sorted(d.items()), key=operator.itemgetter(1))
    print("1: ")
    for language, type_ in lst:
        print('\t' + language)


def sort2(d):
    lst = sorted(d, key=len)
    print("2: ")
    for x in lst:
        print('\t' + x)

def sort3(d):
    lst = sorted(sorted(d), key=last_char, reverse=True)
    print("3: ")
    for x in lst:
        print('\t' + x)

def last_char(string):
    return string[-1].lower()


def main():
    sort1(languages)
    sort2(languages)
    sort3(languages)

if __name__ == '__main__':
    main()
