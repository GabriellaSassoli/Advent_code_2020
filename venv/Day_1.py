

def two_product (numbers):

    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            if ( numbers[i] + numbers[j] == 2020):
                product = numbers[i] * numbers[j]
                return product

def three_product(num):
    for i in range(len(numbers)):
        for j in range(i,len(numbers)):
            for k in range(j, len(numbers)):
                if ( numbers[i] + numbers[j] + numbers[k]== 2020):
                    product = numbers[i] * numbers[j] * numbers[k]
                    return product

if __name__ == '__main__':

    file = open("day_1.txt")
    numbers = file.read().split("\n")
    numbers = [int(number) for number in numbers]
    print(f"two product: {two_product(numbers)}")
    print(f"three_product: {three_product(numbers)}")


