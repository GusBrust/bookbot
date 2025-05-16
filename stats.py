def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def get_num_words(text):
    numWords = len(text.split())
    return numWords


def get_num_chars(text):
    num_chars = {}
    for char in text.lower():
        if num_chars.get(char):
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars


def dict_to_sorted_list(dict):
    lst = [{"char": key, "num": dict[key]} for key in dict]
    # for k in dict:
    #     list.append(
    #         {"char": k, "num": dict[k]}
    #     )
    lst.sort(key=lambda x: x["num"], reverse=True)
    return lst
