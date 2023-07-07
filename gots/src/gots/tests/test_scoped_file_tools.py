def tool_factory():
    v = 0

    class MyTool:
        @staticmethod
        def print():
            nonlocal v
            v += 1
            print(v)
            return v

    return MyTool


def build_tool():
    MyTool = tool_factory()
    return MyTool()


def test():
    tool1 = build_tool()
    assert tool1.print() == 1
    assert tool1.print() == 2
    assert tool1.print() == 3

    tool2 = build_tool()
    assert tool2.print() == 1
    assert tool2.print() == 2

    assert tool1.print() == 4
    assert tool2.print() == 3
