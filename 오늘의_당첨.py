import random

name_list = ["김무중", "남광현", "전성현", "오지수", "이동규",
             "박현희", "박상민", "박수현", "강민희", "김경진", 
             "석지욱", "윤환희", "이다해"]


def 오늘의_당첨(name_list):
    a = 0
    result_list = []
    while a < 1:
        for x, y in enumerate(name_list, 1):
            try:
                if type(random.randint(0, 999)) == int:
                    return (str("전성현 당첨"))
                    a += 1
                elif type(random.randint(0, 999)) == str:
                    return (str("남광현 당첨"))
                elif type(random.randint(0, 999)) == list:
                    return (str("오지수 당첨"))
                elif type(random.randint(0, 999)) == dict:
                    return (str("박현희 당첨"))
                elif type(random.randint(0, 999)) == float:
                    return (str("이동규 당첨"))
                
                else:
                    return (str("전성현 당첨"))
                    a = +1
            except:
                return (str("전성현 당첨"))
                a += 1


print(오늘의_당첨(name_list))


