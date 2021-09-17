def finalQuizScore(h,l,r,q,n,p):
 a=round((90-h*.3-l*.2-r*.15-(q+n)*.1-p*.05)*10)
 r='Sorry, y'if a>100 else'Y'
 return(r+f'ou would need a {a}% on the final quiz to get an A-.')

if __name__=='__main__':
 import doctest
 doctest.run_docstring_examples(finalQuizScore, globals(), name='HW1',verbose=True)