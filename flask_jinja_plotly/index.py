import jinja2
# case 1
# templateStr = """
# Hi, my name is {{name}}.
# I am {{age}} years old.
# I live in {{city}}
# """

# # create jinja template object from a string

# template = jinja2.Environment(
#     loader = jinja2.BaseLoader
# ).from_string(templateStr)

# case 2
template = jinja2.Environment(
    loader = jinja2.FileSystemLoader("templates"),
    # autoescape=jinja2.select_autoescapeW
                                    
).get_template("bio_template.txt")


#Render data in jinja template object
contex = {"name":"James","age":32,"city":"Mumbai"}

renderedText = template.render(contex)

# renderedText = template.render(contex)
print(renderedText)
