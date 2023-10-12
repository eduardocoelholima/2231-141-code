def binary_search( data, target, start, end ):
    # base condition - terminate when start index passes end index
    if start > end:
        return None
    
    # find the middle value between start and end indices
    mid_index = ( start + end ) // 2
    mid_value = data[mid_index]
    
    # recursive calls based on which half the target might be in
    if target == mid_value:
        return mid_index
    elif target < mid_value:
        return binary_search( data, target, start, mid_index-1 )
    else:
        return binary_search( data, target, mid_index+1, end )
        

def main():
    start = 1
    stop = 30
    step = 2

    # start = 30
    # stop = 1
    # step = -2

    data = []
    for loop in range ( start, stop, step ):
            data += [loop]
    print( "\nData: ", data )
    print( "Number of elements: ", len( data ) )
    
    target = 6
    index = binary_search( data, target, 0, len(data) )
    if index != None:
        print( target, "found at index", index )
    else:
        print( target, "not found" )


if __name__ == "__main__":
    main()
