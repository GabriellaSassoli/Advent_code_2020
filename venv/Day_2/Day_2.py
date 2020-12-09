def read_file(filename):
    file = open(filename)
    passwords_rules=[]
    content = file.readlines()
    for passwords_requirements in content:
        passwords_rules.append((passwords_requirements.split("-")[0], passwords_requirements.split("-")[1].split(" ")[0], passwords_requirements.split("-")[1].split(" ")[1].split(":")[0], passwords_requirements.split("-")[1].split(" ")[2].rstrip()))
    return passwords_rules

def find_correct_number_of_passwords(passwords_rules):
    correct_passwords =0
    for min_number,max_number, char,password in passwords_rules:
        count = password.count(char)
        if  int(min_number) <= count <= int(max_number):
            correct_passwords += 1
    return correct_passwords

if __name__ == '__main__':

    passwords_rules = read_file("day_2.txt")
    print(find_correct_number_of_passwords(passwords_rules))
