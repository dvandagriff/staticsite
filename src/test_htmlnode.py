import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
