from unittest.mock import patch
from unittest import TestCase
import unittest
from project import create,load,add,task_validation,date_validation,number_validation
import csv
class Test(TestCase):

    def test_create(self):
        self.assertEqual(create("week"),"week.csv")
        self.assertEqual(create("2023 Todo list"),"2023 Todo list.csv")
    
    def test_load(self):
        # To test if the function load works properly it needs a file that already exist, 
        # so we'll use create for this purpose.
        file_name = create("week")
        
        self.assertEqual(load(file_name),"week.csv")

        # Same here.
        file_name = create("july goals")

        self.assertEqual(load(file_name),"july goals.csv")

        with self.assertRaises(SystemExit):
            # Load should raise FileNotFoundError if the file given doesn't exist,
            # and raises a SystemExit as a result.
            load("month.csv")


    def test_add(self):
        # To test this function a real file is needed so let's use the create function.
        file_name = create("fileForAdd")
        
        # If the function adds a new task it should return False, in other case, it will return True.
        # So to test if it works, input a valid task and date.
        self.assertTrue(add(file_name))

        # Now write an invalid task or date, the return value should be equal to False.
        self.assertFalse(add(file_name))


    def test_task_validation(self):
        self.assertTrue(task_validation("week"))
        self.assertTrue(task_validation("month N12"))
        self.assertFalse(task_validation("Week$$$"))


    def test_date_validation(self):
        self.assertTrue(date_validation("12-12-2023"))
        self.assertFalse(date_validation("12/12/2023"))
        self.assertFalse(date_validation("24th of july"))

    def test_number_validation(self):
        # For the sake of keeping things simple, lets use a list instead of a file for the value of df.
        df = ["first_row","second_row","third_row"]
        self.assertTrue(number_validation(df, 2))
        self.assertTrue(number_validation(df, 0))
        self.assertFalse(number_validation(df,-2))
        self.assertFalse(number_validation(df,6))


# For the sake of not making more horrible tests, 
# I will stop at this point. If someone is reading this, please help me to make this tests better, 
# I'm absolutely lost on how to improve them. 

if __name__ == '__main__':
    unittest.main()