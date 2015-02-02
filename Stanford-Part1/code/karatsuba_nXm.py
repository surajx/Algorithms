def karatsuba_multiplier
  input1_digits_cnt = len(str(input1))
  input2_digits_cnt = len(str(input2))
  if input1_digits_cnt==1 and input2_digits_cnt==1:
    return input1*input2
  #partial_sum_1=partial_sum_2=partial_sum_3=0 #ac,bd,(a+b)(c+d)
  if input1_digits_cnt!=1:
    # split input into two parts: a,b
    str(input1)[]
  else:
    # keep one part as zero
  if input2_digits_cnt!=1:
    # split input into two parts: c,d
  else:
    # keep one part as zero
  # calculate a*c, b*d, & (a+b)(c+d) by recursion.
  # pad zeroes and return the sum

