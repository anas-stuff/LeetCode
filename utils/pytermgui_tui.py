import pytermgui as ptg
from data import Data

CONFIG = """
config:
    InputField:
        styles:
            prompt: dim italic
            cursor: '@72'
    Label:
        styles:
            value: dim bold

    Window:
        styles:
            border: '60'
            corner: '60'

    Container:
        styles:
            border: '96'
            corner: '96'
"""

problem_url = ""  # The URL of the problem

def setup() -> None:
    """ 
    Stup the pytermgui 
    load the config styles
    """
    with ptg.YamlLoader() as loader:
        loader.load(CONFIG)

def submit_url(manager: ptg.WindowManager, window: ptg.Window) -> None:
    """Submit the URL of the problem"""
    global problem_url
    for widget in window:
        if isinstance(widget, ptg.InputField):
            problem_url = widget.value
            break
    manager.stop()

def get_the_url(base_url: str) -> str:
    """ Show the tui using the pytermgui for enter the URL of the problem """
    with ptg.WindowManager() as wm:
        wm.layout.add_slot("Body")
        window = (
            ptg.Window(
                "",
                ptg.InputField(base_url, prompt="URL: "),
                "",
                ["Submit", lambda *_: submit_url(wm, window)],
                width=60,
                box="DOUBLE",
            )
            .set_title("[green bold]Enter the URL of the problem")
            .center()
        )
        wm.add(window)
        wm.run()
    return problem_url

def parse_data(manager: ptg.WindowManager, window: ptg.Window, data: Data) -> None:
    """ Parse the data and choose the language to solve the problem """
    for widget in window:
        if isinstance(widget, ptg.InputField):
            if widget.prompt == "Title: ":
                data.title = widget.value
            elif widget.prompt == "Level: ":
                data.level = widget.value
            elif widget.prompt == "Base path:":
                data.problem_path = widget.value
            elif widget.prompt == "Solve with:":
                # Remove the last comma if exists
                value = str(widget.value).strip()
                if value.endswith(","):
                    value = value[:-1]
                data.solve_with = [s.strip() for s in value.split(",")]
    manager.stop()

def confirm_data(data: Data) -> None:
    """ Show the tui using the pytermgui for confirm the data and choose the language to solve the problem """
    with ptg.WindowManager() as wm:
        wm.layout.add_slot("Body")
        window = (
            ptg.Window(
                "",
                ptg.InputField(data.title, prompt="Title: "),
                ptg.InputField(data.level, prompt="Level: "),
                ptg.InputField(data.problem_path, prompt="Base path:"),
                ptg.InputField("rust,", prompt="Solve with:"),
                "",
                ["Confirm", lambda *_: parse_data(wm, window, data)],
                width=60,
                box="DOUBLE",
            )
            .set_title("[green bold]Confirm the data")
            .center()
        )
        wm.add(window)
        wm.run()