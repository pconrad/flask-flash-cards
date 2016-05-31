# -*- coding: utf-8 -*-

import unittest
from mandarin import *
from flashcard import Flashcard

class TestMandarin(unittest.TestCase):

    def setUp(self):
        self.mandarin_animals = mandarin_animal_flashcards()
        self.mandarin_numbers = mandarin_number_flashcards()
        
    def test_mandarin_animals_is_a_list(self):
        self.assertEqual(type(self.mandarin_animals),list)

    def test_mandarin_numbers_is_a_list(self):
        self.assertEqual(type(self.mandarin_numbers),list)

    def test_all_elements_of_mandarin_animals_list_are_flashcards(self):
        for x in self.mandarin_animals:
            self.assertTrue(isinstance(x,Flashcard))

    def test_all_elements_of_mandarin_numbers_list_are_flashcards(self):
        for x in self.mandarin_numbers:
            self.assertTrue(isinstance(x,Flashcard))

        
if __name__=="__main__":
    unittest.main()
