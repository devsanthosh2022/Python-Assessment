def justify_paragraph(paragraph, page_width):
    try:
        # Attempt to convert page width to an integer
        try:
            page_width = int(page_width)
        except ValueError:
            print("Error: Page width must be a valid integer.")
            return None

        # Check if the page width is a positive integer
        if page_width <= 0:
            raise ValueError("Page width must be a positive integer.")
        elif page_width == 0:
            raise ValueError("Page width cannot be zero.")

        # Check if the paragraph is empty
        if not paragraph:
            print("Error: Paragraph cannot be empty.")
            return None

        # Check if the paragraph contains very long words
        if any(len(word) > page_width for word in paragraph.split()):
            raise ValueError("Paragraph contains very long words that cannot fit within the specified page width.")

        # Split the paragraph into words
        words = paragraph.split()
        lines = []
        current_line = []
        current_length = 0

        # Step 1: Organize words into lines that fit within the specified width
        for word in words:
            word_length = len(word)
            if current_length + len(current_line) + word_length <= page_width:
                # Add the word to the current line if it fits
                current_line.append(word)
                current_length += word_length
            else:
                # Start a new line when the current line exceeds the width
                lines.append(current_line)
                current_line = [word]
                current_length = word_length

        if current_line:
            lines.append(current_line)

        justified = []

        # Step 2: Justify each line to evenly distribute spaces between words
        for line in lines:
            if len(line) > 1:  # If there's more than one word in the line
                total_length = sum(len(word) for word in line)
                total_spaces = page_width - total_length

                num_spaces = len(line) - 1
                spaces_between_words = total_spaces // num_spaces
                extra_spaces = total_spaces % num_spaces

                justified_line = ""
                for i, word in enumerate(line):
                    justified_line += word
                    if i < num_spaces:
                        # Distribute spaces evenly between words
                        spaces_to_add = spaces_between_words + (1 if i < extra_spaces else 0)
                        justified_line += ' ' * spaces_to_add

                justified.append(justified_line)
            else:
                # If there's only one word in the line, left-justify it
                justified.append(line[0].ljust(page_width))

        return justified

    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # User input: paragraph and page width
    paragraph_input = input("Enter the paragraph: ")
    page_width_input = input("Enter the page width: ")

    justified_text = justify_paragraph(paragraph_input, page_width_input)

    if justified_text is not None:
        print("\nJustified Text:")
        for i, line in enumerate(justified_text, 1):
            print(f"Line {i}: {line}")
