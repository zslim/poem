def read_file(path):
    with open(path, "r") as f:
        content = f.readlines()
    return content


def write_file(content, original_path):
    new_path = f"html_{original_path}"
    with open(new_path, "w") as f:
        f.write(content)


def clear_line_breaks(lines):
    return [line[:-1] for line in lines]


def separate_parts(text):
    core = clear_line_breaks(text)
    title = core.pop(0)
    date = core.pop(-1)
    return title, core, date


def create_html(title, core):
    headline_start = "<h1>"
    headline_end = "</h1>"
    p_start = "<p>"
    p_end = "</p>"
    br_tag = "<br>"
    html = [f"{headline_start}{title}{headline_end}"]
    inside_paragraph = False
    first_empty_line = True
    for line in core:
        if line == "" and inside_paragraph and first_empty_line:
            html.append(p_end)
            inside_paragraph = False
            first_empty_line = False
        elif line != "":
            if not inside_paragraph:
                html.append(p_start)
                inside_paragraph = True
            html.append(line + br_tag)
            first_empty_line = True
    return "".join(html)


def format_text(text):
    title, core, date = separate_parts(text)
    return create_html(title, core)


if __name__ == '__main__':
    path = "lenyomat.txt"
    text = read_file(path)
    output = format_text(text)
    write_file(output, path)
