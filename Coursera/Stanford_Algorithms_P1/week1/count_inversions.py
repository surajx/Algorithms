def sort_and_count_inversions(elements):
  if len(elements)<=1:
    return (0, elements)
  no_of_elements = len(elements)
  mid_index = no_of_elements//2
  left_half = elements[:mid_index]
  right_half = elements[mid_index:]
  (count_of_inversions_left, sorted_left_half) = sort_and_count_inversions(left_half)
  (count_of_inversions_right, sorted_right_half) = sort_and_count_inversions(right_half)
  (split_count, sorted_elements) = merge(sorted_left_half, sorted_right_half)
  return (count_of_inversions_left + count_of_inversions_right + split_count, sorted_elements)

def merge(list1, list2):
  merged_list = []
  count_inversions = 0
  list1_idx=list2_idx=0
  while True:
    try:
      if list1[list1_idx]<list2[list2_idx]:
        merged_list.append(list1[list1_idx])
        list1_idx+=1
      else:
        merged_list.append(list2[list2_idx])
        list2_idx+=1
        count_inversions+=len(list1[list1_idx:])
    except:
      if len(list1)==len(list2):
        if list1_idx>list2_idx:
          merged_list.extend(list2[list2_idx:])
        else:
          merged_list.extend(list1[list1_idx:])
      elif list1_idx>=len(list1):
        merged_list.extend(list2[list2_idx:])
      else:
        merged_list.extend(list1[list1_idx:])
      break
  return (count_inversions, merged_list)

with open('IntegerArray.txt','r') as file_desc:
  val_list = []
  for value in file_desc:
    val_list.append(int(value))
  print sort_and_count_inversions(val_list)[0]
