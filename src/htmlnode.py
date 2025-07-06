class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if self.props:
            out = ""
            for prop in ('href', 'target'):
                if prop in self.props:
                    out += f' {prop}="{self.props[prop]}"'
            return out
        return ""

    def __repr__(self):
        return f"HTML({self.tag}, {self.value}, {self.children}, {self.props}"


class LeafNode(HTMLNode):

    def __init__(self, tag, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError()
        if not self.tag:
            return self.value
        proptag = ""
        if self.props:
            proptag = self.props_to_html()
        return f"<{self.tag}{proptag}>{self.value}</{self.tag}>"
