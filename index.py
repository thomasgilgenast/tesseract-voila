# %%
import subprocess

import ipywidgets as widgets
from IPython.display import display


# output widget for logging
# comment out after debugging
out = widgets.Output()
# display(out)

# FileUpload widget and a VBox to hold it next to the Textarea output widget -
# it will be added to the VBox later inside on_change()
uploader = widgets.FileUpload(accept="", multiple=False)
vbox = widgets.VBox([uploader])


@out.capture()
def on_change(change):
    global vbox
    print("change detected")
    filename = list(uploader.value.keys())[0]
    image = uploader.value[filename]["content"]
    print(f"found uploaded image with filename {filename}")
    print("running tessaract...")
    text = subprocess.run(
        "tesseract stdin stdout",
        input=image,
        capture_output=True,
        shell=True,
        check=True,
    ).stdout.decode("utf-8")
    print("done running tessaract; found text:")
    print(text)
    print("that was the text")
    vbox.children = [
        uploader,
        # by default, inline widgets inside the VBox have their width pinned to
        # be very narrow and the Textarea cannot be resized to wider sizes by
        # dragging the corner dragger (it can only be resized vertically)
        # our workaround involves using this Layout to pre-maximize the width
        widgets.Textarea(value=text, rows=20, layout=widgets.Layout(width="90%")),
    ]


uploader.observe(on_change, "value")
out.append_stdout("voila started\n")
vbox
