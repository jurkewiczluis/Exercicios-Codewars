def find_needle(haystack):
    position = 0
    
    for element in haystack:
        if element == "needle":
            break
            
        position = position + 1
            
    return f"found the needle at position {position}"
        
input_list = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
print(find_needle(input_list))

input_list = ["needle", "junk", "hay", "hay", "moreJunk", "ay", "randomJunk"]
print(find_needle(input_list))

input_list = ["randomJunk", "junk", "hay", "hay", "moreJunk", "ay", "needle"]
print(find_needle(input_list))
