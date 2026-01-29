def split_and_join(line):
    splited_string= line.split()
    
    return '-'.join(splited_string)
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)