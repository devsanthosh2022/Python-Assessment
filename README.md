# Justify Text Function

## Description
The `justify_paragraph` function justifies text within a specified page width by evenly distributing spaces between words. It takes a paragraph and page width as inputs and returns an array of justified lines.

## Usage
To use the `justify_paragraph` function, provide a paragraph string and a page width as parameters. For example:

```python
paragraph = "Your paragraph here"
page_width = 20
justified_lines = justify_paragraph(paragraph, page_width)
```

## How It Works
1. The function first breaks the paragraph into individual words.
2. It then organizes these words into lines that fit within the specified width.
3. For each line, it calculates the required spaces to evenly distribute between the words for justification.
4. Finally, it returns an array of justified lines.

## Function Details
The justify_paragraph function:
  -  Splits the paragraph into words.
  -  Organizes words into lines that fit within the specified width.
  -  Calculates the necessary spaces to justify the text.
  -  Returns an array of justified lines.

## Example
paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
page_width = 20

the output might be:

Array[1] = 'This   is  a  sample'
Array[2] = 'text      but      a'
Array[3] = 'complicated  problem'
Array[4] = 'to  be solved, so we'
Array[5] = 'are adding more text'
Array[6] = 'to   see   that   it'
Array[7] = 'actually      works.'
