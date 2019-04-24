#리스트의 값을 매개변수로 가지며 모든 항목을 쉼표와 빈칸으로 구분하는 문자열을 리턴
#['apples', 'bananas', 'tofu', 'cats'] => 'apples, bananas, tofu, and cats'

def comma(list):
    resultStr = ''
    for i in range(len(list)):
        if(i == len(list)-1):
            resultStr += 'and ' + list[i]
        else:    
            resultStr += list[i] + ', '
    print(resultStr)

spam = ['apples', 'bananas', 'tofu', 'cats', 'beginners']
comma(spam)