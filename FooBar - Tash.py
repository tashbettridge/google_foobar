#!/usr/bin/env python
# coding: utf-8

# In[1]:


def solution(x,y):  
  n = [x,y]  
  a = [y for x in n for y in x]  
  u = list(set(a))  
  e = [x for x in u if a.count(x) % 2 == 0]  
  z = [x for x in u if x not in e]  
  return z[0]


# In[2]:


def solution(total_lambs):
  a = 1
  b = 1
  total = 1
  c = 0
  while total + b <= total_lambs:
      total += a
      c += 1
      a *= 2
      b = int(a/2) + int(a/3)
  f1 = 1
  f2 = 1
  total = 0
  count = 0
  while total + f1 <= total_lambs:
      total += f1
      f1, f2 = f2, f1 + f2
      count += 1
  return  count - c


# In[3]:


def solution(s):
    x = 0
    for i, c in enumerate(s):
        if(c=='>') :
            y = i+1;
            x += s.count('<', y)
        total = x * 2
        return total


# In[4]:


def solution(s):

    if(len(s) > 100 or len(s) < 1):
        raise Value("Height is outside of bounds")
    
    s = list(s.replace("-",""))
    l = []
    r = []
    x=0

    for i in range(0,len(s)):
        if s[i] == '<':
            l.append(i)
        if s[i] == '>':
            r.append(i)

    for i in r:
        for y in l:
            if i < y:
                x+=1
    for i in l:
        for y in r:
            if y < i:
                x+=1
                
    return x 


# In[5]:


#Challenge 3
def solution(M, F):
    m, f = long(M), long(F)
    total = 0
    while not (m == 1 and f == 1):
        if f <= 0 or m <= 0:
            return "impossible"
        if f == 1:
            return str(total + m - 1)
        else:
            total += long(m/f)
            m, f = f, m % f
    return str(total)


# In[6]:


def solution(n):
    x = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    return staircase(1, n, x) - 1

def staircase(g, l, x):
    if x[g][l] != 0:
        return x[h][l]
    if l == 0:
        return 1
    if l < g:
        return 0
    x[g][l] = staircase(g + 1, l - g, x) + staircase(g + 1, l, x)
    return x[g][l]


# In[7]:


#Challenge 3

def solution(l):
    count = 0
    x = [0] * len(l)
    for i in xrange(len(l) - 1):
        for j in xrange(i + 1, len(l)):
            if l[j] % l[i] == 0:
                x[j] += 1
                count += x[i]

    return count

