



dict_ = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 6: 'ШЭЮ', 7: 'ФЩЪ'}

def find_sum(str_: str) -> int:

    #t1 = sum([k for i in str_ for k, v in dict_.items() if i in v])
    sum_ = 0

    for i in str_:
        for k, v in dict_.items():
            if i in v:
                sum_ = sum_ + k


    return sum_

str_ = "БФКЩАТ"
print(find_sum(str_))