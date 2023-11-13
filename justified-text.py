def justify_paragraph(paragraph, page_width):
    words = paragraph.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        word_length = len(word)
        if current_length + len(current_line) + word_length <= page_width:
            current_line.append(word)
            current_length += word_length
        else:
            lines.append(current_line)
            current_line = [word]
            current_length = word_length

    if current_line:
        lines.append(current_line)

    # making the text left and right justified
    justified = []
    for line in lines:
        if len(line) > 1:
            num_spaces = page_width - sum(len(word) for word in line)
            num_gaps = len(line) - 1
            spaces_between_words = num_spaces // num_gaps
            extra_spaces = num_spaces % num_gaps

            justified_line = ""
            for i, word in enumerate(line):
                justified_line += word
                if i < num_gaps:
                    spaces_to_add = spaces_between_words + (1 if i < extra_spaces else 0)
                    justified_line += ' ' * spaces_to_add

            justified.append(justified_line)
        else:
            justified.append(line[0].ljust(page_width))

    return justified

# Input the paragraph and the page width
paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
page_width = 20

# Justify and store in an array
array = justify_paragraph(paragraph, page_width)

# Print the array
print("Justified Text Array:")
for i, line in enumerate(array, 1):
    print(f"Array[{i}] = '{line}'")
