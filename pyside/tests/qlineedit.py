"""Tests for QLineEdit."""
from PySide2.QtWidgets import QApplication, QLineEdit

# NOTE: I'm choosing not to implement this.  It opens the door to inumerable
#  Optional[str] arguments throughout PySide.  If you want to clear a text
#  item, use setText('').  One good aspect of static typing is it allows us
#  to be more intentional.

# test that QLineEdit.setText() accepts None as parameter
# edit = QLineEdit()
# edit.setText(None)
