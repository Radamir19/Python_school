def push(st, x):
    st.append(x)

def pop(st):
    if not isEmpty(st):
        return st.pop()
    else:
        print("stack is empty")
        return ''

def isEmpty(st):
    if len(st) == 0:
        return True
    else:
        return False

def top(st):
    if not isEmpty(st):
        return st[-1]
    else:
        return None

def size(st):
    return len(st)

def stack():
    return []