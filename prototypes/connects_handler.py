"""
v0
"""

# # screen_manager.py
# from PyQt6.QtCore import QObject, pyqtSignal
# from typing import Dict, Any

# class ScreenManager(QObject):
#     def __init__(self):
#         super().__init__()
#         self.screens: Dict[str, 'BaseScreen'] = {}
#         self.connections: Dict[str, list] = {}
        
#     def register_screen(self, screen_id: str, screen: 'BaseScreen'):
#         self.screens[screen_id] = screen
        
#     def connect_signals(self, from_screen: str, to_screen: str, 
#                         signal_name: str, slot_name: str):
#         if from_screen not in self.connections:
#             self.connections[from_screen] = []
            
#         connection = {
#             'to_screen': to_screen,
#             'signal': signal_name,
#             'slot': slot_name
#         }
#         self.connections[from_screen].append(connection)
        
#         # Establish the connection
#         getattr(self.screens[from_screen], signal_name).connect(
#             getattr(self.screens[to_screen], slot_name)
#         )
        
# # base_screen.py
# from PyQt6.QtCore import QObject, pyqtSignal
# from typing import Any

# class BaseScreen(QObject):
#     def __init__(self, screen_id: str):
#         super().__init__()
#         self.screen_id = screen_id
#         self.manager = None
        
#     def set_manager(self, manager: 'ScreenManager'):
#         self.manager = manager
        
#     def connect_to(self, screen_id: str, signal_name: str, slot_name: str):
#         if self.manager:
#             self.manager.connect_signals(
#                 self.screen_id,
#                 screen_id,
#                 signal_name,
#                 slot_name
#             )

# # example_screen.py
# from PyQt6.QtCore import pyqtSignal
# # from base_screen import BaseScreen

# class ExampleScreen(BaseScreen):
#     signal_1 = pyqtSignal()
#     signal_2 = pyqtSignal(str)
    
#     def __init__(self, screen_id: str):
#         super().__init__(screen_id)
#         self.signal_1.connect(self.handle_signal_1)
        
#     def handle_signal_1(self):
#         # Handle signal
#         pass
    
# # main.py
# # from screen_manager import ScreenManager
# # from screens.example_screen import ExampleScreen

# def main():
#     manager = ScreenManager()
    
#     # Create any number of screens
#     screen1 = ExampleScreen("screen1")
#     screen2 = ExampleScreen("screen2")
#     screen3 = ExampleScreen("screen3")
    
#     # Register screens
#     manager.register_screen("screen1", screen1)
#     manager.register_screen("screen2", screen2)
#     manager.register_screen("screen3", screen3)
    
#     # Connect screens in any pattern
#     manager.connect_signals("screen1", "screen2", "signal_1", "handle_signal_1")
#     manager.connect_signals("screen2", "screen3", "signal_1", "handle_signal_1")
#     manager.connect_signals("screen3", "screen1", "signal_1", "handle_signal_1")
    
#     # Add more screens and connections as needed
#     screen4 = ExampleScreen("screen4")
#     manager.register_screen("screen4", screen4)
#     manager.connect_signals("screen1", "screen4", "signal_2", "handle_signal_2")


"""
v1
"""
# from PyQt6.QtCore import *
# from PyQt6.QtWidgets import * 
# from PyQt6.QtGui import *
# from PyQt6.QtCore import *
# from typing import Dict, List

# class EventBus(QObject):
#     """Central event manager for broadcasting events between screens and widgets"""
    
#     # Generic signals for screen-widget interactions
#     widget_update = pyqtSignal(str, str, dict)  # screen_id, widget_type, data
#     screen_transition = pyqtSignal(str, dict)   # target_screen, params
    
#     def __init__(self):
#         super().__init__()
#         self._listeners = {}  # Store listeners for different event types
        
#     def emit(self, event_type: str, **kwargs):
#         """Emit an event to all registered listeners"""
#         if hasattr(self, event_type):
#             getattr(self, event_type).emit(**kwargs)

# class ScreenBase(QWidget):
#     """Base class for all screens"""
#     def __init__(self, event_bus: EventBus, screen_id: str):
#         super().__init__()
#         self.event_bus = event_bus
#         self.screen_id = screen_id
#         self.widgets: Dict[str, QWidget] = {}
        
#     def add_widget(self, widget_type: str, widget: QWidget):
#         """Register a widget with the screen"""
#         self.widgets[widget_type] = widget
        
