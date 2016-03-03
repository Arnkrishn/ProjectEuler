import math

num_word_map = {0 : '',
                1 : 'one',
                2 : 'two',
                3 : 'three',
                4 : 'four',
                5 : 'five',
                6 : 'six',
                7 : 'seven',
                8 : 'eight',
                9 : 'nine',
                10 : 'ten',
                11 : 'eleven',
                12 : 'twelve',
                13 : 'thirteen',
                14 : 'fourteen',
                15 : 'fifteen',
                16 : 'sixteen',
                17 : 'seventeen',
                18 : 'eighteen',
                19 : 'nineteen',
                20 : 'twenty',
                30 : 'thirty',
                40 : 'forty',
                50 : 'fifty',
                60 : 'sixty',
                70 : 'seventy',
                80 : 'eighty',
                90 : 'ninety',
                100 : 'hundred',
                1000 : 'thousand'}

def letter_count(word):
    if word is None or word == '':
        return 0
    else:
        return len(word.replace(' ', ''))

def num_letter_count(num):
    if num <= 0:
        print "Please provide positive non-zero input"
    else:
        num_word = ''
        connector = ''
        if num < 100 and num in num_word_map.keys():   # For number already in num word map
            num_word = num_word_map[num]
        else:
            str_num = str(num)
            len_str_num = len(str_num)
            if len_str_num > 2:
                connector = 'and '
            for i in range(len_str_num):
                # For numbers with more than 2 digits
                if len_str_num - i > 2 and str_num[i] != '0':
                    num_word = num_word + num_word_map[int(str_num[i])] + ' ' + num_word_map[int(math.pow(10, len_str_num - i - 1))] + ' '
                else:
                    # Cases to handle the first 2 digits in a number
                    if int(str_num[-2:]) != 0:
                        if int(str_num[-2:]) in num_word_map.keys():
                            num_word = num_word + connector + num_word_map[int(str_num[-2:])]
                        else:
                            num_word = num_word + connector + num_word_map[int(str_num[len(str_num) - 2]) * 10] + ' ' + num_word_map[int(str_num[len(str_num) - 1])]
                        break

        return letter_count(num_word)

#Test
print num_letter_count(6000)
num = 1000

sum = 0
for i in range(1, num + 1):
    sum += num_letter_count(i)

print sum
