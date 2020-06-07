def camel_to_snake(name):
        for i in enumerate(name):
            if i[1].isupper():
                name = name.replace(i[1], f'_{i[1].lower()}')
        if name[0] == '_':
            return name.lower()[1:len(name)]
        return name.lower()
# print(camel_to_snake("MtnactBxlnlfKsayaeM"))



def snake_to_camel(name):
    for i in enumerate(name):
            if i[1] == '_':
                name = name.replace(i[1], ' ')
                name = name.title()
            else:
                name = name.title()
    return name.replace(' ', '')
# print(snake_to_camel("bo"))