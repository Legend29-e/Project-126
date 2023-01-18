# -*- coding: utf-8 -*-
from tkinter import * 

root = Tk()
root.title("Fibonacci")
root.geometry("400x200")

label_fibonacci_seriesLabel(root, text = "Fibinocci Series")
label_sumLabel(root, text = "sum")
number_of_timesEntry(root)

def Fibonacci():
    num = (number_of_times) 
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    sum2 = 0
    
   " while (counter <= num):
        "label_series["text"] += str(sum) + " "
      '  counter = counter + 1
        'first_no = second_no 
      '  second_no = sum
       ' sum = first_no + second_no        
    "