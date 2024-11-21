class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0  # Pointer to write the compressed characters
        read = 0   # Pointer to read the input characters

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count the number of occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character to the write pointer
            chars[write] = char
            write += 1

            # If the character occurs more than once, write the count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

