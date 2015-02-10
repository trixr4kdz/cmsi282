import unittest
from PriorityQueue import PriorityQueue

class TestPriorityQueue (unittest.TestCase):

	def setUp (self):
		print "TestPriorityQueue: setUp_: begin"
		testName = self.id()
		print "setting up for " + testName

	def test_is_empty (self):
		pq = PriorityQueue()
		self.assertEqual (len(pq), 0)

	def test_isInstance (self):
		pq = PriorityQueue()
		self.assertIsInstance (pq, PriorityQueue, "The object is not an instance of class PriorityQueue")

	def test_add_to_empty_pq (self):
		pq = PriorityQueue()
		pq.add(4)
		actual = pq.getitem(0)
		expected = 4
		self.assertEqual (actual, expected)

	def test_add_many_items (self):
		pq = PriorityQueue()
		pq.add(1)
		pq.add(2)
		pq.add(10)
		pq.add(5)
		pq.add(3)
		pq.add(6)
		actual = pq.getitem(len(pq)-1)
		expected = 10
		self.assertEqual (actual, expected)

	def test_peek (self):
		pq = PriorityQueue()
		pq.add(4)
		actual = pq.peek()
		expected = 4
		self.assertEqual (actual, expected)

	def test_remove (self):
		pq = PriorityQueue()
		pq.add(4)
		pq.remove()
		actual = len (pq)
		expected = 0
		self.assertEqual (actual, expected)

	def test_remove_from_empty (self):
		pq = PriorityQueue()
		pq.remove()
		self.assertRaises (ValueError, pq.remove())

	def test_len (self):
		pq = PriorityQueue()
		pq.add(4)
		actual = len (pq)
		expected = 1
		self.assertEqual (actual, expected)

	def test_str (self):
		pq = PriorityQueue()
		pq.add(4)
		actual = str (pq)
		expected = "[" + str(4) + "]"
		self.assertEqual (actual, expected)

	def test_sift_up (self):
		pass

	def test_sift_down (self):
		pass

	def tearDown (self):
		print "TestPriorityQueue: tearDown_: end \n"

suite = unittest.TestLoader().loadTestsFromTestCase(TestPriorityQueue)
unittest.TextTestRunner(verbosity = 2).run(suite)