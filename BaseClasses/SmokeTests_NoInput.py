class Outer:
    """Outer Class"""

    def __init__(self, v1, v2):
        ## instantiating the 'Inner' class
        self.inner = self.Inner()
        ## instantiating the multilevel 'InnerInner' class
        self.v1 = v1
        self.v2 = v2
        self.v3 = v1 + v2

    class Inner:
        """First Inner Class"""

        def __init__(self):
            self.v4 = outer.v1 * outer.v2


### Accessing the Inners using variables

outer = Outer(5, 2)

# Trying this:
outer_v3 = outer.v3
print(outer_v3)

inner_v4 = outer.inner.v3
print(inner_v4)
