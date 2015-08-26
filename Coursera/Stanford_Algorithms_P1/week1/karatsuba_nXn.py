def karatsuba_multiplier(input1, input2):
  input1_digits_cnt = len(str(input1))
  input2_digits_cnt = len(str(input2))
  if input1_digits_cnt==1 or input2_digits_cnt==1:
    return input1*input2
  a=b=c=d=0
  # split input into two parts: a,b
  a = int(str(input1)[:input1_digits_cnt//2])
  b = int(str(input1)[input1_digits_cnt//2:])
  # split input into two parts: c,d
  c = int(str(input2)[:input2_digits_cnt//2])
  d = int(str(input2)[input2_digits_cnt//2:])
  # calculate a*c, b*d, & (a+b)(c+d) by recursion.
  ac = karatsuba_multiplier(a,c)
  bd = karatsuba_multiplier(b,d)
  ab_cd = karatsuba_multiplier(a+b,c+d) #(a+b)(c+d)
  partial_sum_1 = ac*(10**input1_digits_cnt)
  partial_sum_3 = bd
  partial_sum_2 = (ab_cd - ac - bd)*(10**(input1_digits_cnt/2))
  return partial_sum_1 + partial_sum_2 + partial_sum_3

print karatsuba_multiplier(1234, 5678)
