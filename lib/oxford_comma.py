def oxford_comma(items):
    if len(items) == 1:
        return ''.join(items)
    
    if len(items) == 2:
        return ' and '.join(items)
    
    if len(items) > 2:
        i=0
        string = ""
        while i < (len(items)-1):
            string += items[i] + ", "
            i += 1
        string += "and " + items[i]
        return string