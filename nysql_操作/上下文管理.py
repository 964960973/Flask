class Foo(object):
    def __enter__(self):
        return 123

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



obj = Foo()
with obj as f:
    print(f)