# mypy: disable-error-code="misc, override, no-redef"

PySideModule: str

def GetPySideModule(): ...
def bindTexture(self, qimage): ...
def initQGLWidget(self, glFormat, parent): ...
def isContextInitialised(self): ...
def releaseTexture(self, tex): ...
