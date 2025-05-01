from application.FrontEnd.B_WidgetsFolder.widgetConfiguration import *
from application.FrontEnd.B_WidgetsFolder.webpageWidgetConfiguration import *
# Button
button = Button(text="Start")
reset_button = Button(text="Reset")

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

eWebPage = EmbeddedWebPage()
start_ewebpage = Button(text="Start WebPage")
embed_ewebpage = Button(text="Embed WebPage")