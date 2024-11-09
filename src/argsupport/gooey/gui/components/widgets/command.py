from argsupport.gooey.gui.components.widgets.textfield import TextField
from argsupport.gooey.python_bindings import types as t



__ALL__ = ('CommandField',)

class CommandField(TextField):

    def getUiState(self) -> t.FormField:
        return t.Command(**super().getUiState())  # type: ignore
