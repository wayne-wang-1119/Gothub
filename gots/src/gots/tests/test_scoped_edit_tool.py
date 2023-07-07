from ..tools.scoped_file_tools_funcs import (
    MyCreateToolInput,
    MyLocateToolInput,
    edit_file_tool_factory,
)

read, locate, write = edit_file_tool_factory()


# def test_read():
#     """
#     Test the read function.
#     """
#     file_path = MyCreateToolInput(
#         file_path=
#     )
#     read().run(file_path.file_path)
#     print(read().run(file_path.file_path))
#     locate_inp = MyLocateToolInput(line_number="1:3")
#     assert locate().run(locate_inp.line_number) == "def tool_factory():\n    v = 0\n"
#     print(locate().run(locate_inp.line_number))
