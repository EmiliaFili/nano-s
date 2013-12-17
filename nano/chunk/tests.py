from django.test import TestCase

from nano.chunk.models import Chunk

class ChunkTest(TestCase):

    def test_str(self):
        item = Chunk(slug='test', content='Test')
        self.assertEqual(str(item), item.slug)