#     def update_widget(self, widget_type: str, data: dict):
#         """Update a specific widget"""
#         self.event_bus.emit('widget_update', 
#                         screen_id=self.screen_id,
#                         widget_type=widget_type,
#                         data=data)

# class WidgetBase(QWidget):
#     """Base class for all widgets"""
#     def __init__(self, event_bus: EventBus, widget_type: str):
#         super().__init__()
#         self.event_bus = event_bus
#         self.widget_type = widget_type
#         self.setup_listeners()
        
#     def setup_listeners(self):
#         """Set up event listeners for the widget"""
#         self.event_bus.widget_update.connect(self.on_update)
        
#     def on_update(self, screen_id: str, widget_type: str, data: dict):
#         """Handle updates from screens"""
#         if widget_type == self.widget_type:
#             self.process_update(data)

# # Example usage
# class MyScreen(ScreenBase):
#     def __init__(self, event_bus: EventBus, screen_id: str):
#         super().__init__(event_bus, screen_id)
        
#         # Add two widgets
#         self.add_widget("widget1", MyWidget1(event_bus, "widget1"))
#         self.add_widget("widget2", MyWidget2(event_bus, "widget2"))

# class MyWidget1(WidgetBase):
#     def process_update(self, data: dict):
#         # Handle updates from screens
#         print(f"Widget 1 received: {data}")

# class MyWidget2(WidgetBase):
#     def process_update(self, data: dict):
#         # Handle updates from screens
#         print(f"Widget 2 received: {data}")




# from typing import Any, Callable, Dict, List, Optional
# from PyQt6.QtCore import QObject, pyqtSignal, QThread
# from PyQt6.QtCore import *
# from PyQt6.QtWidgets import * 
# from PyQt6.QtGui import *
# from PyQt6.QtCore import *
# from typing import Dict, List
# from queue import Queue
# import logging
# import inspect

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class EventBus(QObject):
#     """
#     Central event manager for broadcasting events between screens and widgets.
    
#     This implementation provides thread-safe event handling with proper error management
#     and type checking. Events are queued and processed in a dedicated thread to prevent
#     blocking the main UI thread.
#     """
    
#     # Define core signals
#     widget_update = pyqtSignal(str, str, dict)      # screen_id, widget_type, data
#     screen_transition = pyqtSignal(str, dict)       # target_screen, params
    
#     def __init__(self):
#         super().__init__()
#         self._listeners: Dict[str, List[Callable]] = {}
#         self._queue: Queue[tuple[str, dict]] = Queue()
#         self._thread = QThread()
#         self.moveToThread(self._thread)
#         self._thread.started.connect(self._process_queue)
#         self._running = True
        
#     def start(self) -> None:
#         """Start the event processing thread."""
#         self._thread.start()
        
#     def stop(self) -> None:
#         """Stop the event processing thread cleanly."""
#         self._running = False
#         self._thread.quit()
#         self._thread.wait()
        
#     def _process_queue(self) -> None:
#         """Process events in the queue thread."""
#         while self._running:
#             try:
#                 event_type, kwargs = self._queue.get()
#                 signal = getattr(self, event_type)
#                 signal.emit(**kwargs)
#             except Exception as e:
#                 logger.error(f"Error processing event {event_type}: {str(e)}")
#             finally:
#                 self._queue.task_done()

#     def emit(self, event_type: str, **kwargs) -> None:
#         """
#         Emit an event to all registered listeners.
        
#         Args:
#             event_type: Name of the signal to emit
#             **kwargs: Parameters matching the signal signature
            
#         Raises:
#             ValueError: If the event type doesn't exist
#             TypeError: If parameters don't match signal signature
#         """
#         try:
#             # Validate signal exists
#             if not hasattr(self, event_type):
#                 raise ValueError(f"Unknown signal: {event_type}")
                
#             # Get signal instance
#             signal = getattr(self, event_type)
            
#             # Validate it's actually a signal
#             if not isinstance(signal, pyqtSignal):
#                 raise TypeError(f"{event_type} is not a signal")
                
#             # Validate parameters match signal signature
#             param_types = [param.annotation for param in 
#                         inspect.signature(signal.emit).parameters.values()]
            
#             # Convert kwargs to match signal types
#             processed_kwargs = {}
#             for key, value in kwargs.items():
#                 target_type = param_types[list(kwargs.keys()).index(key)]
#                 processed_kwargs[key] = self._convert_value(value, target_type)
            
