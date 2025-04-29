import unittest
from main import printBalance, deposits

class tests(unittest.TestCase):
    def test_print(self):
        balance = 10
        expected = "Your balance currently is: $10"
        self.assertEqual(printBalance(balance), expected)   #This tests if I am returning the right string to the user
    
    def test_deposit(self):
        balance = 10
        deposit = 10
        Full_Name = "j"
        expected = 20
        
        self.assertEqual(deposits(deposit, balance, Full_Name), 20)   #This tests if I am depositing the right amount.

    if __name__ == '__main__':
        unittest.main()
    

