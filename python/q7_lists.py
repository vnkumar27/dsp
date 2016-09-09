# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    count = 0
    for word in words:
        if len(word) >=2 and word[0] == word[len(word)-1]:
                count +=1
    print count


def front_x(words):
    xwords = [word for word in words if word[0]=="x"]
    otherwords = [word for word in words if word[0]!="x"]
    print sorted(xwords)+sorted(otherwords)


def sort_last(tuples):
    print sorted(tuples,key=lambda i: i[-1])


def remove_adjacent(nums):
    if not nums:
        return nums
    newlist = [nums[0]]
    for num in nums[1:]:
        if num != newlist[-1]:
            newlist.append(num)
    print newlist


def linear_merge(list1, list2):
    new_list = sorted(list1+list2)
    print new_list
