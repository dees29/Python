def my_print(txt):
    print(txt)


msg_template="""Hello {name},
Thank you for joining {website}.
happy to have you with us.
"""#.format(name="Deepu", website='cfe.sh')

def format_msg(my_name="Deepu", my_website='cfe.sh'):
    my_msg=msg_template.format(name=my_name, website=my_website)
    #print(my_msg)
    return my_msg


"""
"{} {}".format("abc",123)
"{1} {0}".format("abc",123)
"{name} {number}".format(name="abc", number=123)

"{} {name} {number}".format("another", name="abc", number=123)
"""


def base_funcation(*args, **kwargs):
    print(args,kwargs)