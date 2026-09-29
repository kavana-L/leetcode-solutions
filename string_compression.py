class Solution:
    def compress(self, chars: list[str]) -> int:
        read,write=0,0
        while read < len(chars):
            start = read
            while read < len(chars) and chars[read] == chars[start]:
                read +=1
            chars[write] = chars[start]
            write +=1

            if read - start > 1:
                for digit in str(read - start):
                    chars[write] = digit
                    write +=1
        return write

        