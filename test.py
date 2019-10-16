import unittest
import redis
redis_db = redis.StrictRedis(host="localhost", port=6379, charset="utf-8", decode_responses=True, db=0)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
