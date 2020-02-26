class Rotation(object):

    def is_substring(self, s1, s2):

        pass

    def is_rotation(self, s1, s2):
        if s1 == s2:
            return True
        elif s1 is None or s2 is None:
            return False
        elif s1 == "" or s2 == "":
            return False
        elif len(s1) != len(s2):
            return False
        t1 = list(s1)
        t2 = list(s2)
        i = 0
        while i < len(t1):
            t1.append(t1.pop(0))
            if t1 == t2:
                return True
            i = i + 1
        return False