#             # Queue the event for thread-safe processing
#             self._queue.put((event_type, processed_kwargs))
            
#         except Exception as e:
#             logger.error(f"Error emitting event {event_type}: {str(e)}")
#             raise

#     @staticmethod
#     def _convert_value(value: Any, target_type: Any) -> Any:
#         """Convert a value to match the expected parameter type."""
#         if target_type == dict and not isinstance(value, dict):
#             return dict(value)
#         elif target_type == str and not isinstance(value, str):
#             return str(value)
#         return value

# class ScreenBase(QWidget):
#     """
#     Base class for all screens in the application.
    
#     Provides integration with the EventBus for widget management and event handling.
#     """
    
#     def __init__(self, event_bus: EventBus, screen_id: str):
#         super().__init__()
#         self.event_bus = event_bus
#         self.screen_id = screen_id
#         self.widgets: Dict[str, QWidget] = {}

#     def add_widget(self, widget_type: str, widget: QWidget) -> None:
#         """
#         Register a widget with the screen.
        
#         Args:
#             widget_type: Unique identifier for the widget type
#             widget: The widget instance to register
#         """
#         self.widgets[widget_type] = widget

#     def update_widget(self, widget_type: str, data: dict) -> None:
#         """
#         Update a specific widget by sending an event through the bus.
        
#         Args:
#             widget_type: Type of widget to update
#             data: Data to send to the widget
#         """
#         try:
#             self.event_bus.emit('widget_update',
#                             screen_id=self.screen_id,
#                             widget_type=widget_type,
#                             data=data)
#         except Exception as e:
#             logger.error(f"Failed to update widget {widget_type}: {str(e)}")

# class WidgetBase(QWidget):
#     """
#     Base class for all widgets in the application.
    
#     Handles registration with the event bus and provides basic event handling.
#     """
    
#     def __init__(self, event_bus: EventBus, widget_type: str):
#         super().__init__()
#         self.event_bus = event_bus
#         self.widget_type = widget_type
#         self.setup_listeners()

#     def setup_listeners(self) -> None:
#         """Set up event listeners for the widget."""
#         self.event_bus.widget_update.connect(self.on_update)

#     def on_update(self, screen_id: str, widget_type: str, data: dict) -> None:
#         """
#         Handle updates from screens.
        
#         Args:
#             screen_id: ID of the screen sending the update
#             widget_type: Type of widget being updated
#             data: Update data
#         """
#         if widget_type != self.widget_type:
#             return
            
#         try:
#             self.process_update(data)
#         except Exception as e:
#             logger.error(f"Widget {self.widget_type} failed to process update: {str(e)}")

#     def process_update(self, data: dict) -> None:
#         """
#         Process the update data.
        
#         Override this method in subclasses to handle specific updates.
        
#         Args:
#             data: Dictionary containing the update data
#         """
#         raise NotImplementedError("Subclasses must implement process_update")
    
    
# from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout
# import sys

# class MyScreen(ScreenBase):
#     def __init__(self, event_bus: EventBus):
#         super().__init__(event_bus, "main_screen")
        
#         # Add widgets
#         self.add_widget("counter_button", QPushButton("Click Me"))
#         self.add_widget("status_label", QLabel("Ready"))

# class MyWidget(WidgetBase):
#     def process_update(self, data: dict) -> None:
#         """Handle updates from screens."""
#         print(f"Received update: {data}")

# def main():
#     app = QApplication(sys.argv)
    
#     # Initialize event bus
#     event_bus = EventBus()
#     event_bus.start()
    
#     # Create screen and widgets
#     screen = MyScreen(event_bus)
    
#     # Clean up on exit
#     def cleanup():
#         event_bus.stop()
#         app.quit()
    
#     app.aboutToQuit.connect(cleanup)
    
#     screen.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()



"""
Never worked but base for all needed items
"""
# import sys
# from typing import Any, Callable, Dict, List, Optional
# from PyQt6.QtCore import QObject, pyqtSignal, QThread
# from PyQt6.QtCore import *
# from PyQt6.QtWidgets import *
# from PyQt6.QtGui import *
# from PyQt6.QtCore import *
# from typing import Dict, List
# from queue import Queue
# import logging
# import inspect

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class EventBus(QObject):
#     """Central event manager for broadcasting events between screens and widgets.
#     This implementation provides thread-safe event handling with proper error management
#     and type checking. Events are queued and processed in a dedicated thread to prevent
#     blocking the main UI thread."""
    
