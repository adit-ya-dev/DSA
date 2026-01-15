"Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example
Input: "A man, a plan, a canal: Panama"
Output: True
"

def isPalindrome(s):
    cleaned = ""

    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()

    return cleaned == cleaned[::-1]
