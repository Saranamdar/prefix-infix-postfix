

OPERATORS = set(['+', '-', '*', '/', '(', ')'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2}

class Stack():
    
    def __init__(self):
        self.lst=[]

    def get(self,):
        li_copy = []
        li_copy.extend(self.lst)
        return li_copy
        
    
    def push(self,dataval):
        self.lst.append(dataval)
    
    def peek(self):
        return self.lst[-1]

    def pop(self):
        return self.lst.pop()

    def size(self):
        return(len(self.lst))



def infix_to_postfix(formula):

    stack=Stack()
    stack1=stack.lst


    output = ''

    for ch in formula:
        if ch not in OPERATORS:
            output += ch
        elif ch == '(':
            stack.push('(')
        elif ch == ')':
            while stack1 and stack1[-1] != '(':
                output += stack.pop();
            stack.pop() # pop '('
        else:
            while stack1 and stack1[0] != '(' and PRIORITY[ch] <= PRIORITY[stack1[-1]]:
                output += stack.pop();
            stack.push(ch)

    while stack1: output += stack.pop();

    return output




def infix_to_prefix(formula):
    stack=Stack()
    op_stack=stack.lst

    stack2=Stack()
    exp_stack = stack2.lst

    for ch in formula:
        if not ch in OPERATORS:
            stack2.push(ch)
        elif ch == '(':
            stack.push(ch)
        elif ch == ')':
            while op_stack[-1] != '(':
                op = stack.pop()
                a = stack2.pop()
                b = stack2.pop()
                exp_stack.insert(0, op+b+a )
            stack.pop() # pop '('
        else:
            while op_stack and op_stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[op_stack[-1]]:
                op = stack.pop()
                a = stack2.pop()
                b = stack2.pop()
                exp_stack.insert(0,op+b+a )
            stack.push(ch)

    while op_stack:
        op = op_stack.pop()
        a = stack2.pop()
        b = stack2.pop()
        exp_stack.insert(0,op+b+a )

    return exp_stack[0]





def prefix_to_infix(formula):
    stack = Stack()
    my_stack=stack.lst
    prev_op = None
    for ch in reversed(formula):
        if not ch in OPERATORS:
            stack.push(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            if prev_op and PRIORITY[prev_op] < PRIORITY[ch]:
                exp = '('+a+')'+ch+b
            else:
                exp = a+ch+b
            stack.push(exp)
            prev_op = ch

    return my_stack[0]




def isOperand(x):
	return ((x >= 'a' and x <= 'z') or
			(x >= 'A' and x <= 'Z')) 


def postfix_to_infix(exp) :

	s = []

	for i in exp:	
		
		# Push operands
		if (isOperand(i)) :		
			s.insert(0, i)
			
		# We assume that input is a
		# valid postfix and expect
		# an operator.
		else:
		
			op1 = s[0]
			s.pop(0)
			op2 = s[0]
			s.pop(0)
			s.insert(0, "(" + op2 + i +
							op1 + ")")
			
	# There must be a single element in
	# stack now which is the required
	# infix.
	return s[0]

















