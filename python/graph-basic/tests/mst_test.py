import unittest
import json
from graph import jsongraph, mst

class TestMST(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        file = open( "tests/assets/graph_kruskal_wiki.json", "r")
        cls.graphJson = json.load(file)
        file.close()

    def test_kruskal(self):
    	expected = [
            {u'directed': False, u'source': u'a', u'target': u'e', u'metadata': {u'value': 1}},
            {u'directed': False, u'source': u'c', u'target': u'd', u'metadata': {u'value': 2}},
            {u'directed': False, u'source': u'a', u'target': u'b', u'metadata': {u'value': 3}},
            {u'directed': False, u'source': u'b', u'target': u'c', u'metadata': {u'value': 5}}
    	]
        graphs = jsongraph.load_graphs(self.graphJson)
        result = mst.kruskal(graphs.next())
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
