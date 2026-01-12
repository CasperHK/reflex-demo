import reflex as rx


def menu() -> rx.Component:
    """Standalone menu navigation component."""
    return rx.vstack(
        # Top menu items
        rx.vstack(
            rx.heading("Menu", size="5", margin_bottom="20px"),
            rx.link(
                rx.text("Dashboard", size="4", _hover={"color": "blue.600"}),
                href="/dashboard",
            ),
            rx.link(
                rx.text("Charts", size="4", _hover={"color": "blue.600"}),
                href="/charts",
            ),
            rx.link(
                rx.text("Users", size="4", _hover={"color": "blue.600"}),
                href="/users",
            ),
            rx.link(
                rx.text("Projects", size="4", _hover={"color": "blue.600"}),
                href="#",
            ),
            rx.link(
                rx.text("Reports", size="4", _hover={"color": "blue.600"}),
                href="#",
            ),
            rx.link(
                rx.text("Settings", size="4", _hover={"color": "blue.600"}),
                href="#",
            ),
            spacing="4",
            flex="1",
        ),
        # Bottom menu items
        rx.vstack(
            rx.divider(margin_bottom="10px"),
            rx.link(
                rx.text("Help", size="4", _hover={"color": "blue.600"}),
                href="#",
            ),
            rx.link(
                rx.text("Logout", size="4", _hover={"color": "red.600"}),
                href="#",
            ),
            spacing="4",
        ),
        spacing="4",
        padding="20px",
        width="100%",
        height="100%",
    )
