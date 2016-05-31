# -*- coding: utf-8 -*-

import unittest
from flashcard import Flashcard


class TestFlashCard(unittest.TestCase):

    def setUp(self):
        self.fc1 = Flashcard(u"dog",u"狗 gǒu");             
        self.fc2 = Flashcard(u"cat",u"猫 māo");    

    def test_fc1_front(self):
        self.assertEqual(u"dog",self.fc1.front);

    def test_fc1_back(self):
        self.assertEqual(u"狗 gǒu",self.fc1.back);
    
    def test_fc2_front(self):
        self.assertEqual(u"cat",self.fc2.front);

    def test_fc2_back(self):
        self.assertEqual(u"猫 māo",self.fc2.back);

        
if __name__=="__main__":
    unittest.main()
