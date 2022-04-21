"""Take an array of numbers and return it sorted. 
   If the function passes in an empty array or null/nil 
   value then it should return an empty array."""

def sortArray(array):
    
    sorted_array = []
    
    while array: # while array != None
        min = array[0]  # an arbitrary minimum number 
        for num in array: 
            if num < min:
                min = num
        sorted_array.append(min)
        array.remove(min)    

    return sorted_array

print(sortArray([-5, 4, 0, 80, -7, 80, 25]))
print(sortArray([]))