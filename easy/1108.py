class Solution:
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
        # simply return the string parameter using the str.replace() function
