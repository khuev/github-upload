# Class:       605.203.83 Discrete Mathematics Spring 2021
# Assignment:  Project 03 - Probability for Monthly Dinners
# Author:      Khue Tran
# Date:        2021.04.11
# Description: This program produces the probability that out of a group of six friends that each friend gets to select where to go to dinner at least once in the next twelve months, given the number of trials and series.

############################################################################

import itertools
import sys
import random

##### SET UP VARIABLES AND INPUTS #####

names = ['Khue','Ginny','Sachi','Daniel','Johnathan','Crisrael']
trials_completed = 0
series_completed = 0
successes = 0
failures = 0


########## HANDLE USER INPUT ##########

##### NUMBER OF TRIALS
# user input to take in given number of variables and catch invalid inputs that are not positive integer numbers
print("Khue, Ginny, Sachi, Daniel, Johnathan, and Crisrael are planning to") 
print("have a monthly dinner where one of them chooses the restaurant for") 
print("that month. To make it more interesting, they will be rolling a ")
print("6-sided die every month to determine who gets to pick. What is the") 
print("probability that over the course of the next 12 months, everyone gets") 
print("to pick a restaurant at least once?")
print()
n_trials = input("Enter a positive integer indicating the number of trials per set: ")
n_series = input("Enter the number of sets in series to run of this number of trials: ")

########### ERROR CHECKING ############

try:
   num_user_input = int(n_trials)
   if num_user_input > 0:
      print()
      print("# of trials entered = " + n_trials)
   else:
      print("Cannot run negative number of trials, please try again.")
      sys.exit()
   print()
except ValueError:
   print("Incorrect value type passed. Please input an integer.")

try:
   series_user_input = int(n_series)
   if series_user_input > 0:
      print()
      print("# sets in series entered = " + n_series)
   else:
      print("Cannot run negative number of sets in a series, please try again.")
      sys.exit()
   print()
except ValueError:
   print("Incorrect value type passed. Please input an integer.")



# print to text file, using input number as part of the output file name
original_stdout = sys.stdout

with open('output_trials'+str(num_user_input)+'_series'+str(series_user_input)+'.txt', 'w', encoding='utf-8') as newfile:
   sys.stdout = newfile

   print("====================================")
   print("# of trials entered by user = " + str(num_user_input))
   print("# sets in series entered by user = " + str(series_user_input))

   ########## RUNNING SERIES OF TRIALS ##########
   # nested while loop for running n trials for k series
   while series_completed < series_user_input:
      while trials_completed < num_user_input:
         list_temp_trial = random.choices(names, k=12)
         #print(list_temp_trial)
         #if (all(x in names for x in list_temp_trial)):

         if set(names).issubset(list_temp_trial):
            successes = successes + 1
         #   print('Everyone exists!')
         #else:
            #failures = failures + 1
         #   print('Everyone is a figment of my imagination')

         trials_completed = trials_completed + 1
         #failures = 0

      print()
      print("Results of " + str(trials_completed) + " trials: ") 
      print("Fraction of successful trials: " + str(successes/(num_user_input)))

      successes = 0
      
      series_completed = series_completed + 1
      print("Set #" + str(series_completed) + " in series completed.")
      print()

      # reset variables for trials
      trials_completed = 0

   original_stdout = sys.stdout


   print("====================================")
   print("Program run completed.")
# print(random.choices(names, k=12))


