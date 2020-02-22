class Permutations(object):

    def is_permutation(self, str1, str2):
        if (str1 is None) or (str2 is None):
            return False
        elif (str1 == "") or (str2 == ""):
            return False
        else:
            s1 = list(str1)
            s2 = list(str2)
            return (s1.sort() == s2.sort())
