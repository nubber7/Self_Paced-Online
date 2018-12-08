import html_render as hr
from io import StringIO


# STEP 1 TESTS
# Element class
def test_element_init_no_content():
    page = hr.Element()
    assert page.content == []

def test_element_init_w_empty_content():
    page = hr.Element("")
    assert page.content == []

def test_element_init_w_content():
    page = hr.Element("hello")
    assert page.content == ["hello"]

def test_element_append_to_empty_no_content():
    page = hr.Element()
    page.append("")
    assert page.content == []

def test_element_append_to_empty_w_content():
    page = hr.Element()
    page.append("one")
    assert page.content == ["one"]

def test_element_append_twice_to_empty_w_content():
    page = hr.Element()
    page.append("one")
    page.append("two")
    assert page.content == ["one", "two"]

def test_element_append_to_nonempty_no_content():
    page = hr.Element("one")
    page.append("")
    assert page.content == ["one"]

def test_element_append_to_nonempty_w_content():
    page = hr.Element("one")
    page.append("two")
    assert page.content == ["one", "two"]

def test_element_append_twice_to_nonempty_w_content():
    page = hr.Element("one")
    page.append("two")
    page.append("three")
    assert page.content == ["one", "two", "three"]

def test_element_render_no_content():
    page = hr.Element()
    f = StringIO()
    page.render(f)
    expected = "<html>\n</html>\n"
    assert f.getvalue() == expected

def test_element_render_w_one_line():
    page = hr.Element("one")
    f = StringIO()
    page.render(f)
    expected = "<html>\n   one\n</html>\n"
    assert f.getvalue() == expected

def test_element_render_w_two_lines():
    page = hr.Element("one")
    page.append("two")
    f = StringIO()
    page.render(f)
    expected = "<html>\n   one\n   two\n</html>\n"
    assert f.getvalue() == expected

def test_element_render_w_indent_no_content():
    page = hr.Element()
    f = StringIO()
    page.render(f, "   ")
    expected = "   <html>\n   </html>\n"
    assert f.getvalue() == expected

def test_element_render_w_indent_w_one_line():
    page = hr.Element("one")
    f = StringIO()
    page.render(f, "   ")
    expected = "   <html>\n      one\n   </html>\n"
    assert f.getvalue() == expected

def test_element_render_w_indent_w_two_lines():
    page = hr.Element("one")
    page.append("two")
    f = StringIO()
    page.render(f, "   ")
    expected = "   <html>\n      one\n      two\n   </html>\n"
    assert f.getvalue() == expected

def test_step_1_html_output():
    page = hr.Element()
    page.append("Here is a paragraph of text -- there could be more of them, "
                "but this is enough  to show that we can do some text")
    page.append("And here is another piece of text -- you should be able to add any number")
    f = StringIO()
    page.render(f)
    expected = "<html>\n" \
               "   Here is a paragraph of text -- there could be more of them, but this is enough " \
               " to show that we can do some text\n" \
               "   And here is another piece of text -- you should be able to add any number\n" \
               "</html>\n"
    assert f.getvalue() == expected


# STEP 2 TESTS
# Html class, Body class, Paragraph class
def test_html_element_render_w_indent_w_two_lines():
    page = hr.Html("one")
    page.append("two")
    f = StringIO()
    page.render(f, "   ")
    expected = "   <html>\n      one\n      two\n   </html>\n"
    assert f.getvalue() == expected

def test_body_element_render_w_indent_w_two_lines():
    page = hr.Body("one")
    page.append("two")
    f = StringIO()
    page.render(f, "   ")
    expected = "   <body>\n      one\n      two\n   </body>\n"
    assert f.getvalue() == expected

def test_paragraph_element_render_w_indent_w_two_lines():
    page = hr.P("one")
    page.append("two")
    f = StringIO()
    page.render(f, "   ")
    expected = "   <p>\n      one\n      two\n   </p>\n"
    assert f.getvalue() == expected