#     # # Define core signals
#     widget_update = pyqtSignal(str, str, dict)      # screen_id, widget_type, data
#     screen_transition = pyqtSignal(str, dict)       # target_screen, params
    

#     def __init__(self):
#         super().__init__()
#         self._listeners: Dict[str, List[Callable]] = {}
#         self._queue: Queue[tuple[str, dict]] = Queue()
#         self._thread = QThread()
#         self.moveToThread(self._thread)
#         self._thread.started.connect(self._process_queue)
#         self._running = True
        
#         self._signal_signatures = {
#             'widget_update': (str, str, dict),
#             'screen_transition': (str, dict),
#             }

#     def start(self) -> None:
#         """Start the event processing thread."""
#         self._thread.start()

#     def stop(self) -> None:
#         """Stop the event processing thread cleanly."""
#         self._running = False
#         self._thread.quit()
#         self._thread.wait()

#     def _process_queue(self) -> None:
#         """Process events in the queue thread."""
#         while self._running:
#             try:
#                 event_type, kwargs = self._queue.get()
#                 signal = getattr(self, event_type)
#                 # signal.emit(**kwargs)
#                 signal.emit(*kwargs.values())
#             except Exception as e:
#                 logger.error(f"Error processing event {event_type}: {str(e)}")
#             finally:
#                 self._queue.task_done()

#     def emit(self, event_type: str, **kwargs) -> None:
#         """Emit an event to all registered listeners.
#         Args:
#             event_type: Name of the signal to emit
#             **kwargs: Parameters matching the signal signature
#         Raises:
#             ValueError: If the event type doesn't exist
#             TypeError: If parameters don't match signal signature"""
#         try:
#             # Validate signal exists
#             if not hasattr(self, event_type):
#                 raise ValueError(f"Unknown signal: {event_type}")
            
#             # Get signal instance
#             signal = getattr(self, event_type)
            
#             # Validate it's actually a signal
#             # if not isinstance(signal, pyqtSignal):
#             if not isinstance(signal, pyqtBoundSignal):
#                 raise TypeError(f"{event_type} is not a signal")
            
#             # Validate parameters match signal signature
#             param_types = [param.annotation for param in 
#                         inspect.signature(signal.emit).parameters.values()]
            

            
#             # Convert kwargs to match signal types
#             processed_kwargs = {}
#             for key, value in kwargs.items():
#                 target_type = param_types[list(kwargs.keys()).index(key)]
#                 processed_kwargs[key] = self._convert_value(value, target_type)
            
#             # Queue the event for thread-safe processing
#             self._queue.put((event_type, processed_kwargs))
#         except Exception as e:
#             logger.error(f"Error emitting event {event_type}: {str(e)}")
#             raise

#     @staticmethod
#     def _convert_value(value: Any, target_type: Any) -> Any:
#         """Convert a value to match the expected parameter type."""
#         if target_type == dict and not isinstance(value, dict):
#             return dict(value)
#         elif target_type == str and not isinstance(value, str):
#             return str(value)
#         return value

# class ScreenBase(QWidget):
#     """Base class for all screens in the application.
#     Provides integration with the EventBus for widget management and event handling."""
    
#     def __init__(self, event_bus: EventBus, screen_id: str):
#         super().__init__()
#         self.event_bus = event_bus
#         self.screen_id = screen_id
#         self.widgets: Dict[str, QWidget] = {}
#         self._layout = QVBoxLayout()
#         self.setLayout(self._layout)
    
#     def add_widget(self, widget_type: str, widget: QWidget) -> None:
#         """Register a widget with the screen.
#         Args:
#             widget_type: Unique identifier for the widget type
#             widget: The widget instance to register"""
#         widget.setObjectName(widget_type)  # Set objectName to match widget_type
#         self.widgets[widget_type] = widget
#         self._layout.addWidget(widget)
    
#     def update_widget(self, widget_type: str, data: dict) -> None:
#         """Update a specific widget by sending an event through the bus.
#         Args:
#             widget_type: Type of widget to update
#             data: Data to send to the widget"""
#         try:
#             self.event_bus.emit('widget_update',
#                               screen_id=self.screen_id,
#                               widget_type=widget_type,
#                               data=data)
#         except Exception as e:
#             logger.error(f"Failed to update widget {widget_type}: {str(e)}")
# class WidgetBase(QWidget):
#     """Base class for all widgets in the application.
#     Handles registration with the event bus and provides basic event handling."""
    
