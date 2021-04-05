def foo():
    def bar():
        return "This is from Bar"
    return bar()

print(foo())