def test_recursive_render():
    page = hr.Html()
    body = hr.Body()
    p1 = hr.P()
    body.append(p1)
    page.append(body)
    f = StringIO()
    page.render(f)
    expected = "<html>\n" \
               "   <body>\n" \
               "      <p>\n" \
               "      </p>\n" \
               "   </body>\n" \
               "</html>\n"
    assert f.getvalue() == expected

def test_recursive_render_with_multiple_paragraphs():
    page = hr.Html()
    body = hr.Body()
    p1 = hr.P("Here is a paragraph of text")
    p2 = hr.P()
    p2.append("And here is another piece of text")
    body.append(p1)
    body.append(p2)
    page.append(body)
    f = StringIO()
    page.render(f)
    expected = "<html>\n" \
               "   <body>\n" \
               "      <p>\n" \
               "         Here is a paragraph of text\n" \
               "      </p>\n" \
               "      <p>\n" \
               "         And here is another piece of text\n" \
               "      </p>\n" \
               "   </body>\n" \
               "</html>\n"
    assert f.getvalue() == expected

def test_step_2_html_output():
    page = hr.Html()
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough  to show that we can do some text"))
    body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
    page.append(body)
    f = StringIO()
    page.render(f)
    expected = "<html>\n" \
               "   <body>\n" \
               "      <p>\n" \
               "         Here is a paragraph of text -- there could be more of them, but this is enough " \
               " to show that we can do some text\n" \
               "      </p>\n" \
               "      <p>\n" \
               "         And here is another piece of text -- you should be able to add any number\n" \
               "      </p>\n" \
               "   </body>\n" \
               "</html>\n"
    assert f.getvalue() == expected


# STEP 3 TESTS
# Head class, OneLineTag class, Title class
def test_title_render_empty_content():
    page = hr.Title()
    f = StringIO()
    page.render(f)
    expected = "<title></title>\n"
    assert f.getvalue() == expected

def test_title_render():
    page = hr.Title("this is a title")
    f = StringIO()
    page.render(f)
    expected = "<title>this is a title</title>\n"
    assert f.getvalue() == expected

def test_title_render_append_to_empty_content():
    page = hr.Title()
    page.append("this is a title")
    f = StringIO()
    page.render(f)
    expected = "<title>this is a title</title>\n"
    assert f.getvalue() == expected

def test_title_render_append_to_nonempty_content():
    page = hr.Title("this is a title")
    page.append("this is a second title")
    f = StringIO()
    page.render(f)
    expected = "<title>this is a title this is a second title</title>\n"
    assert f.getvalue() == expected

def test_step_3_html_output():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough  to show that we can do some text"))
    body.append(hr.P("And here is another piece of text -- you should be able to add any number"))
    page.append(body)
    f = StringIO()
    page.render(f)
    expected = "<html>\n" \
               "   <head>\n" \
               "      <title>PythonClass = Revision 1087:</title>\n" \
               "   </head>\n" \
               "   <body>\n" \
               "      <p>\n"\
               "         Here is a paragraph of text -- there could be more of them, but this is enough " \
               " to show that we can do some text\n" \
               "      </p>\n" \
               "      <p>\n" \
               "         And here is another piece of text -- you should be able to add any number\n" \
               "      </p>\n" \
               "   </body>\n" \
               "</html>\n"
    assert f.getvalue() == expected


# STEP 4 TESTS
# Attributes keyword inputs
def test_element_init_w_attributes():
    page = hr.Element("some text content", id="TheList", style="line=height:200%")
    f = StringIO()
    page.render(f)
    expected = '<html id="TheList" style="line=height:200%">\n   some text content\n</html>\n'
    assert f.getvalue() == expected

def test_element_init_w_clas_attribute():
    page = hr.P("some content", clas="intro")
    f = StringIO()
    page.render(f)
    expected = '<p class="intro">\n   some content\n</p>\n'
    assert f.getvalue() == expected

