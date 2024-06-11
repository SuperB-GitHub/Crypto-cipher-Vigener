import time


# Функция составления словаря на английском
def form_dict():
    d = {}
    iter = 0
    for i in range(97,123):
        d[iter] = chr(i)
        iter = iter +1
    return d
 
# Функция изменения букв в цифры
def encode_val(word):
    list_code = []
    lent = len(word)
   
    d = form_dict()
    
    for w in range(lent):
        for value in d:
            if word[w] == d[value]:
               list_code.append(value) 
    return list_code
 
# Функция составления 2 списков
def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0
    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0 
 
    return dic  
 
# Функция составления закодированого текста
def full_encode(value, key):
 
    dic = comparator(value, key)
    print('Пары для кодирования',dic)
  
    lis = []
    d = form_dict()
 
    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go) 
    return lis
 
#------------------------------------------------------------------
# Декодер
#------------------------------------------------------------------
 
# Функция декодирования в списки
def full_decode(value, key):
 
    dic = comparator(value, key)
    
    print('Пары для раскодирования =', dic)
    d = form_dict() # получаем словарь кода
 
    lis =[]
    for v in dic:
        go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
        lis.append(go) 
    return lis
    
#Функция соспоставления из списка из цифры в букву
def decode_val(list_in):
 
    list_code = []
    lent = len(list_in)
 
    d = form_dict() # получаем словарь кода
    
    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value]) 
    return list_code

#Функция для нахождения индекса совпадения
def get_index(mes):
    print(mes)
    mas = list(mes)
    le = len(mas)
    j = 2

    for i in range(2, 11):
        count_i = []
        for j in range(-1, le, j):
            count = mas.count(mas[j]) - 1
            count_i.append(count)
        j = i + 1
        index = 0
        for k in range(1, len(count_i)):
            index += (k * (k - 1)) / (le * (le - 1))        
        print(i, index)


if __name__ == "__main__":
 
    print ('Словарь шифра:',form_dict())
    word = input('Введите слово: ')
    word = word.lower()
    key = input('Введите ключ: ')
    key = key.lower()
    
    key_encoded = encode_val(key)
    value_encoded = encode_val(word)
 
    print ('Слово в цифрах =',value_encoded)
    print ('Ключ в цифрах =', key_encoded)
    print('----------------------------------------------------------')
    shifre = full_encode(value_encoded, key_encoded)
    print ('Зашифрованное слово =', ''.join(decode_val(shifre)))
    print('----------------------------------------------------------')
    decoded = full_decode(shifre, key_encoded)
    print ('Расшифрованная последовательность =', decoded)
    decode_word_list = decode_val(decoded)
    fin_word = ''.join(decode_word_list)
    print ('Слово =',''.join(decode_word_list))

    print('----------------------------------------------------------')
    otvet = input('Начать ли процесс брутфорса? Yes or No -> ')
    start=time.time()
    if otvet.lower() == 'yes':
        bruteforce = open('words.txt')
        dict_bru=bruteforce.readlines()
        dlina = len(dict_bru)
        new_word = ''
        for count in range(dlina):
            yon = dict_bru[count]
            fal_key = encode_val(yon)
            print('Фальшивый ключ = ', yon, fal_key)
            podbor = full_decode(shifre, fal_key)
            print('Раскодированные цифры', podbor)
            new_word = ''.join(decode_val(podbor))
            print('Раскодированное слово', new_word)
            print('----------------------------------------------------------')
            if new_word == fin_word:
                print('Найденый ключ:', yon)
                end=time.time()
                ttime = end-start
                print('Затраченное время: ', ttime)
                break
            elif count+1==dlina:
                print('Ключ не найден, надо поменять словарь')
            
    
    otvet1 = input('Начать ли процесс частотного анализа? Yes или No -> ')
    start1=time.time()
    if otvet1.lower() == 'yes':
        d = form_dict()
        dlina1 = len(d) #26
        zash_word = ''.join(decode_val(shifre)) #Зашифрованное слово в буквах
        
        print(get_index(zash_word))
        
        end1=time.time()
        ttime1=end1-start1
        print('Затраченное время: ',ttime1)
