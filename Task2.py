#Take an array of numbers and return it sorted. 
#If the function passes in an empty array or null/nil value then it should 
#return an empty array. 

#solution using Bubble Sort
#Bubble sort has O(n^2) time complexity, but is very simple

#Ideally use TimSort/QuickSort/Radix Sort for better time complexity.


def main():

    to_sort = [5,3,8,2,7,3,9,2,1]
    
    def manual_sort(to_sort):

        
        #Traverse the array
        for i in range(len(to_sort)):
            #Compare adjacent elements and swap if necessary
            for j in range(len(to_sort) - 1):
                if to_sort[j] > to_sort[j+1]:
                    #Swap
                    to_sort[j], to_sort[j+1] = to_sort[j+1], to_sort[j]


        return to_sort


    print(manual_sort(to_sort))


if __name__ == "__main__":
    main()