> [!IMPORTANT]
> 
> This is **not** an official Stanford University project. This is part of a demonstration for STATS 290 regarding branding for Shiny applications.


# Stanford Brand Demo - Shiny for Python

This repository shows an implementation of [Stanford's identity guidelines][suidg] in a [Shiny for Python application][s4py] using the new [`brand.yml` specification][byml] and theming feature introduced in [Shiny for Python v1.2.0](https://github.com/posit-dev/py-shiny/releases/tag/v1.2.0).

You can view the demo in the [Shinylive Playground][slpg].

> [!NOTE]
>
> This demo uses a custom Pyodide wheel to run in the Shinylive Playground for the `libsass` dependency. 

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
| ![Dark Mode](https://github.com/user-attachments/assets/ab90c349-f55f-4c91-94de-3662cf6bf66d) | ![Light Mode](https://github.com/user-attachments/assets/f392008b-afc6-423a-9004-9d4ba3b6030c) |

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
git clone git@github.com:stanford-brand-yml/py-shiny-branded-demo.git
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

The demo can be deploy to:

- [Shinylive Playground][slpg]
- [Shiny Server](https://posit.co/products/open-source/shiny-server/)
- [Posit Connect](https://posit.co/products/enterprise/connect/)

> [!NOTE]
> 
> The `libsass` dependency is not available in the Pyodide environment used
> by Shinylive, so the application is using a custom Pyodide wheel until 
> the Shiny for Python WebAssembly distribution is updated.

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
[slpg]: https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGA+gIwE5QgEwHQCeMANmADRgDGA9hAC5z1Jjx1SIA6EABN9PJx69uAMwCuxYom4cwAZTYQR1DDm4BVCAEsAbnAwBnLXQKyuw7gYAWKutNkLsy1WaHEtEANaCLNgTLArOjoABwNEAHoIgHdYvANFZ3w4HDFXCxEoSjg0ampvAKDQ8KjY6LxM7Nz8vBoYCISnFRx04Tpo4wYMe0DgsMiI9s79Wup6xqVm1t53LxSPHqL+0rjZz3mIUfHKG2piBsTmgFoxbT1DY1MwLi4aYhUfbhCoYjhguEfeSihVDxeegDEAA4AMIARgArJDptxvr9oMQjjgfgVZMCAEwABmxmJhcJwf0R7gA5kFAQAhIEAZgAggAWcl4vKI4kYOAEQF0gAidIAYhCqTDoj8YEdWezAVTeVSQVTcdchLw0HAtMSPgEAby+dqYQlaOq0RC6XSAJx0oG6zwcjXYgDsIJN6JhymJgK5NK59sZCosbJw0TyOEBQK5MrBAFEYWsjmhiGIDWAAdiAGwgylCqzGBOa3m53Mw573I4vOjUQFg20Q8NGmEE4nGF5HP0UsGYumYyM+4QhDDUbIGAwx4hZVGJ9Hh9Fc9Em1zmbgA7gAWWoBJEBFhexUBm4Vn0cG4pcscH3O2waoMAEJuAAeI53ufOOCs6inINPXv9wexkdztAj5+vtI0SZgwc49loMA-Na+KEnOBhwDQuBQdINB7GKbKmEIXR0FoyGiNQxJwWIlCftIhbUMWxClnOHjKNIBhWnOwoYNoECutwdYNoifpzsibH6ChPwEgiSIorwc4kmS3DKqqcC8SiZEfnAA5Dj+EBcCYIQEVgIRWByD60HQ4RzrwRyWC+GDZNIaCnBAmEWLwmQwFoxDWg4FnZNwcjYNuAAKvYwrw0QqqSdjcMAcqYmQ3DtlF3DJti0W2tiAC6JnCAkBCvNIwAQCokHENFXFaJQaWKjI5VmQYHnqjZEB2eljmwC5bnyDVXn6FoIjcP51CBdwwWqlJwCxdFCVxclmJlQ5lgmNl4V5RgBXTQ56VVTV9EEAkcAwI1ojNa5PSLow9yyLwC68io3AwLQ1AGM82Rzr+UDwZ8+3OYdARyO13kQH5AVdrwRgAF4JmCyYhAAHkKIVSbF6WzHARy7kNYVgngEJPUIu5QMJxLGeVTktT031iJZ+5yJ13W9TDqPSONCMeEjKOhdI6NOkIc43Xl91ZB86VE59sjHRA9zRcu0A0NFIK0NVw4GNF3N3Q9cmA5YWigz0YJ0lDtOszF2JYzMHjeOlg36-D5U4AhKhQDhtA9K++iI7OosEWWcEFVIjP67IeARC98FGREsZ9p4RwGPEOiEWryIYKO-uB28Bgh-clDh4ObLnPB+AGNHrTwASYgwG9klhX7AcDsnMTNJB8dRzH6VxwnldBynAaqHX4dZ-oOcN60w4YGqpd0wEidV8HRjEtAdBk3A-exwpY+t9XU8z3PTZwNnKQL2AAC+ZDgPwCDICgdxbvElADuQVCGYwdDMFE3BcnAIhM9JL0npuhiiL2MBeYcVQ0ksC4G4HASGWQ6CuW4C9bgHhuDoBAfgIgxAuBPwAJLbjoLuNkMDpJvC6ANKABAAD8S5iHKjwNwckYg6AHkzNuLQWDdzXTunQrkAAlAAmkQ9c6CNwSDUNgk23BqAiDwFwAAJJgbAOAjjn0MNIAAFHOGCCJpDAnBFCCEZBVFCUJKJeOGigRYhxLooQajGxlw0ZSWkDJzFfGZOhCU85uR8gFA4ohS1nHWgBFKGUcpPEyWHvOLUYS6SeL1BAdUAIjSmnNJEq0Gi7QOnRJ4l0Gj3SejTJ4v0AYVzGNDOCcMnjoyxnjMkzEqZKSePIpRUsGiKxViNJ4zibBuIpBsa2dsJSwJKRUt+dOGjxyTmnFwAAlAAbhuBAJ+ABxRg+g7Zf3uBgbgOgfi4Xtn9fCay4BZCsB-eCG5VlcAAALiAgJQbZ3A1TRKwAweR38I7fFeEo6Rn8nmrPGdwEAc5JEKPCNwFR5VWyYmkM5SGSjgJZmih8+CXyVDRSBJiAApOMzxvBTEQq0FCmFDA4V-gRQosaaKMXpUijivFIE4CEs+SSg26LMUG3BddXF0KaV0uJd-aKWImXpQhNiaQ8KkYkvSuNKlSjBmeC5aKnl3A+XkvKpNSV0rZWIowNFds-LyootZZCqVw507qoZQlHVFgTRCrZVCtV3ARUauRWSucUy5xnLZLPFidrAXTIgHvGZT8ZarI3PQLACRRCnGuVoWg5zLmRtoCclQTyQ0vToO8v86cAK4B+X8oQkiy7RIHNIfNykDBpv-L2V8LqhBureGTHgXV3nFoHNwAAfPFNF0UAQjKnCaTteY8xVr9epWZERuALPucsmBkgE1rI2RgLZUadmyODXQUNdDKDy3gowng+pbl9QgGc-ZOwvXPOPia7+cCeDSKQRq7cObeCSLnQu2W0g7lLMeQol5Lw4Blu5d8n14lq1HsOZI82QQ4UKMvXap9dtF13vSngNAciAQgABae2AcA95HBQ6B2GdA96-L2golCzzEKrpTe8hRVaZrps8JmuRxGT2rIA8IIdvAh1733ofSAGHmBQBCCEPAIQCA3zI-fZgC4AAqDDRAuX3NbbmCQHnKXofuMQxyxF4McJMIBMjcCEBILJ14B5qCqfgHgrgC45CZjsrsnqBBsHxv4yEdw3xtkSOHQuZcq4tApF-mMJ4BAI42YIBEcBsAXPKRDkggOAmhOYQXEsEoER6zYLEGgLYEQtJGDoEiLeWWgvWA8KF0OaAIh0khNkHAmIqR0jgMmSggrMS42RBCdEdIoBoDQJWW0JpbRUjBJQKkWIgRAjQBCMLECYCRZTnpnAsXBPCYBAAGQtMOiCWkMB0LulwEQf8nh2ysO4NAcDpu2B6odmZG3zuQVCPcKBWgMvCZc9QOhsCXN0C4NdrbfBi7CZgduCAIQZl7YC0V2z326E0gE9FNkuB9DRTEFoXb+25soBQadzbdDyRIJmQuAA8mgNg8DsH7jmxxO2UB-P-1J8A2RBniBGbkhAcnABeahSCKh-3R7AYgSiUAoDfq8AX4y8fcBBGySdVPSfmdBzTlh5PkRsA0rucz7Okd4GkzteecvEGyKlUg0XnmFzqAMGIF4rlorBQAOTTuFPQEzHEtBsmudA9T+5afk6F-uDwRhraiO6uD9cHRsGCAXDL-c6utCa9Vzr7nc3+eC7kyLvHC4AAS1BgrnGis4ehTCwFTci1buAtvGfRL84eKwUA9CqbMz7nTt3F1HmeMpjzlmFzhkhuRjiO1TOHmsJng8HgcJsQD7X8ngKVfa7wC1lAGAJDKSUUo3yh3E-e5F0Jn499uCjtkGfb+kcDBXwMLIcZeBJc4BQAwLvSjxlG64M5lASPuBR832qFA0AdB-gwCCiwGvP8oDPDRJ857TiRgDoJA60LcD460IhBQEvw3SyDMp-7R7DgEAvh0AoB+45A-C-4zQOQa7YHf54H4H4Ea4eBwGYEGDuDWw-6yDUFaC0FghIEBAAByxcnUlAXkNB+g3AEBlBLBcUYIYI0UwhSqpBpB5BkBmBEAHB86lAKikAchJUzB5AbByhXB-BUBAA6owWqJ9moXKOIRITNFIZQSgErj+rIJYaodFLIFyJOloXQjLGdtEvQCwRsnGHAKzrIFiO1kcJiGCAEaocYSYSgXgBQbQlgSHjsIoQYDEVYLYQEOSH8BgOuHIAkXwdISwZJvPnAKEWEbwGYVEVgASNQOgLQqWH9CQYUatGAKUVGrYaAbUbIBwrjFGtQpUfGnMhWsDuQM0YUTsNQCVMpKzsALIPjiEDcjSCwRMVMU3t6HYWAJMTciCLMcsfMfGlyLIClMgWEQUYUcUZgZAouhUcELQIoScbQEkbIDSHGjwDQucepGAAcfga8aYagcQhgfvnGDANUQMWQdHp4fGOgNQFCgCSYcLG8PIdwE0eVLUcILIGCkgRCRIRHj4WAOBHXFcHsSYe8RIRrsCXAKCeCfCQiQEMdKuiVAqiiWSQib4YbP0XSbUeifQTbEhGkbSeSdwPiZIUCS8CCbkKSdyRYFCVSVwYKEySKYiWAJFFydKXXhibRH1FKeSbycIOqUUdHviDUYcdqUJCgDjLQYob5PdtAbAbQqfriQSdHhgeYS9qmrIA6SEdaRYJqdwBrjqaieEfiIafssabIJJuAnQjAaEJaS8a6YCXgHaVEdfpgecH+DhDAIod8XGS6aifiQUQUf-tXoAdgHACAcybILoTgPoWOhbvoDic0Rrmgd8XcMXBACgNEDpLqVGV6cyXybUAaUafoIoY8VUdwAAGqbLYBGRWnenCBHEoBXGNk2RPGKFE4QA3FgAvyZASAGHunhGRHHH3FnFVELl0AQBOhqGyD+QQRQQsEbqBwoAYmLlHBYkXkRkTlakRHSHTm7lzn7myCLmSlLGUyIRxw4mwibo3nfmHkRzsmAXjkdlRnbnvnbJ7kXFgUQB0jrEQHKCXkgW3ngXKnQXclTkzmIUQAHkQCYwnnyDESfiYXXnYUQARyUUlp4XkkEUfldHEXIXJjrHaE-CsQxzRRXkDigVgB3nMS8VMUIksUIWflIXCWHm2jrEOH8QYDUWCW0WiRKXiUSHumelCStkmE6WqB+m4y9mtHtGmb9nxqd4RavAn5PkwUfGvnmENHlHSX-H2USGyDOXHmRmQnyCKBxxqBtFlFjq9HynSnjHyAFkIQ3LLmUyvD3E0nkVxXRVN6Sm7HPk8k+UEHR5wXOVEWloZWin1FmW-mFUykQGIzcBBUdE9Evh9FZWkERUrFN7LnNXxreUBBtU8BpUNX4EeCIys65Hxi9W8DunaX6mqB6U2ldmGU9l0FgAgi7jpxCncBWXTY2WaV6mOVRE7AISeBCkoAAQhBTWFGyC7XpxwkKlfT+VCTi5LX7VgkhV1VhUikRXoIMD-zLnvU7SJVLHfX-w9UZWbmTk5VvnnUPWQyHW9EnVhFnX3XeVlVgEVXvyLV7UrW1ViD1WI3hSyCLXDGeQzHkV40jHULrHE2eRrFgDpXuWkH9VMyDV5EjWZUZlZUGU4Aw0OW+lzWKHJXXJZGUHcAln6G2XA0vlwXwTxU4Sgwc0eVgAS3RWXUKkOBRWRqgz83hlM0WARW83THrE60LF60q2rE7FM2i0emg3mHy3XIy2kFsmS0I0034HCzrlaCRYdSS3q0GGa3CBvUfXcAAAaaFftXCQdP1AAWibdjTAC7ZFgzcNUDVleNTNezRlWzUZQGWAEGV3p7YLXocnJtWEVOXGYoWmesVnXQk4QXfpRbbGcGdOZLjbU7WAHGVvlAIrdKYGcGdwDSJLp7S9dyfYa-FAOuQeF3WJg7rnrTnGTAr3R0KWW8P3fsUzVOc8AOB3CnZiYHOvcuSvmvc0H3XZYUe6XPdgqzpFFlSzEEAYCgHAAAI7m7ECs68gvDwTWlZnMo5k6B5nAFTW40H6L0vlC7EAz7X1AMoBZjJmoka4Eg6CN0vkwNKIa4xmYFI6KFI4-FbhWnAU0VnWGRQBMwYARy7SH3kkCXX0YnUDnAiD3DRBHBBbD3USql4nNHv3pSf3f0Fm-0rl9gcH0CwbRpMPZUVAuTAMvRJ6SDgMfUy3QO6BwPm14AIPY0a5dw4CZ7sXPFmAKgLg4704Y4IGmbQ4uYlT8PDpcDSb57OauYmNHgYB6DbiwJU51A9hwC7h-S6Dya95-TkY3KaaQYy4eDEgwKgLqD8JOP6j0DbjqYBN4LAAAAGc2DOsTTOKUSiSWAw2WxgeWOgeAqWVg6WER1A0WsidDJAEQZ+FUWuMCAmlgNg0Q3wW6O4g+h4G2rw8ADuy6DAYaq4Ige4DukGR+se9jwT-CUVbTRkUGVO1mxWdmvkDmNgPAljxj7mqe3AQZOw2gryz8bw+DxAJ+xuC4gaV06C612ufD2yMylTizbmTe1UZM-YcC4zgK1OeC8TnOKCST3uVumYx61sb8BaggXAZkZ52JQTag8EAFUEM6ezZkcgDFA4VuPFAT0Uy6+gvYayjQnTgL1C5aL4oCy6j49GULWLII6mpY-8kGhYBCKmIehyI+Y5w62hamxytOrzsi6OJASTD0ngUAaoju9wuM4+SCFObAoLtyiyymLzGuWu8AST1AaAAAVtFXZohEYNtA7v46PlkL2M2rTs5h5oy1OtVJjq09vpQKSwFnICCHIHINwPPjZXZi1sYIui8DOusiOeq8PgEys6bjy8zmYyws5jY3YwDtJK9oclTgprLN403sutLspCPoE4S7nhPhei06c2wNspHBoMcsYCZgC0uVQsOTQZOv07tfAHs+iFQkGWGiExuK4dvs5vsiAv2FwFSIW1TOuM3Kwv7k47BmgC5JcFwHSFQuGH9HPMGqqwwA7nNtE1q3dNuOgWTFU0Y9c9Go7b5Zo9jWbRYGQ0JWRvg-ckQwEKbUzbuxQ1QzQ3Q8WLQiqYnSw8ytmdHgAbzNkD-o+3gAAWRr2HzlOc3CgDdNbEoowRiQov+yuKrHfsyjhFAt4d+W84Zvoy9UA51q8HHbSulOiRHuYvfsOr80G72dudFMg9FFukYLQOMm9DWvDhgEJvdk3K-E8PdmCLfm9EVZu8yeOu+iplTkYNEkQjXg6R6bx4E57kK4Ch5qQZU4J7jPK6S9uESn5vGu7mstuaK5BgB-PM0Zu2rDuwfi-oRu5bIASxWrgLINIBHohpzgohUCoE+CZzgFld+Ti6+GZ3XpZ-TtZ7RvRo55ifOtia5xZwk9Zw+WkdaUOs0V1G50F9-Kx-geJ5jZYUooF1Z9-HgKWBYSVI6c3bHqfjh7Td1NuaMKsmB4Bz8qzuztYSiGZ6iWgIE+zoChFcZ7iy0FTaiSIHV1CxFV5-ZzsaifFyEIl38mAE1y50gKIMSEsd181657V3vHl-gZDPp0DngLMC+z+nFIV7IfAPIcxxirCdiEbqQeuOzst7x0opDD8gAFSXqUHxA8EYC7fNFvwTcwKLfs4fbxDpYOmlqVA2yrKs4NdOcZo9dU2Hf4FQCQy0evbnfRQED8XfwA8H4RUhdXApRg8zQQ-xBvBX7GBvIODvzcU16hkCFqEKKI+rIGCNe2f0Y7Ho8OSY9ByC58wKJKKA-CXOemeg-NGY84Tpx5lYAwClqArk9bhU9sg09c-Mm573TvzwIM8hBMyRxEmloUeoky-RJY+YEpBqgs9s8jec9o9q8K8a+M8vC6RQBKKYh4DogQh0++i1qerPczIWBUe0FpfBn0fdSpnBm7exdgGaMcIO9LrqwnMF7WX7ixo3KwLT3IMSLXDx-NHup1oBAcA3BgB4DyvDHqOFERV4fhYnOC4RrbIscsHW728eo8CyC8hF9N7IOj1d6yDW4rQzTze8Cu8jBI6e-m0YOGAl9FkJ86fCCcfKb2MaChNjBaRuF0IEj3RoGzvTqQYwaZvPOifLqUvvASdN3sekFPPs7ABlTNFWa1Owjms07D7biaar+gJPO+4MACuabVBGTkYhBQub8zS56QbwLRerKb6vAb-rBbQ++gxPTgAGo9+qdaPIo3XZCMEGIgWQCAAURYYmsKlchnAMxJHAqQ10NAEcHRBPA7oTrWgJvGHA4Qa8SGI4AgO-hIDGS27YQJd3GLQDOysA+AYgPIEYA-UpPLCmgJCAYDpIciCgasiwwgA2Bp+bGhkCugqceAwAMFLykSjcBz6LKaKE1lJQTRZBeqaKJaimjY1qaV1M9rIBgDYDSq0Au3vgQP7Mkk+nqKVjy2WxMJHS7lGRrAwyp0ClGkA2RqIJBoKNXBDAsIgyjPZcCeB+gnAXgJyyLoiBsGGvHGRjDEhyBiA-qNKRoEzRdBt8REDADkSYCAhhgq6sYIRIf9U2kgtwWARR4AMRSbJCFpyUEZXVKu8cIoQPTABlxqh5JWQLhXKFK05acLWyt7RmiyBRKXrZoR3TAB8Q1QylXobUWb4jDT2WFTyoPmUD0AjgSsNbvUNGqs0XBDg6AU4K8HwNPBV1cIggx8GcCnS-g7AbgIybbJQhJAsnHwJiEkMth2DVSrg2SGpCsBGAhYVpWxo5Cg08CLrkak8DrF8UqsJYvrxa6TcOeLXUYYUW0GkMJh9RKYYZFmG3R5hwwt0ksJW5fEdqewBsk2RbKXdAU-FSEdMNyxzCVYVdHkjMgfzVN2chjJRI-iRwkd9A5wcZFxiPi8ZkAbIe+s7nTaRw6AXeUTHfCYDIA0mUQEIHRhyY-B5C3La2CziRzzw6gEQY7AYEDj3k5mtAGUY9jlEqQre6INtpiHkQhABs6IYsP2ypAKiVwjBYkn4TpAoBMQTZF6DAGGx4BgIqCFnEgnZYOig8wACPGVFuwOljsXALbsJn3gpQgAA