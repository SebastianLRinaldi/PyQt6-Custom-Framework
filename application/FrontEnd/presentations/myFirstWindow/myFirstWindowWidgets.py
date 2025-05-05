from application.FrontEnd.B_WidgetsFolder.widgetConfiguration import *
from application.FrontEnd.B_WidgetsFolder.webpageWidgetConfiguration import *
# Button
update_widget_btn = Button(text="Start")
reset_widget_btn = Button(text="Reset")

label = Label(text="Enter your name:")
check_box = CheckBox(text="Accept terms and conditions")
radio_button = RadioButton(text="Select this option")
calendar_widget = CalendarWidget()
list_widget = ListWidget()
text_edit = TextEdit(text="This is a multi-line text editor")

eWebPage = WebPage()
start_page_btn = Button(text="Start WebPage")
debug_page_btn = Button(text="Show WebPage Debug Data")
inject_css_btn = Button(text="Inject Blue")
highlight_elm_btn = Button(text="Highlight Element")
design_mode_btn = Button(text="Activate Design Mode")
devtools_btn =  Button(text="Activate Dev Tools")




url_input = LineEdit(text="URL GOES HERE")
change_url_btn = Button(text="Change to Entered URL")




# DevTools view
devtools_view = WebPage()
devtools_view.setWindowTitle("DevTools")




