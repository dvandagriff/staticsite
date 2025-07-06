import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):

    def test_init_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_empty_props_to_html(self):
        node = HTMLNode()
        node.props = {}
        test = node.props_to_html()
        self.assertTrue(len(test) == 0)

    def test_nonempty_props_to_html(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
        })
        test = node.props_to_html()
        self.assertTrue(len(test) > 0)
        self.assertTrue(test.startswith(' '))
        self.assertEqual(test, ' href="https://www.google.com" target="_blank"')
        node.props={"href": "https://www.google.com"}
        test = node.props_to_html()
        self.assertEqual(test, ' href="https://www.google.com"')


class TestLeafNode(unittest.TestCase):

    def test_init_none(self):
        node = LeafNode(tag=None)
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.props)
        self.assertIsNone(node.children)

    def test_props_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_w_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == '__main__':
    unittest.main()
