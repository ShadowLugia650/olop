import os
import random #in practice use sysrandom


class Dummy():
    a = "abcd"
    def __init__(self):
        pass


def add_to_list_dict(d, k, v):
    if k in d:
        d[k].append(v)
    else:
        d[k] = [v]


def n_from(n, nvals, allow_boolops=False):
    RANGE = 15
    m = random.choice([i for i in nvals if i < n])
    #k = random.choice([i for i in nvals if abs(m * i - n) < RANGE])
    try:
        k = random.choice([i for i in nvals for j in nvals for k in nvals if abs(m * i - n) in nvals or abs(m * i - n) == k * j])
    except IndexError:
        return n_from(n, nvals, allow_boolops)
    r = n - m * k
    if r == 0:
        return random.choice(nvals[m]) + " * " + random.choice(nvals[k])
    #return random.choice(nvals[m]) + " * " + random.choice(nvals[k]) + (" + " if r > 0 else " - ") + _rec_n_from(n, nvals, allow_boolops)
    if abs(r) in nvals:
        return random.choice(nvals[m]) + " * " + random.choice(nvals[k]) + (" + " if r > 0 else " - ") + random.choice(nvals[abs(r)])
    j = random.choice([i for i in nvals for j in nvals if abs(r) == i * j])
    print(n, m, k, r, j, abs(r)/j)
    return random.choice(nvals[m]) + " * " + random.choice(nvals[k]) + (" + " if r > 0 else " - ") + random.choice(nvals[int(abs(r) / j)]) + " * " + random.choice(nvals[j])
    #return random.choice(nvals[m]) + " * " + random.choice(nvals[k]) + (" + " if r > 0 else " - ") + str(abs(r))


def _rec_n_from(n, nvals, allow_boolops=False):
    if n in nvals:
        return random.choice(nvals[n])
    RANGE = 15
    m = random.choice([i for i in nvals if i < n])
    k = random.choice([i for i in nvals if abs(m * i - n) < RANGE])
    r = n - m * k
    if r == 0:
        return random.choice(nvals[m]) + " * " + random.choice(nvals[k])
    return random.choice(nvals[m]) + " * " + random.choice(nvals[k]) + (" + " if r > 0 else " - ") + _rec_n_from(n, nvals, allow_boolops)


def generate_obfs_prims_from(pys):
    nvals = {}
    for py in pys:
        mod = __import__(py)
        for i in dir(mod):
            if not i.startswith("__"):
                ## TODO: split by type?
                if callable(mod.__dict__[i]):
                    try:
                        n = len(mod.__dict__[i]())
                        add_to_list_dict(nvals, n, "len({}.{}())".format(py, i))
                    except:
                        pass
                if hasattr(mod.__dict__[i], "__dict__"):
                    n = len(mod.__dict__[i].__dict__)
                    add_to_list_dict(nvals, n, "len({}.{}.__dict__)".format(py, i))
                    for attr, val in mod.__dict__[i].__dict__.items():
                        if type(val) == int:#[int, float]:
                            add_to_list_dict(nvals, val, "{}.{}.{}".format(py, i, attr))
                        elif type(val) == str:
                            # check if there are any numbers in str
                            #else
                            for ci in range(len(val)):
                                add_to_list_dict(nvals, ord(val[ci]), "ord({}.{}.{}[{}])".format(py, i, attr, ci))
    return nvals


def get_bytes_from_files(char, recurse_nums=None):
    #return [globals().update(b = open(f).buffer) or [i for i in b if ord(i) == ord(c)] for d, dirs, files in os.walk(".") for f in files for c in key]
    idx = [None, -1]
    walk = list(os.walk("."))
    random.shuffle(walk)
    for d, dirs, files in walk:
        random.shuffle(files)
        for file in files:
            if not file.endswith(".pyc"):
                with open(file, "r") as f:
                    buf = f.buffer.read()
                    if char.encode() in buf:
                        idx = [file, buf.index(char.encode())]
                        break
        if idx[0] is not None:
            break
    if idx[0] is None:
        return None
    if recurse_nums is not None:
        if idx[1] in recurse_nums:
            idx[1] = random.choice(recurse_nums[idx[1]])
        else:
            idx[1] = n_from(idx[1], recurse_nums)
    return "open(\"{}\").read().encode()[{}]".format(*idx)


def generate_obfs(key, recursive=False):
    pyf = []
    for d, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                pyf.append(file[:-3].replace(os.pathsep, "."))
    nums = generate_obfs_prims_from(pyf)
    cmds = []
    for c in key:
        if ord(c) in range(48, 58):
            byte = get_bytes_from_files(c, nums if recursive else None)
            if byte is None:
                if int(c) in nums:
                    cmds.append("str({})".format(random.choice(nums[int(c)])))
                else:
                    cmds.append("str({})".format(n_from(int(c), nums)))
            else:
                if int(c) in nums and random.random() < 0.25:
                    cmds.append("str({})".format(random.choice(nums[int(c)])))
                else:
                    cmds.append(byte)
        else:
            byte = get_bytes_from_files(c, nums if recursive else None)
            if byte is None:
                if ord(c) in nums:
                    nc = random.choice(nums[ord(c)])
                    if "ord(" in nc:
                        cmds.append(nc.replace("ord(", "")[:-1])
                    else:
                        cmds.append("chr({})".format(nc))
                else:
                    cmds.append("chr({})".format(n_from(ord(c), nums)))
            else:
                if ord(c) in nums and random.random() < 0.25:
                    nc = random.choice(nums[ord(c)])
                    if "ord(" in nc:
                        cmds.append(nc.replace("ord(", "")[:-1])
                    else:
                        cmds.append("chr({})".format(nc))
                else:
                    cmds.append(byte)
    return cmds


def _test_generated(l):
    s = "".join([eval(i.replace("pyobfs.os", "os").replace("pyobfs.random", "random")) for i in l])
