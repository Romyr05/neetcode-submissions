class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + "#" + s) #len of s to help up decode s
        return "".join(encoded)

        string = "".join(encoded)
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1
            # Extract length
            length = int(s[i:j])
            # Extract string using length
            result.append(s[j+1:j+1+length])
            # Move pointer past this string
            i = j + 1 + length

        return result
