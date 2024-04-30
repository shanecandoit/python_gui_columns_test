import fltk

# Create a new window
window = fltk.Fl_Window(800, 800, "4 Column GUI")

# Create 3 text editors
text_editor1 = fltk.Fl_Text_Editor(0, 0, 200, 800)
text_editor2 = fltk.Fl_Text_Editor(200, 0, 200, 800)
text_editor3 = fltk.Fl_Text_Editor(400, 0, 200, 800)

# Create a canvas and a read-only text editor in the fourth column
canvas = fltk.Fl_Box(600, 0, 200, 400)
text_editor4 = fltk.Fl_Text_Editor(600, 400, 200, 400)
# text_editor4.set_output(True)  # Make the text editor read-only
text_editor4.set_output()  # Make the text editor read-only

# Create 3 boxes to act as splitters
splitter1 = fltk.Fl_Box(200, 0, 5, 800)
splitter2 = fltk.Fl_Box(400, 0, 5, 800)
splitter3 = fltk.Fl_Box(600, 0, 5, 800)

# Set the box color to grey
splitter1.color(fltk.FL_GRAY)
splitter2.color(fltk.FL_GRAY)
splitter3.color(fltk.FL_GRAY)

# Set the text buffer for each text editor
text_buffer1 = fltk.Fl_Text_Buffer()
text_buffer2 = fltk.Fl_Text_Buffer()
text_buffer3 = fltk.Fl_Text_Buffer()
text_buffer4 = fltk.Fl_Text_Buffer()

text_buffer1.append("first:\n")
text_buffer2.append("second:\n")
text_buffer3.append("third:\n")
text_buffer4.append("fourth:\n")

text_editor1.buffer(text_buffer1)
text_editor2.buffer(text_buffer2)
text_editor3.buffer(text_buffer3)
text_editor4.buffer(text_buffer4)

# Show the window
window.end()
window.show()

# Start the FLTK event loop
fltk.Fl.run()