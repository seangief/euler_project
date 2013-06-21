def main():
    f = open('C:\\Documents and Settings\\Sean Young\\My Documents\\Euler 11.txt','r')
    data = str(f.read())
    data = data.split('\n ')
    matrix = []
    for line in data:
            matrix.append(line.split())
    for h in range(len(matrix)):
            for k in range(len(matrix[h])):
                    matrix[h][k] = int(matrix[h][k])
    multiples = []
    multiples.extend(downcrawl(matrix))
    multiples.extend(sidecrawl(matrix))
    multiples.extend(leftcrawl(matrix))
    multiples.extend(rightcrawl(matrix))
    return max(multiples)

def downcrawl(matrix):
   list = []
   for h in range (len(matrix)):
      for k in range(len(matrix[h])-3):
         product = matrix[h][k]*matrix[h][k+1]*matrix[h][k+2]*matrix[h][k+3]
         list.append(product)
   return list

def sidecrawl(matrix):
    list = []
    for h in range(len(matrix)-3):
        for k in range(len(matrix[h])):
            product = matrix[h][k]*matrix[h+1][k]*matrix[h+2][k]*matrix[h+3][k]
            list.append(product)
    return list

def leftcrawl(matrix):
    list = []
    for h in range(len(matrix)-3):
        for k in range(len(matrix[h])-3):
            product = matrix[h][k]*matrix[h+1][k+1]*matrix[h+2][k+2]*matrix[h+3][k+3]
            list.append(product)
    return list

def rightcrawl(matrix):
    list = []
    for h in range(len(matrix)-3):
        for k in range(len(matrix[h])-3):
            product = matrix[h+3][k]*matrix[h+2][k+1]*matrix[h+1][k+2]*matrix[h][k+3]
            list.append(product)
    return list

    