#     def __init__(self, event_bus: EventBus, widget_type: str):
#         super().__init__()
#         self.event_bus = event_bus
#         self.widget_type = widget_type
#         self.setObjectName(widget_type)  # Set objectName to match widget_type
#         self.setup_listeners()

#     def setup_listeners(self) -> None:
#         """Set up event listeners for the widget."""
#         self.event_bus.widget_update.connect(self.on_update)

#     def on_update(self, screen_id: str, widget_type: str, data: dict) -> None:
#         """Handle updates from screens.
#         Args:
#             screen_id: ID of the screen sending the update
#             widget_type: Type of widget being updated
#             data: Update data"""
#         if widget_type != self.objectName():
#             return
#         try:
#             self.process_update(data)
#         except Exception as e:
#             logger.error(f"Widget {self.objectName()} failed to process update: {str(e)}")

#     def process_update(self, data: dict) -> None:
#         """Process the update data.
#         Override this method in subclasses to handle specific updates.
#         Args:
#             data: Dictionary containing the update data"""
#         raise NotImplementedError("Subclasses must implement process_update")

# class MyScreen(ScreenBase):
#     def __init__(self, event_bus: EventBus):
#         super().__init__(event_bus, "main_screen")
#         # Add widgets
#         self.add_widget("counter_button", QPushButton("Click Me"))
#         self.add_widget("status_label", QLabel("Ready"))
        
        
# class MyScreen1(ScreenBase):
#     def __init__(self, event_bus: EventBus):
#         super().__init__(event_bus, "screen1")
#         self.add_widget("counter_button", QPushButton("Click Me"))
#         self.add_widget("status_label", QLabel("Ready"))
        
#         # Connect the button click to emit an event
#         self.widgets["counter_button"].clicked.connect(self.on_counter_button_clicked)
        
#     def on_counter_button_clicked(self):
#         # Emit event to update screen 3's status label
#         self.event_bus.emit('widget_update',
#                         screen_id="screen3",
#                         widget_type="status_label",
#                         data={'text': 'Button clicked!'})

# class MyScreen3(ScreenBase):
#     def __init__(self, event_bus: EventBus):
#         super().__init__(event_bus, "screen3")
#         self.add_widget("status_label", QLabel("Waiting for update"))

# class MyWidget(WidgetBase):
#     def process_update(self, data: dict) -> None:
#         """Handle updates from screens."""
#         print(f"Received update: {data}")

# def main():
#     app = QApplication(sys.argv)
#     # Initialize event bus
#     event_bus = EventBus()
#     event_bus.start()
    
#     # Create all screens
#     screen1 = MyScreen1(event_bus)
#     screen3 = MyScreen3(event_bus)
    
#     # Clean up on exit
#     def cleanup():
#         event_bus.stop()
#         app.quit()
#     app.aboutToQuit.connect(cleanup)
    
#     # Show all screens
#     screen1.show()
#     screen3.show()
    
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()


"""
working but,
uses screen id but its not really needed since in the design each widget will be different
"""
# import sys
# from PyQt6.QtCore import QObject, pyqtSignal, QThread
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
# from queue import Queue


# class EventBus(QObject):
#     widget_update = pyqtSignal(str, str, dict)

#     def __init__(self):
#         super().__init__()
#         self._queue = Queue()
#         self._thread = QThread()
#         self.moveToThread(self._thread)
#         self._thread.started.connect(self._process_queue)
#         self._running = True

#     def start(self):
#         self._thread.start()

#     def stop(self):
#         self._running = False
#         self._thread.quit()
#         self._thread.wait()

#     def emit(self, event_type, *args):
#         self._queue.put((event_type, args))

#     def _process_queue(self):
#         while self._running:
#             event_type, args = self._queue.get()
#             getattr(self, event_type).emit(*args)
#             self._queue.task_done()


# class ScreenBase(QWidget):
#     def __init__(self, event_bus, screen_id):
#         super().__init__()
#         self.event_bus = event_bus
#         self.screen_id = screen_id
#         self.widgets = {}
#         layout = QVBoxLayout()
#         self.setLayout(layout)

#     def add_widget(self, widget_type, widget):
#         self.widgets[widget_type] = widget
#         self.layout().addWidget(widget)


