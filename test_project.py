from unittest.mock import patch
from unittest import TestCase
import unittest
from project import create,load,task_validation,date_validation,number_validation
import csv
class Test(TestCase):

    def test_create(self):
        self.assertEqual(create("week"),"week.csv")
        self.assertEqual(create("2023 Todo list"),"2023 Todo list.csv")
    
    def test_load(self):
        # To test if the function load works properly it needs a file that already exist.
        with open("week.csv", "w") as test_list:
            key_writer = csv.writer(test_list)
            key_writer.writerow(["task","date", "state"])

        self.assertEqual(load("week.csv"),"week.csv")

        # Same here.
        with open("july goals.csv", "w") as test_list:
            key_writer = csv.writer(test_list)
            key_writer.writerow(["task","date", "state"])

        self.assertEqual(load("july goals.csv"),"july goals.csv")

        with self.assertRaises(SystemExit):
            # Load should raise FileNotFoundError if the file given doesn't exist,
            # and raises a SystemExit as a result.
            load("month.csv")


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



#delete later, some functions made to understand unit testing#


#def get_input(text):
#    return input(text)

#def get_input(text):
#    return input(text)

#def answer():
#    ans = get_input('enter yes or no')
#    if ans == 'yes':
#        return 'you entered yes'
#    if ans == 'no':
#        return 'you entered no'
    

#class Test(TestCase):

#   @patch('test_project.get_input', return_value='yes')
#    def test_answer_yes(self,input):
#        self.assertEqual(answer(), 'you entered yes')

#    @patch('test_project.get_input', return_value='no')
#    def test_answer_no(self,input):
#        self.assertEqual(answer(), 'you entered no')

if __name__ == '__main__':
    unittest.main()