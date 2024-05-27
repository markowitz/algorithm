from Stack import Stack

def is_paren_balanced(paren_string):
    s = Stack()

    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]

        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    
    if s.is_empty() and is_balanced:
        return True
    else:
        return False
    

def is_match(str1, str2):
    if str1 == "(" and str2 == ")":
        return True
    elif str1 == "{" and str2 == "}":
        return True
    elif str1 == "[" and str2 == "]":
        return True
    else:
        return False
    
print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))

print("String : ))(( Balanced or not?")
print(is_paren_balanced("))(("))

