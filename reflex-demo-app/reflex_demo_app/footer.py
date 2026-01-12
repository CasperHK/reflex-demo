import reflex as rx


def footer() -> rx.Component:
    """Reusable footer component."""
    return rx.box(
        rx.vstack(
            rx.divider(margin_bottom="20px"),
            rx.grid(
                # Company Info
                rx.vstack(
                    rx.heading("Reflex Demo", size="5", margin_bottom="10px"),
                    rx.text("Building beautiful web apps with Reflex.", size="3", color="gray.600"),
                    spacing="2",
                ),
                # Quick Links
                rx.vstack(
                    rx.heading("Quick Links", size="5", margin_bottom="10px"),
                    rx.link(rx.text("Home", size="3", _hover={"color": "blue.600"}), href="/"),
                    rx.link(rx.text("About", size="3", _hover={"color": "blue.600"}), href="/about"),
                    rx.link(rx.text("Contact", size="3", _hover={"color": "blue.600"}), href="/contact"),
                    spacing="2",
                ),
                # Resources
                rx.vstack(
                    rx.heading("Resources", size="5", margin_bottom="10px"),
                    rx.link(
                        rx.text("Documentation", size="3", _hover={"color": "blue.600"}),
                        href="https://reflex.dev/docs/",
                        is_external=True,
                    ),
                    rx.link(
                        rx.text("GitHub", size="3", _hover={"color": "blue.600"}),
                        href="https://github.com/reflex-dev/reflex",
                        is_external=True,
                    ),
                    rx.link(
                        rx.text("Discord", size="3", _hover={"color": "blue.600"}),
                        href="https://discord.gg/reflex",
                        is_external=True,
                    ),
                    spacing="2",
                ),
                # Legal
                rx.vstack(
                    rx.heading("Legal", size="5", margin_bottom="10px"),
                    rx.link(rx.text("Privacy Policy", size="3", _hover={"color": "blue.600"}), href="#"),
                    rx.link(rx.text("Terms of Service", size="3", _hover={"color": "blue.600"}), href="#"),
                    rx.link(rx.text("Cookie Policy", size="3", _hover={"color": "blue.600"}), href="#"),
                    spacing="2",
                ),
                columns="4",
                spacing="8",
                margin_bottom="20px",
                width="100%",
            ),
            rx.divider(margin_bottom="20px"),
            rx.hstack(
                rx.text("© 2024 Reflex Demo. All rights reserved.", size="3", color="gray.600"),
                rx.spacer(),
                rx.hstack(
                    rx.link(rx.text("Twitter", size="3", _hover={"color": "blue.600"}), href="https://twitter.com", is_external=True),
                    rx.text("|", color="gray.400"),
                    rx.link(rx.text("LinkedIn", size="3", _hover={"color": "blue.600"}), href="https://linkedin.com", is_external=True),
                    rx.text("|", color="gray.400"),
                    rx.link(rx.text("GitHub", size="3", _hover={"color": "blue.600"}), href="https://github.com", is_external=True),
                    spacing="2",
                ),
                width="100%",
            ),
            spacing="0",
            padding="40px 20px",
        ),
        bg="gray.50",
        border_top="1px solid #e2e8f0",
        width="100%",
    )
