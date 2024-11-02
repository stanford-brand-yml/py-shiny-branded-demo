# This file demonstrates the use of a Stanford brand.yml file to theme a 
# Shiny for Python application.

# Modified from py-shiny/examples/brand/app.py
# https://github.com/posit-dev/py-shiny/blob/415ced034e6c500adda524abb7579731c32088b5/examples/brand/app.py#L8

import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from shiny import App, render, ui
from brand_yml import Brand

# Obtain the brand data from the brand.yml file
brand = Brand.from_yaml(__file__)

# Create a theme from the brand data
theme = ui.Theme.from_brand(brand)

## Usually, we'll want to directly use the brand file inside of shiny with:
# theme = ui.Theme.from_brand(__file__)

## However, for this example, we'll need to have the theme information separate.

## Extra demo to show tinting of the brand colors
theme.add_rules((Path(__file__).parent / "_colors.scss").read_text())

app_ui = ui.page_navbar(
    ui.nav_panel(
        "Input Output Demo",
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_slider("slider1", "Numeric Slider Input", 0, 11, 11),
                ui.input_numeric("numeric1", "Numeric Input Widget", 30),
                ui.input_date("date1", "Date Input Component", value="2024-01-01"),
                ui.input_switch("switch1", "Binary Switch Input", True),
                ui.input_radio_buttons(
                    "radio1",
                    "Radio Button Group",
                    choices=["Option A", "Option B", "Option C", "Option D"],
                ),
                ui.input_action_button("action1", "Action Button"),
            ),
            ui.layout_columns(
                ui.value_box(
                    "Metric 1",
                    "100",
                    theme="primary",
                ),
                ui.value_box(
                    "Metric 2",
                    "200",
                    theme="secondary",
                ),
                ui.value_box(
                    "Metric 3",
                    "300",
                    theme="info",
                ),
            ),
            ui.card(
                ui.card_header("Plot Output"),
                ui.output_plot("plot1"),
            ),
            ui.card(
                ui.card_header("Text Output"),
                ui.output_text_verbatim("out_text1"),
            ),
        ),
    ),
    ui.nav_panel(
        "Widget Gallery",
        ui.layout_column_wrap(
            ui.card(
                ui.card_header("Button Variants"),
                ui.input_action_button("btn1", "Default"),
                ui.input_action_button("btn2", "Primary", class_="btn-primary"),
                ui.input_action_button("btn3", "Secondary", class_="btn-secondary"),
                ui.input_action_button("btn4", "Info", class_="btn-info"),
                ui.input_action_button("btn5", "Success", class_="btn-success"),
                ui.input_action_button("btn6", "Warning", class_="btn-warning"),
                ui.input_action_button("btn7", "Danger", class_="btn-danger"),
            ),
            ui.card(
                ui.card_header("Radio Button Examples"),
                ui.input_radio_buttons(
                    "radio2",
                    "Standard Radio Group",
                    ["Selection 1", "Selection 2", "Selection 3"],
                ),
                ui.input_radio_buttons(
                    "radio3",
                    "Inline Radio Group",
                    ["Option 1", "Option 2", "Option 3"],
                    inline=True,
                ),
            ),
            ui.card(
                ui.card_header("Checkbox Examples"),
                ui.input_checkbox_group(
                    "check1",
                    "Standard Checkbox Group",
                    ["Item 1", "Item 2", "Item 3"],
                ),
                ui.input_checkbox_group(
                    "check2",
                    "Inline Checkbox Group",
                    ["Choice A", "Choice B", "Choice C"],
                    inline=True,
                ),
            ),
            ui.card(
                ui.card_header("Select Input Widgets"),
                ui.input_selectize(
                    "select1",
                    "Selectize Input",
                    ["Selection A", "Selection B", "Selection C"],
                ),
                ui.input_select(
                    "select2",
                    "Multiple Select Input",
                    ["Item X", "Item Y", "Item Z"],
                    multiple=True,
                ),
            ),
            ui.card(
                ui.card_header("Text Input Widgets"),
                ui.input_text("text1", "Text Input"),
                ui.input_text_area(
                    "textarea1",
                    "Text Area Input",
                    "Default text content for the text area widget",
                ),
                ui.input_password("password1", "Password Input"),
            ),
            width=300,
            heights_equal=False,
        ),
    ),
    ui.nav_panel(
        "Colors",
        ui.fill.as_fill_item(
            ui.div(
                ui.div(ui.output_ui("ui_colors"), class_="container-sm"),
                class_="overflow-y-auto",
            )
        ),
    ),
    ui.nav_panel(
        "Documentation",
        ui.fill.as_fill_item(
            ui.div(
                ui.div(
                    ui.markdown(
"""
# Brand.yml Demo Application

This application serves as a comprehensive demonstration of color theming and UI components using a [`brand.yml` file](https://posit-dev.github.io/brand-yml/). 
The app showcases how to implement and test different color schemes and UI elements in a Shiny for Python application.

## Technical Details

### Color Implementation

The application sources its colors from a `brand.yml` file, which defines:

- Primary and secondary colors
- Success, warning, and error states
- Background and foreground colors
- Custom color palettes with tints

We use the `brand_yml` package to load the brand data and generate a `ui.Theme` object for consistent theming across the app.
We also implement custom SCSS rules for additional color variant tinting

## Usage

The app serves as both a demonstration and a testing ground for brand color implementations. Use it to:

1. Validate color schemes
2. Test UI component appearances
3. Verify dark mode compatibility
4. Ensure consistent branding across your application
                        """
                    ),
                    class_="container-sm ",
                ),
                class_="overflow-y-auto",
            )
        ),
    ),
    ui.nav_spacer(),
    ui.nav_control(ui.input_dark_mode(id="color_mode")),
    title="brand.yml Demo",
    fillable=True,
    theme=theme,
)


