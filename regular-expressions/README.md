# Regular Expressions in Python
- A RegEx or a regular expression is a sequence of characters that forms a search pattern
- RegEx can be used to check whether a string contains a specified search pattern or not

## Metacharacters
- `[]` :- A set of characters
  - ex: `[a-m]`
- `\` :- Signals a special sequence (can be used to escape special characters)
  - ex: `\d`
- `.` :- Any character except a new line character
  - ex: `he..o`
- `^` :- Starts with
  - ex: `^hello`
- `$` :- Ends with
  - ex: `planet$`
- `*` :- Zero or more occurrences
  - ex: `he.*o`
- `+` :- One or more occurrences
  - ex: `he.+o`
- `?` :- Zero or more occurrences
  - ex: `he.?o`
- `{}` :- Exactly the specified number of occurrences
  - ex: `he.{2}o`
- `|` :- Either or
  - ex: `falls|stays`
- `()` :- Capture and group


# Python re Module methods

- `findall(pattern, text)` : returns a list containing all the matches
- `search(pattern, text)` : returns a Match object if there is a match in the string
- `split(pattern, text, max_splits)` : returns a list contains the split string
- `sub(pattern, replace_text, text)` : replace matched text with the text of our choice