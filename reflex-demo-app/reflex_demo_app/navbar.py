import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        # Logo section
        rx.hstack(
            rx.image(
                src="/favicon.ico",
                width="50px",
                height="auto",
            ),
            rx.heading("Reflex Demo App", size="6"),
            spacing="2",
        ),
        # Navigation tags/links
        rx.spacer(),
        rx.hstack(
            rx.link("Home", href="/", color="gray.6", hover_color="blue.600"),
            rx.link("About", href="/about", color="gray.6", hover_color="blue.600"),
            rx.link("Contact", href="/contact", color="gray.6", hover_color="blue.600"),
            rx.link("Docs", href="https://reflex.dev/docs/getting-started/introduction/", is_external=True, color="gray.6", hover_color="blue.600"),
            spacing="4",
        ),
        # Color mode button
        rx.color_mode.button(),
        justify="between",
        padding="16px",
        border_bottom="1px solid #ddd",
        bg="white",
        position="sticky",
        top="0",
        z_index="999",
        width="100%",
        box_shadow="0 2px 4px rgba(0,0,0,0.1)",
    )