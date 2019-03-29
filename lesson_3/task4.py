# Определить, какое число в массиве встречается чаще всего.
def maxIn(x):
    y = dict()
    if (type(x) == list):
        a = set(x)
        for i in a:
            z = 1
            for j in x:
                if i == j:
                    y[i] = z
                    z += 1
        return y
    return {}

x = [1,3,5646,34,233,1,3]
print(maxIn(x))