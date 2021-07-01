
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    person = None
    penguin_word_count = 0
    taylor_word_count = 0
    penguin_sticker_count = 0
    taylor_sticker_count = 0
    penguin_image_count = 0
    taylor_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == '廖宏偉':
            if s[2] == '貼圖':
                penguin_sticker_count += 1
            elif s[2] == '圖片':
                penguin_image_count += 1
            else:
                for m in s[2:]:
                    penguin_word_count += len(m)
        elif name == '拆彈魯邦邦':
            if s[2] == '貼圖':
                taylor_sticker_count += 1
            elif s[2] == '圖片':
                taylor_image_count += 1
            else:
                for m in s[2:]:
                    taylor_word_count += len(m)
    print('宏偉說了', penguin_word_count, '傳了', penguin_sticker_count, '個貼圖', '傳了', penguin_image_count, '個圖片')  
    print('魯邦邦說了', taylor_word_count, '傳了', taylor_sticker_count, '個貼圖', '傳了', taylor_image_count, '個圖片')    
        # print(s)

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('[LINE]宏偉.txt')
    lines = convert(lines)
    # write_file('output.txt', lines)

main()