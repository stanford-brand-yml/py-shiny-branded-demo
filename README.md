# Stanford Brand Demo - Shiny for Python

> [!IMPORTANT]
> 
> This is **not** an official Stanford University project. This is part of a demonstration for STATS 290 regarding branding for Shiny applications.

This repository shows an implementation of [Stanford's identity guidelines][suidg] in a [Shiny for Python application][s4py] using the new [`brand.yml` specification][byml] and theming feature introduced in [Shiny for Python v1.2.0](https://github.com/posit-dev/py-shiny/releases/tag/v1.2.0).

> [!NOTE]
>
> This demo currently cannot run in the Shinylive Playground due to a missing Pyodide wheel for the `libsass` dependency. 
> It must be run locally or deployed to a server with full Python support. For more information, see the [Deployment Note](#deployment-note).

## Overview

The demo showcases Stanford's visual identity system through a Shiny for Python application that displays:

- Color palette implementation
- UI component styling
- Dark mode support
- Interactive visualizations using brand colors

The application is modified from the [Brands example](https://github.com/posit-dev/py-shiny/tree/main/examples/brand) in the main [Shiny for Python repository](https://github.com/posit-dev/py-shiny/).

### Requirements

- [Shiny for Python][s4py] >= 1.2.0
- Python >= 3.9
- [`libsass`](https://sass.github.io/libsass-python/) (not available in Shinylive/Pyodide, c.f. [py-shiny#1753](https://github.com/posit-dev/py-shiny/issues/1753))
- Additional data science dependencies listed in [`requirements.txt`](requirements.txt), e.g. `matplotlib`, `numpy`.

### Color Themes

| Dark Mode | Light Mode |
|-----------|------------|
| ![Dark Mode](https://github.com/user-attachments/assets/ab90c349-f55f-4c91-94de-3662cf6bf66d) | ![Light Mode](https://github.com/user-attachments/assets/f392008b-afc6-423a-9004-9d4ba3b6030c
) |

## Repository Structure

The repository structure is as follows:


- `_brand.yml`: Defines Stanford's brand colors, typography, and other visual elements following the [Stanford Identity Guide][suidg]
    - This file is used to configure the brand theming in the Shiny application
- `_colors.scss`: Contains additional SCSS rules for color tinting and UI component styling
   - This file is included to demonstrate how to extend the brand theming with custom styles and see how different color tints
     of the main stanford palette are applied.
- `app.py`: A demo application showcasing the brand implementation in Shiny for Python
    - The application uses the `_brand.yml` file to configure the brand theming
    - It includes interactive visualizations and UI components styled with Stanford's brand colors
- `requirements.txt`: Contains the Python dependencies required to run the application


## Installation

1. Clone the repository:

```bash
git clone https://github.com/stanford-brand-yml/brand-yml
cd py-shiny-branded-demo
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application locally:

```bash
shiny run app.py
```

The app will be available at http://localhost:8000

<img width="2185" alt="Dark Mode with the Branded Shiny App inside of VS Code" src="https://github.com/user-attachments/assets/7f3ee902-8ef9-436d-97f5-255608a0dfa7">

### Deployment Note

While this demo can't run in [Shinylive][shinylive] yet (see [py-shiny#1753](https://github.com/posit-dev/py-shiny/issues/1753)), you can deploy it to:

- Shiny Server
- Posit Connect

## Brand Implementation

The [`_brand.yml` file][byml] defines Stanford's visual identity elements:

- Cardinal Red as primary color
- Cool Grey as secondary color
- Source Sans Pro and Source Serif Pro fonts
- Spacing and layout guidelines
- Custom color variants and tints

Example from `_brand.yml`:

```yaml
color:
  primary: "#8C1515"    # Stanford Cardinal Red
  secondary: "#4D4F53"  # Cool Grey
  success: "#175E54"    # Dark Green
  info: "#006CB8"       # Digital Blue
  warning: "#FFBD3D"    # Sun
  danger: "#820000"     # Dark Cardinal Red
```

## Acknowledgments

- [Stanford University Identity Guide][suidg]
- Shiny for Python team for the brand theming feature

[suidg]: https://identity.stanford.edu/
[s4py]: https://shiny.posit.co/py/
[byml]: https://posit-dev.github.io/brand-yml/
[shinylive]: https://shiny.posit.co/py/docs/shinylive.html
