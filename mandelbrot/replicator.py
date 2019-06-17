import sys

def repeat_good(text):
    """"
    Input:
        A string of text
    Output:
        None

    This functions uses list comprehension to replicate each letter.
    The number of replications is decided by it's place in the text string.
    """
    print('-'.join([text[i]*(i+1) for i in range(len(text))]).title())

def repeat_bad(q):
    qq = q;qqq = 1;qqqq = [];
    for qqqqq in q:
        for qqqqqq in range(qqq):
            qqqq.append(qqqqq) 
        qqq = qqq+1
    out_q = ''
    qqq2 = qqqq;qqq2.reverse()
    for a in range(len(q)):
        for b in range(0,a+1):
            a = qqq2.pop(); out_q += a
        out_q +='-' 
    qqq_qqq_qqq = ''
    for c in range(len(out_q)-1):
        qqq_qqq_qqq += out_q[c] 
    print(qqq_qqq_qqq.title())

if(len(sys.argv) == 1):
    print('Please provide a string'); sys.exit()

arg = sys.argv[1]
repeat_good(arg)
repeat_bad(arg)
