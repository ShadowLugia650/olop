primitives = {"while": lambda scopevar, cond, do: globals().update(scopevar) or globals().update(wl = [1]) or any([wl.append(1) or exec(do) for i in wl if eval(cond) and len(wl) < 1000000]) or globals(), "dowhile": lambda scopevar, cond, do: globals().update(scopevar) or globals().update(wl = [1]) or (exec(do) and False) or any([wl.append(1) or exec(do) for i in wl if eval(cond) and len(wl) < 1000000]) or globals(),}
