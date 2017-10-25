#!/usr/bin/env python3

def quickSort(num_list):
   q_help(num_list,0,len(num_list)-1)

def q_help(num_list,first,last):
   if first<last:

       splitpoint = partition(num_list,first,last)

       q_help(num_list,first,splitpoint - 1)
       q_help(num_list,splitpoint + 1,last)


def partition(num_list,first,last):
   piv = num_list[first]

   left = first + 1
   right = last

   done = False
   while not done:

       while left <= right and num_list[left] <= piv:
           left = left + 1

       while num_list[right] >= piv and right >= left:
           right = right -1

       if right < left:
           done = True
       else:
           num_list[left], num_list[right] = num_list[right], num_list[left]

   num_list[first], num_list[right] = num_list[right], num_list[first]

   return right

   # def quickSort(num_list):
   #         arr_len = len(num_list)
   #         if( arr_len <= 1):
   #             return num_list
   #
   #         else:
   #             piv = num_list[0]
   #
   #             g = []
   #             for element in num_list[1:]:
   #                 if element > piv:
   #                     g.append(element)
   #             l = []
   #             for element in num_list[1:]:
   #                 if element <= piv:
   #                     l.append(element)
   #
   #             return quickSort(l) + [piv] + quickSort(g)
