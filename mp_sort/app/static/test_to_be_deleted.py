# import random
# def gen_random_int(number, seed):
# 	result = list(range(number))
# 	random.seed(seed)
# 	random.shuffle(result)
# 	return result
# array = gen_random_int(10,200)
# print(type(array))
# array_str = ', '.join(map(str, array))
# print(type(array_str))

# print("swe"[2])

# name = "Donald Duck"

# print("Hello, ", name, ".")

# print(f"Hello, {name}.")

# print("Hello, {name}.")

# print("Hello, " + name +  ".")

# print(3**1**2) # 3

# def foo(a, b):
#   c = a + b
#   print(c)

# # x=11
# # print(1!=2)
# # print(not 1==2)

# # if x > 5:
# #   print("A")
# # elif x < 10:
# #   print("B")
# # else:
# #   print("C")
# # print("D")

# # print(type(float(4)))
# # print(4)

# # name = "John Wick"
# # for idx in range(len(name)):
# #   print(idx, name[idx])

# # letters = "abcdefg"
# # for char in letters:
# #   print(letters)



# print(7//2)

# def left_of(index):
#       return (index*2)+1
# def right_of(index):
#   return (index+1)*2

# def max_child(array, index, heap_size):
#     if right_of(index) >= heap_size:
#         return left_of(index)
#     else:
#         # Compare the values of left and right child nodes
#         if array[left_of(index)] > array[right_of(index)]:
#             return left_of(index)
#         else:
#             return right_of(index)
        
# def max_heapify(array, index, heap_end_pos):
#     largest = index  # Initialize the largest as the root
#     left_child = 2 * index + 1
#     right_child = 2 * index + 2

#     # Compare the left child with the root
#     if left_child < heap_end_pos and array[left_child] > array[largest]:
#         largest = left_child

#     # Compare the right child with the largest element found so far
#     if right_child < heap_end_pos and array[right_child] > array[largest]:
#         largest = right_child

#     # If the largest element is not the root, swap them and continue to heapify
#     if largest != index:
#         array[index], array[largest] = array[largest], array[index]
#         max_heapify(array, largest, heap_end_pos)

# def build_max_heap(array):
#     heap_end_pos = len(array) - 1
#     for i in range(heap_end_pos // 2, -1, -1):
#         max_heapify(array, i, heap_end_pos)

# def heapsort(array):
#     build_max_heap(array)
#     heap_end_pos = len(array) - 1  # Index of the last element in the heap
#     while heap_end_pos > 0:
#         array[0], array[heap_end_pos] = array[heap_end_pos], array[0]
#         heap_end_pos -= 1
#         #Heapify the remaining heap (from index 0 to heap_end_pos inclusive)
#         max_heapify(array, 0, heap_end_pos)

# # Example usage:
# array = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
# heapsort(array)
# print("Sorted Array:", array)

# array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

# build_max_heap(array)
# print(1999,array)


# def min_child(heap, index, heap_size):
#     left_index = left_of(index)
#     right_index = right_of(index)

#     if left_index >= heap_size:
#         return right_index
#     else:
#         if right_index >= heap_size or heap[left_index] <= heap[right_index]:
#             return left_index
#         else:
#             return right_index
        
# minheap = [1, 2, 4, 3, 9, 7, 8, 10, 14, 16]
# print(min_child(minheap, 4, len(minheap)))


# letters = "abcdefg"
# for idx in range(len(letters)):
#     print(idx, letters[idx])

# letters = "abcd"

# # print(3 > 5 or 3 < 5)
# print(letters[-1:-len(letters)-1:-1])
# print(letters[::-1])
# print(letters[-1:-len(letters):-1])
# print(letters[0:len(letters):-1])

# name = "1. John Wick"
# print(name[3:6])

# value=1
# target=1

# if value >= target:
#   print("A")
# else:
#   print("B")
# print("C")

def move_disks(n, from_tower, to_tower, aux_tower):
    if n == 1:
        return [f"Move disk 1 from {from_tower} to {to_tower}."]
    
    # Step 1: Move the first n - 1 disks from the source to auxiliary tower
    step1 = move_disks(n - 1, from_tower, aux_tower, to_tower)
    
    # Step 2: Move the last disk from source to destination tower
    step2 = [f"Move disk {n} from {from_tower} to {to_tower}."]
    
    # Step 3: Move the first n - 1 disks from auxiliary to destination tower
    step3 = move_disks(n - 1, aux_tower, to_tower, from_tower)
    
    # Combine all steps
    return step1 + step2 + step3

result = move_disks(3, "A", "B", "C")
print(result)

print(["Move disk 1 from A to B.", "Move disk 2 from A to C.", "Move disk 1 from B to C.", "Move disk 3 from A to B.", "Move disk 1 from C to A.", "Move disk 2 from C to B.", "Move disk 1 from A to B."]
)

def min_heapify(array, index, heap_size):
    smallest = index  # 初始化最小值索引为当前索引
    left_child = 2 * index + 1  # 左孩子的索引
    right_child = 2 * index + 2  # 右孩子的索引

    # 如果左孩子存在且比当前节点的值小，更新最小值索引
    if left_child < heap_size and array[left_child] < array[smallest]:
        smallest = left_child

    # 如果右孩子存在且比当前节点的值小，更新最小值索引
    if right_child < heap_size and array[right_child] < array[smallest]:
        smallest = right_child

    # 如果最小值索引不等于当前索引，交换它们的值并递归地对子树执行 min_heapify
    if smallest != index:
        array[index], array[smallest] = array[smallest], array[index]
        min_heapify(array, smallest, heap_size)

# 示例用法：
my_array = [4, 10, 3, 5, 1]
heap_size = len(my_array)

# 在索引 1 处执行 min_heapify，假设数组已经是一个堆，现在破坏了堆属性
min_heapify(my_array, 1, heap_size)

print("Min-heapified array:", my_array)




def permutate(s): #看！
    # Create an empty list to store the permutations
    permutations = []
    
    # Recursive helper function
    def permute_helper(str1, str2):
        if len(str2) == 0:
            # When str2 is empty, a permutation is complete
            permutations.append(str1)
        else:
            for i in range(len(str2)):
                # Move a character from str2 to str1
                new_str1 = str1 + str2[i]
                new_str2 = str2[:i] + str2[i+1:]
                # Recursively invoke with the updated strings
                permute_helper(new_str1, new_str2)
    
    # Start the recursion with empty str1 and the input string s
    permute_helper("", s)
    
    return permutations

input_string = "abc"
result = permutate(input_string)
print(result)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test the gcd function with example inputs
result = gcd(48, 18)
print(result)  # Output should be 6


def min_heapify(array, index, heap_end_pos):
    smallest = index
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    if left_child < heap_end_pos and array[left_child] < array[smallest]:
        smallest = left_child

    if right_child < heap_end_pos and array[right_child] < array[smallest]:
        smallest = right_child

    if smallest != index:
        array[index], array[smallest] = array[smallest], array[index]
        min_heapify(array, smallest, heap_end_pos)
        
def heapsort(array):
    n=len(array)
    i = int(n/2)-1
    #建堆
    while i>=0:
        min_heapify(array,i,n)
        i-=1
    
    #排序
    j=n-1
    while j>0:
        array[j],array[0] = array[0],array[j]
        min_heapify(array,0,j)
        j-=1
    return array[::-1] #为什么min_heapsort还要反转才是最小的？不已经是smallest了吗？

array = gen_random_int(10, 100)
result = heapsort(array)  
print(result)