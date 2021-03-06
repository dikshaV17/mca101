def areaRectangle(length, breadth):
    '''
    objective : to compute the area of a rectangle
    input parameters:
        length: length of rectangle
        breadth: breadth of rectangle
    approach: multiply length and breadth
    return: area of rectangle
    '''
    area = length*breadth
    return area

def main():
    '''
    objective : to compute the area of a rectangle
    user inputs:
        length: length of rectangle
        breadth: breadth of rectangle
    approach: use function areaRectangle
    '''
    length = int(input('Enter Length of Rectangle: '))
    breadth = int(input('Enter Breadth of Rectangle: '))
    print('Length of Rectangle: ', length)
    print('Breadth of Rectangle: ', breadth)
    print('Area of Rectangle: ', areaRectangle(length, breadth))
    print('End of Output')

if __name__ == '__main__':
    main()
print('End of Program')
