import re


with open('./text_file.txt', 'r') as f:
    content = f.read()


def mad_libs(mls):
    matches = re.findall("ADJECTIVE|VERB|NOUN", mls)
    if matches is not None:
        for word in matches:
            q = input(f'Введите {word}: ')
            mls = mls.replace(word, q, 1)
        return mls


new_content = mad_libs(content)

with open('new_text_file.txt', 'w') as f:
    f.write(new_content)



