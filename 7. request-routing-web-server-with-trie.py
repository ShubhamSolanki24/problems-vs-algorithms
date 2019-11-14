from collections import defaultdict


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, path_part):
        # Insert the node as before
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()

    def __repr__(self):
        return str(self.handler)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        path_parts = path.split('/')
        node = self.root
        for part in path_parts:
            if part != '':
                node.insert(part)
                node = node.children[part]

        node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        path_parts = path.split('/')
        node = self.root

        for part in path_parts:
            if part != '':
                node = node.children[part]

        return node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler):
        # self.not_found_handler = not_found_handler
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.route_trie.insert(path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        return self.route_trie.find(path)

    def split_path(self, ):
        pass
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here


if __name__ == '__main__':
    # Here are some test cases and expected outputs you can use to test your implementation

    # create the router and add a route
    router = Router("root handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home", "home handler")  # add a route
    router.add_handler("/home/about", "about handler")  # add a route
    router.add_handler("/home/about/me/edit", "edit handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'home handler'
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me"))  # should print 'not found handler'
    print(router.lookup("/home/about/me/edit"))  # should print 'edit handler'
