import hyperdiv as hd
from .state import ChartState



def chart():
    state = ChartState()

    hd.line_chart(
        state.get_coordinates(),
        x_axis="linear",
        padding=1,
        background_color="neutral-50",
        border_radius="large",
        grid_color="neutral-200",
        height=20,
        shrink=False
    )


def reset_button():
    state = ChartState()
    with hd.hbox(align="center", justify="center"):
        if len(state.get_coordinates()) > 0:
            if hd.button("Reset",  variant="danger" ).clicked:
                state.reset_coordinates()


def float_validation(value):
    try:
        float(value)
    except:
        return "Input should be a valid float number"

def add_coordinates():
    state = ChartState()
    # The form for adding a new host.
    with hd.form() as form:
        x =form.text_input(placeholder="X value", name="x-value", validation=float_validation)
        y= form.text_input(placeholder="Y value", name="y-value", validation=float_validation)

        form.submit_button("Add", prefix_icon="plus", variant="primary")

    if form.submitted:
        x = float(form.form_data["x-value"])
        y = float(form.form_data["y-value"])
        state.add_coordinates(x, y)
        form.reset()


def main():
    app = hd.template(title="Line Chart", sidebar=False)
    app.body.padding = 4
    app.body.gap = 2
    with app.body:
        chart()
        reset_button()
        add_coordinates()
