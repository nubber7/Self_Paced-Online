#!/usr/bin/env python3
import unittest
import mailroom_OO


class DonorTest(unittest.TestCase):
    def setUp(self):
        self.test = mailroom_OO.Donor('Mr.', 'Brin', 100000)

    def test_donor(self):
        self.assertEqual(self.test.donor, {'Brin': {'title': 'Mr.',
                         'donations': 100000, 'num_donations': 1}})
        self.test.title = 'Dr.'
        self.assertEqual(self.test.donor, {'Brin': {'title':
                         'Dr.', 'donations': 100000, 'num_donations': 1}})
        self.test.donation = 150000
        self.assertEqual(self.test.donor, {'Brin': {'title':
                         'Dr.', 'donations': 250000, 'num_donations': 2}})


class DonorGroupTest(unittest.TestCase):
    def setUp(self):
        self.test = mailroom_OO.DonorGroup(('Mr.', 'Brin', 100000),
                    ('Ms.', 'Wojcicki', 200000), ('Ms.', 'Avey', 150000))

    def test_donor_group(self):
        self.assertEqual(self.test.donor_group, {'Brin': {'title': 'Mr.',
                         'donations': 100000, 'num_donations': 1},
                         'Wojcicki': {'title': 'Ms.', 'donations': 200000,
                         'num_donations': 1}, 'Avey': {'title': 'Ms.',
                         'donations': 150000, 'num_donations': 1}})
