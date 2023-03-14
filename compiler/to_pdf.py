from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape

template = '../resume-en.tex'
with open(template, 'r') as f:
    template = f.read()

doc = Document(template)
doc.generate_pdf('resume-en', clean_tex=True)
print('your resuem is ready!')

