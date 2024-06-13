import re
NUMBER = re.compile("[0-9]")
WHITESPACE = re.compile(" |\\n|\\t")
IDENTIFIER = re.compile("^([A-Za-z][_|\w]*)")
BINOP = re.compile("+ | - | * | / | < | > | <= | >= | == | != | ^")
