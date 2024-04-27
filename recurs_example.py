def CalcSumNumbers(A):
    if A == []:
        # если набор пуст, возвратить 0
        return 0
    else:
        # Вычислить сумму - прибавить первый элемент набора
        summ = CalcSumNumbers(A[1:]) # рекурсивный вызов этой же функции

        # Прибавить к общей сумме первый элемент
        summ = summ + A[0]

        return summ

def main():
    reslt = CalcSumNumbers([ 2, 3, 8, 11, 4, 6 ])
    print(reslt +)


if __name__ == '__main__':
    main()