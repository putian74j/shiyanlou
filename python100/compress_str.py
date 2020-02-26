class CompressString(object):

    def compress(self, string):

        if string is None or string == "":
            return string
        tem = []
        print(string)
        i = 0
        while i < len(string)-1:
            tem.append(string[i])
            print(tem)
            if string[i] != string[i+1]:
                tem.append(" ")
            i = i + 1
        tem.append(string[-1])
        st = "".join(tem).split()
        s = ""
        for j in st:
            if len(j) > 1:
                s = s + j[0]
                s = s + str(len(j))
            else:
                s = s + j
        if len(s) == len(string):
            return string
        else:
            return s



