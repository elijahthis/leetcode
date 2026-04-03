# Given a list of song lists (one for each person), and also a list of query songs. 
# Return a list of recommended songs, where each rec must come from a playlist that contains all the query songs
# The idea was to find the people with the all query songs
# So brute force was going thru each person's playlist and use all() to check whether all query songs r in that playlist, if yes extract the other songs
# Then optimised was 
# 1. Build a songToPerson hashmap
# 2. Use set.intersect() to find common ppl
# 3. Then only go thru those common ppl to add their songs

def songRec(songLists, querySongs):
    