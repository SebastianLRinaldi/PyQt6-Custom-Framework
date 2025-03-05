from application_draft.FrontEnd.presentations.myFirstWindow.myFirstWindowWidgets import *








def on_click() -> None:
    pass
    # self.event_bus.emit('widget_update', "status_label_main", {'text': 'Button clicked!'})

def update_label() -> None:
    label.setText("I have been updated!")
    
    
    # if widget_name in self.widgets:
    #     self.widgets[widget_name].setText(data.get('text', ''))