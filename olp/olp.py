# olp.py: Useful functions for streamlining one-line python programming
#  primitives["while"](scopevar: dict, cond: str, do: str) -> dict:
#    params: 
#      scopevar: dict: a dict to update the scope of the while loop,
#        This is usually globals(), locals(), or globals() | locals()
#      cond: str: the condition to check at each iteration (passed into eval)
#      do: str: the code to execute at each iteration (passed into exec)
#    returns:
#      dict: the globals() at the end of the while loop execution, to allow
#       access to variables modified within the loop
#  primitives["dowhile"](scopevar: dict, cond: str, do: str) -> dict:
#    A do-while equivalent to the while loop, with the same params and return value
primitives = {"while": lambda scopevar, cond, do: globals().update(scopevar) or globals().update(wl = [1]) or any([wl.append(1) or exec(do) for i in wl if eval(cond) and len(wl) < 1000000]) or globals(), "dowhile": lambda scopevar, cond, do: globals().update(scopevar) or globals().update(wl = [1]) or (exec(do) and False) or any([wl.append(1) or exec(do) for i in wl if eval(cond) and len(wl) < 1000000]) or globals(),}
