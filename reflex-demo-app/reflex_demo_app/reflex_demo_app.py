"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .navbar import navbar


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.color_mode.button(position="top-right"),
        navbar(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9", color="blue.600"),
            rx.text(
                "I'm Casper. Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!", color_scheme="blue"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
            padding="20px",
        ),
        width="100%",
    )


app = rx.App()
app.add_page(index)

def about():
    return rx.vstack(
        navbar(),
        rx.container(
            rx.heading("About Page", size="9", color="blue.600"),
            rx.text("This is the about page.", size="5"),
            rx.box(
                rx.text("Here you can add more information about your application.", size="4"),
                margin_top="20px",
                padding="20px",
                border_radius="8px",
                bg="gray.100",
            ),
            min_height="85vh",
        ),
        width="100%",
    )

def contact():
    return rx.vstack(
        navbar(),
        rx.container(
            rx.heading("Contact Us", size="9", color="blue.600"),
            rx.text("You can reach us at contact@example.com", size="5"),
            rx.hstack(
                rx.link(
                    rx.button("GitHub", color_scheme="gray"),
                    href="https://github.com",
                    is_external=True,
                ),
                rx.link(
                    rx.button("Twitter", color_scheme="blue"),
                    href="https://twitter.com",
                    is_external=True,
                ),
                spacing="4",
                margin_top="20px",
            ),
            min_height="85vh",
        ),
        width="100%",
    )

app.add_page(about)

app.add_page(contact)