class Solution:
    def encode(self, strs):
        encoded = ''
        for s in strs:
            if s != ':':
                encoded += s + ':;'
            else:
                encoded += ':' + s + ':;'
        return encoded


    def decode(self, str):
        # write your code here
        result = []
        buf = ''
        skip = False

        for s in range(len(str)):
            if skip:
                skip = False
                continue

            if str[s] != ':':
                buf += str[s]
            elif str[s] == ':' and str[s+1] == ';':
                result.append(buf)
                buf = ''
                skip = True
            elif str[s] == ':' and str[s+1] == ':':
                buf += ':'
                skip = True
        return result