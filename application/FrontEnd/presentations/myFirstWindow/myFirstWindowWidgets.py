from application.FrontEnd.B_WidgetsFolder.widgetConfiguration import *
from application.FrontEnd.B_WidgetsFolder.webpageWidgetConfiguration import *
# Button
update_widget_btn = Button(text="Start")
reset_widget_btn = Button(text="Reset")

# Label
label = Label(text="Enter your name:")


# LineEdit
line_edit = LineEdit(text="Type something here")

# CheckBox
check_box = CheckBox(text="Accept terms and conditions")

# RadioButton
radio_button = RadioButton(text="Select this option")

calendar_widget = CalendarWidget()

list_widget = ListWidget()

# TextEdit
text_edit = TextEdit(text="This is a multi-line text editor")

# eWebPage = EmbeddedWebPage()
eWebPage = WebPage()
start_page_btn = Button(text="Start WebPage")
debug_page_btn = Button(text="Webview Debug Data")