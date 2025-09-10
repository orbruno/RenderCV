from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader("app/templates"))

# Load the template
template = env.get_template("cv.html")

# Example data to render
example_data = {
    "name": "John Doe",
    "title": "Software Engineer",
    # Add other fields as needed for your template
}

# Render the template
html_output = template.render(**example_data)

# Print or save the result
with open("tests/test_cv_rendered.html", "w") as f:
    f.write(html_output)
print("Rendered HTML saved to tests/test_cv_rendered.html")
