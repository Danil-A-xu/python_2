translation = {'ЛОЛ' : 'очень смешно',
              'КРИНЖ' : 'что-то странное, стыдное',
              'РОФЛ' : 'шутка',
              'ЩИЩ': 'одобрение или восторг',
              'КРИПОВЫЙ' : 'страшный, пугающий',
              'АГРИТЬСЯ' : 'злиться'}
print('Здраствуй для того чтобы перевести непонятные вам слова введите их ниже надеюсь мы поможем вам их понять.')
for i in range(5):
    words = input('введите непонятное слово (большими буквами!):')
    if words in translation.keys():
        
        print(translation[words])
        
    else:
        print('Извините такова слова нет!')
