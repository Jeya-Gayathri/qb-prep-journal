def main():
    age = 21
    if 0<=age<=4:
        print('Free')
    elif 5<=age<=12:
        print('$100')
    elif 13<=age<=59:
        print('$250')
    elif age>=60:
        print('$120')

main()
