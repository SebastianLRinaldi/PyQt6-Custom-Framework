from FrontEnd.B_WidgetsFolder.WidgetConfigurations.widgetConfiguration import *

button = Button(text="A Build Button", widgetRow=0,widgetCol=0)
tableLabel = TrackTableLabel("A Build Label", widgetRow=0,widgetCol=1)
table = TrackTabel(widgetRow=1)



button1 = Button(text="A Build Button1")


tableLabel1 = TrackTableLabel("A Build Label1")

button2 = Button(text="A Build Button2")
tableLabel2 = TrackTableLabel("A Build Label2")


# button.clicked.connect(tableLabel.update_label)