def server(input, output, session):
    @render.plot
    def plot1():
        """
        Generates a sine wave plot using the brand colors.
        The plot adjusts based on user input and color mode.
        """
        colors = {
            "foreground": theme.brand.color.foreground,
            "background": theme.brand.color.background,
            "primary": theme.brand.color.primary,
        }

        if theme.brand.color:
            colors.update(theme.brand.color.to_dict("theme"))

        if input.color_mode() == "dark":
            bg = colors["foreground"]
            fg = colors["background"]
            colors.update({"foreground": fg, "background": bg})

        x = np.linspace(0, input.numeric1(), 100)
        y = np.sin(x) * input.slider1()
        fig, ax = plt.subplots(facecolor=colors["background"])
        ax.plot(x, y, color=colors["primary"])
        ax.set_title("Sine Wave Output", color=colors["foreground"])
        ax.set_facecolor(colors["background"])
        ax.tick_params(colors=colors["foreground"])
        for spine in ax.spines.values():
            spine.set_edgecolor(colors["foreground"])
            spine.set_alpha(0.25)
        return fig

    @render.text
    def out_text1():
        """Returns a simple example function as text output."""
        return "\n".join(
            ["def example_function():", '    return "Function output text"']
        )

    @render.ui
    def ui_colors():
        """
        Generates a UI component displaying all color variations from the brand palette.
        """
        colors = []

        # Show custom tints of the brand colors instead of bootstrap colors.
        for color in brand.color.palette.keys():
            colors += [
                ui.div(
                    ui.div(f"{color}-500", class_=f"p-3 mb-2 position-relative bd-{color}-500"),
                    *[
                        ui.div(f"{color}-{r}", class_=f"p-3 bd-{color}-{r}")
                        for r in [100, 200, 300, 400, 500, 600, 700, 800, 900]
                    ],
                    class_="mb-3",
                )
            ]

        return ui.TagList(
            ui.div(
                *[
                    ui.div(
                        ui.div(
                            color, class_=f"p-3 mb-2 position-relative text-bg-{color}"
                        ),
                        class_="col-md-3 mb-3",
                    )
                    for color in [
                        "primary",
                        "secondary",
                        "dark",
                        "light",
                        "info",
                        "success",
                        "warning",
                        "danger",
                    ]
                ],
                class_="row font-monospace",
            ),
            ui.div(
                *[
                    ui.div(
                        ui.div(color, class_=f"p-3 mb-2 position-relative bd-{color}"),
                        class_="col-md-3 mb-3",
                    )
                    for color in ["black", "white", "foreground", "background"]
                ],
                class_="row font-monospace",
            ),
            ui.layout_column_wrap(*colors, class_="font-monospace"),
        )


app = App(app_ui, server)