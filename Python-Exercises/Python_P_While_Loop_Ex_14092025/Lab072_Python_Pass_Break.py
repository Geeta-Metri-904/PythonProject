for i in range(0,10,1): # 0 to 9
    if i == 6 or i==5:
        print(i)
    else:
        pass # pass is a placeholder statement that does nothing
        # It's used when a statement is syntactically required but no action is needed..

# | i | condition | O/P
# | 0 | 0 == 6 - False | Nothing will be printed ( go back )
# | 1 | 1 == 6 - False | Nothing will be printed ( go back )
# | 2 | 2 == 6 - False | Nothing will be printed ( go back )
# | 3 | 3 == 6 - False | Nothing will be printed ( go back )
# | 4 | 4 == 6 - False | Nothing will be printed ( go back )
# | 5 | 5 == 5 - True | 5
# | 6 | 6 == 6 - True | 6
# | 7 | 7 == 6 - False | Nothing will be printed ( go back )
# | 8 | 8 == 6 - False | Nothing will be printed ( go back )
# | 9 | 9 == 6 - False | Nothing will be printed ( go back )
# | 10 | 10 == 6 -> For Loop Finished

# output :
# 5
# 6



