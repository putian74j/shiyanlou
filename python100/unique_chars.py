class UniqueChars(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        else:
            i = 0
            while i < len(string):
                j = i + 1
                while j < len(string):
                    if(string[i] == string[j]):
                        return False
                    j += 1
                i +=1
        return True