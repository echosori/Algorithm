import re


def between_markers(text: str, begin: str, end: str) -> str:
    p_between = re.compile("(?<={}).+(?={})".format(re.escape(begin),re.escape(end)))
    p_lookahead = re.compile(".+(?={})".format(re.escape(end)))
    p_lookbehind = re.compile("(?<={}).+".format(re.escape(begin)))

    a = text.find(begin)
    b = text.find(end)

    if a == -1 and b == -1:
        return text
    elif a!=-1 and b!=-1 and a > b:
        return ''

    elif a == -1 and b != -1: #no opened
        print(p_lookahead.search(text).group())
        return p_lookahead.search(text).group()

    elif a != -1 and b == -1:#no closed
        print(a)
        print(b)
        print(p_lookbehind.search(text).group())
        return p_lookbehind.search(text).group()
    #
    else:
        return p_between.search(text).group()


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"

    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"

    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'

    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'

    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'

    assert between_markers('No <hi>', '>', '<') == '', 'Wrong .,.'
    print('Wow, you are doing pretty good. Time to check it!')
