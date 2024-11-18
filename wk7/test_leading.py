import unittest
from leading import leading_substrings

class TestLeadingSubstrings(unittest.TestCase):
    
    def test_regular_string(self):
        """Test if the function works correctly with a regular string."""
        result = leading_substrings('bear')
        expected = ['b', 'be', 'bea', 'bear']
        self.assertEqual(result, expected, "The leading substrings are incorrect.")

    def test_empty_string(self):
        """Test if the function returns an empty list for an empty string."""
        result = leading_substrings('')
        expected = []
        self.assertEqual(result, expected, "The function should return an empty list for an empty string.")
    
    def test_single_character_string(self):
        """Test if the function handles a string with only one character."""
        result = leading_substrings('a')
        expected = ['a']
        self.assertEqual(result, expected, "The function should return ['a'] for a single character string.")
    
    def test_special_characters(self):
        """Test if the function works with strings containing special characters."""
        result = leading_substrings('!@#')
        expected = ['!', '!@', '!@#']
        self.assertEqual(result, expected, "The function should correctly handle special characters.")
    
    def test_numerical_string(self):
        """Test if the function handles numerical string inputs."""
        result = leading_substrings('123')
        expected = ['1', '12', '123']
        self.assertEqual(result, expected, "The function should correctly handle numerical strings.")
    
    def test_non_string_input(self):
        """Test if the function raises an error for non-string input."""
        with self.assertRaises(TypeError):
            leading_substrings(123)  # Pass an integer instead of a string
    
    def test_list_input(self):
        """Test if the function raises an error for a list input."""
        with self.assertRaises(TypeError):
            leading_substrings(['a', 'b', 'c'])  # Pass a list instead of a string


if __name__ == '__main__':
    unittest.main()