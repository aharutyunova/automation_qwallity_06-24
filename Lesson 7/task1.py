#1. Write a Python function to find the maximum value of given list(write algorithm).
def Max_from_list(sample_list: list):
   sample_list.sort(reverse=True)
   return sample_list[0]
   
sample_list = [1,6,8,2,65,75,21,6,45]
print(f'Maximum value of given list {sample_list} is: ',Max_from_list(sample_list))