def test_step_4_html_output():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, but this is enough "
                     " to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    page.append(body)
    f = StringIO()
    page.render(f)
    expected = "<html>\n" \
               "   <head>\n" \
               "      <title>PythonClass = Revision 1087:</title>\n" \
               "   </head>\n" \
               "   <body>\n" \
               '      <p style="text-align: center; font-style: oblique;">\n' \
               "         Here is a paragraph of text -- there could be more of them, but this is enough " \
               " to show that we can do some text\n" \
               "      </p>\n" \
               "   </body>\n" \
               "</html>\n"
    assert f.getvalue() == expected


# STEP 5 TESTS
# SelfClosingTag class, Hr class, Br class
def test_hr_element_init():
    page = hr.Hr()
    f = StringIO()
    page.render(f)
    expected = "<hr />\n"
    assert f.getvalue() == expected

def test_br_element_init():
    page = hr.Br()
    f = StringIO()
    page.render(f)
    expected = "<br />\n"
    assert f.getvalue() == expected

def test_self_closing_tag_init_w_content_raises_error():
    message = ""
    try:
        _ = hr.Hr("this is content")
    except TypeError as e:
        message = e.args[0]
    finally:
        assert message == "'SelfClosingTag' object cannot have any content"

def test_self_closing_tag_init_w_kwargs_raises_error():
    message = ""
    try:
        _ = hr.Hr(id="one", clas="two")
    except TypeError as e:
        message = e.args[0]
    finally:
        assert message == "'SelfClosingTag' object cannot have any content"

def test_self_closing_tag_append_raises_error():
    page = hr.Hr()
    message = ""
    try:
        page.append("this is content")
    except TypeError as e:
        message = e.args[0]
    finally:
        assert message == "'SelfClosingTag' object cannot have any content"

def test_step_5_html_output():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough  to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    page.append(body)
    f = StringIO()
    page.render(f)
    expected = "<html>\n" \
               "   <head>\n" \
               "      <title>PythonClass = Revision 1087:</title>\n" \
               "   </head>\n" \
               "   <body>\n" \
               '      <p style="text-align: center; font-style: oblique;">\n' \
               "         Here is a paragraph of text -- there could be more of them, but this is enough " \
               " to show that we can do some text\n" \
               "      </p>\n" \
               "      <hr />\n" \
               "   </body>\n" \
               "</html>\n"
    assert f.getvalue() == expected


# STEP 6 TESTS
# Anchor class
def test_anchor_element_init():
    page = hr.A("http://google.com", "link to google")
    f = StringIO()
    page.render(f)
    expected = '<a href="http://google.com">link to google</a>\n'
    assert f.getvalue() == expected

def test_step_6_html_output():
    page = hr.Html()
    head = hr.Head()
    head.append(hr.Title("PythonClass = Revision 1087:"))
    page.append(head)
    body = hr.Body()
    body.append(hr.P("Here is a paragraph of text -- there could be more of them, "
                     "but this is enough  to show that we can do some text",
                     style="text-align: center; font-style: oblique;"))
    body.append(hr.Hr())
    body.append("And this is a ")
    body.append(hr.A("http://google.com", "link"))
    body.append("to google")
    page.append(body)
    f = StringIO()
    page.render(f)
    expected = "<html>\n" \
               "   <head>\n" \
               "      <title>PythonClass = Revision 1087:</title>\n" \
               "   </head>\n" \
               "   <body>\n" \
               '      <p style="text-align: center; font-style: oblique;">\n' \
               "         Here is a paragraph of text -- there could be more of them, but this is enough " \
               " to show that we can do some text\n" \
               "      </p>\n" \
               "      <hr />\n" \
               "      And this is a \n" \
               '      <a href="http://google.com">link</a>\n' \
               "      to google\n" \
               "   </body>\n" \
               "</html>\n"
    assert f.getvalue() == expected
