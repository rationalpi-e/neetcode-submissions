class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(str)}#{str}' for str in strs)

    def decode(self, s: str) -> List[str]:
        mylist = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            word = s[j + 1 : j  + 1 + length]
            mylist.append(word)

            i = j+ 1+ length

        return mylist