import zope.interface
from data import Data

class ITextUserInterface(zope.interface.Interface):
    def setup(self) -> None:
        """Stup the tui"""
        pass
    def get_the_url(self, base_url: str) -> str:
        """Show the tui for enter the URL of the problem"""
        pass
    def confirm_data(self, data: Data) -> Data:
        """Show the tui for confirm the data and choose the language to solve the problem"""
        pass