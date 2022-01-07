# oldec.py: A decoder for one-line python with three primary functions:
#  parse(string: str) -> [str]: parse a one-line python string, returning a list
#    of strings wit each line of the decoded pythonas an individual item in the
#    list.
#  parse_recursive(string: str) -> [str]: parse a one-line python string, similar
#    to the parse function, but recursively.
#  beautify(c: [str]) -> [str]: clean up a list of parse results, making them
#    easier to read for non-one-line python programmers.
# Also, these usage comments break my "one-line" rule, I hope you're happy.
globals().update(olp = __import__("olp")) or globals().update(beautify = lambda c: [chunk[:chunk.index(chunk.strip())]+tradimport(chunk.strip()[17:-1]) if chunk.strip().startswith("globals().update(") and chunk.strip().endswith(")") else (cleanchunk(chunk) if chunk.strip().startswith("(") else chunk) for chunk in c]) or globals().update(tradimport = lambda l: (["import "+name if any([name+s+"="+s+"__import__("+q+name+q+")" == l for q in ["\"", "'"] for s in ["", " "]]) else l for name in [l.split("=")[0].strip()]][0]) if "=" in l else l) or globals().update(cleanchunk = lambda chunk: olp.primitives["while"](locals(), "chunk.strip().startswith('(') and chunk.strip().endswith(')')", "globals().update(chunk = chunk[:chunk.index(chunk.strip())] + chunk.strip()[1:-1])")["chunk"]) or globals().update(parse = lambda string: globals().update(temp = []) or globals().update(join = lambda c: globals().update(tmp = [c[i] if c[i].count('(') == c[i].count(')') else (c[i] + " or " + c[i+1] if c[i].count('(') > c[i].count(')') and i+1 < len(c) else c[i]) for i in range(len(c))]) or [tmp[i] for i in range(len(tmp)) if tmp[i] is not None and (i == 0 or tmp[i] not in tmp[i-1])]) or globals().update(parseif = lambda c: globals().update(tmp = []) or [tmp.append(i[:i.index(i.strip())]+i[i.rindex("if"):-11].strip()+":") or tmp.append("    "+i[:i.index(i.strip())]+i[:i.rindex("if")].strip()) if i.endswith("else False") else tmp.append(i) for i in c][0] or tmp) or globals().update(parsequit = lambda c: globals().update(tmp = []) or [tmp.append(i[:-7]) or tmp.append(i[:i.index(i.strip())] + "quit() # may be return if in a function") if i.endswith("or True") else tmp.append(i) for i in c][0] or tmp) or globals().update(parsefor = lambda c: globals().update(tmp = []) or globals().update(nextindent = 0) or [tmp.append(i[:i.index(i.strip())] + i.strip()[i.strip().index("for"):(-4 if i.strip()[-2].isdigit() else -1)].strip()+":") or tmp.append(i[:i.index(i.strip())] + "    " + i.strip()[1:i.strip().index("for")]) if i.strip()[0].startswith('[') else ([tmp.append(i[:i.index(i.strip())] + "    " * idx + "for " + f.strip() + ":") for idx, f in enumerate(i[:-1].split("for")[1:])][0] if i.strip().startswith("for") and i.count("for") > 1 else (tmp.append("    " * nextindent + i))) for i in c][0] or tmp) or globals().update(parseifelse = lambda c: globals().update(tmp = []) or [tmp.append(i) for i in c][0] or tmp) or globals().update(chunks = string.split(" or ")) or globals().update(chunks = olp.primitives["dowhile"](globals(), "chunks != temp", "globals().update(temp = chunks) or globals().update(chunks = join(chunks))")["chunks"] ) or globals().update(chunks = [cleanchunk(chunk) for chunk in chunks]) or globals().update(chunks = parseif(chunks)) or globals().update(chunks = [cleanchunk(chunk) for chunk in chunks]) or globals().update(chunks = parsequit(chunks)) or globals().update(chunks = [cleanchunk(chunk) for chunk in chunks]) or globals().update(chunks = parsefor(chunks)) or globals().update(chunks = [cleanchunk(chunk) for chunk in chunks]) or globals().update(chunks = parseifelse(chunks)) or chunks) or globals().update(parse_recursive = lambda string: globals().update(lines = parse(string)) or olp.primitives["dowhile"](globals(), "temp != lines", "globals().update(temp = lines) or globals().update(lines = sum([([line[:line.index(line.strip())]+i for i in parse(line.strip())] if not line.strip().startswith(\"if\") else [line]) for line in lines], []))")["lines"]) or True