# class MyScreen1(ScreenBase):
#     def __init__(self, event_bus):
#         super().__init__(event_bus, "screen1")
#         button = QPushButton("Click Me")
#         self.add_widget("button", button)
#         button.clicked.connect(self.on_click)

#     def on_click(self):
#         self.event_bus.emit('widget_update', "screen3", "status_label", {'text': 'Button clicked!'})


# class MyScreen3(ScreenBase):
#     def __init__(self, event_bus):
#         super().__init__(event_bus, "screen3")
#         label = QLabel("Waiting...")
#         self.add_widget("status_label", label)
#         event_bus.widget_update.connect(self.update_label)

#     def update_label(self, screen_id, widget_type, data):
#         if screen_id == self.screen_id and widget_type in self.widgets:
#             self.widgets[widget_type].setText(data.get('text', ''))


# def main():
#     app = QApplication(sys.argv)
#     event_bus = EventBus()
#     event_bus.start()

#     screen1 = MyScreen1(event_bus)
#     screen3 = MyScreen3(event_bus)

#     screen1.show()
#     screen3.show()

#     app.aboutToQuit.connect(event_bus.stop)
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()



"""
IF we want some type of "text" signal to be emited
"""
# import sys
# from typing import Dict, TypeVar, Union
# from PyQt6.QtCore import QObject, pyqtSignal, QThread
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
# from queue import Queue

# # Generic type for the widget dictionary
# Q = TypeVar('Q', bound=QWidget)

# class EventBus(QObject):
#     widget_update = pyqtSignal(str, dict)

#     def __init__(self):
#         super().__init__()
#         self._queue = Queue()
#         self._thread = QThread()
#         self.moveToThread(self._thread)
#         self._thread.started.connect(self._process_queue)
#         self._running = True

#     def start(self):
#         self._thread.start()

#     def stop(self):
#         self._running = False
#         self._thread.quit()
#         self._thread.wait()

#     def emit(self, event_type: str, *args: Union[str, dict]):
#         self._queue.put((event_type, args))

#     def _process_queue(self):
#         while self._running:
#             event_type, args = self._queue.get()
#             getattr(self, event_type).emit(*args)
#             self._queue.task_done()


# class ScreenBase(QWidget):
#     def __init__(self, event_bus: EventBus):
#         super().__init__()
#         self.event_bus = event_bus
#         self.widgets: Dict[str, Union[QPushButton, QLabel]] = {}  # Refined type hint here for clarity
#         layout = QVBoxLayout()
#         self.setLayout(layout)

#     def add_widget(self, name: str, widget: QWidget) -> None:
#         widget.setObjectName(name)
#         self.widgets[name] = widget
#         self.layout().addWidget(widget)


# class MyScreen1(ScreenBase):
#     def __init__(self, event_bus: EventBus):
#         super().__init__(event_bus)
#         button = QPushButton("Click Me")
#         self.add_widget("button_click_me", button)
#         button.clicked.connect(self.on_click)

#     def on_click(self) -> None:
#         self.event_bus.emit('widget_update', "status_label_main", {'text': 'Button clicked!'})


# class MyScreen3(ScreenBase):
#     def __init__(self, event_bus: EventBus):
#         super().__init__(event_bus)
#         label = QLabel("Waiting...")
#         self.add_widget("status_label_main", label)
#         event_bus.widget_update.connect(self.update_label)

#     def update_label(self, widget_name: str, data: dict) -> None:
#         if widget_name in self.widgets:
#             self.widgets[widget_name].setText(data.get('text', ''))


# def main():
#     app = QApplication(sys.argv)
#     event_bus = EventBus()
#     event_bus.start()

#     screen1 = MyScreen1(event_bus)
#     screen3 = MyScreen3(event_bus)

#     screen1.show()
#     screen3.show()

#     app.aboutToQuit.connect(event_bus.stop)
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()


from PyQt6.QtCore import QObject, pyqtSignal

class MyEmitter(QObject):
    my_signal = pyqtSignal(str, int)
    another_signal = pyqtSignal()

    def do_something(self):
        self.my_signal.emit("Action performed", 100)
        self.another_signal.emit()

def my_slot(text, number):
    print(f"Slot received: {text}, {number}")

def another_slot():
    print("Another slot was triggered")

if __name__ == '__main__':
    emitter = MyEmitter()
    emitter.my_signal.connect(my_slot)
    emitter.another_signal.connect(another_slot)
    emitter.do_something()