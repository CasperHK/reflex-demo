"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from .navbar import navbar
from .footer import footer
from .menu import menu

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
            flex="1",
        ),
        footer(),
        width="100%",
        min_height="100vh",
        display="flex",
        flex_direction="column",
    )

def stat_card(title: str, value: str, icon: str, color: str) -> rx.Component:
    """Create a statistics card component."""
    return rx.box(
        rx.vstack(
            rx.text(icon, size="8"),
            rx.text(title, size="3", color="gray.600"),
            rx.text(value, size="6", weight="bold"),
            spacing="2",
            align="center",
            justify="center",
        ),
        padding="20px",
        border_radius="8px",
        border="1px solid #e2e8f0",
        bg="white",
        box_shadow="0 1px 3px rgba(0,0,0,0.1)",
    )

def sidebar() -> rx.Component:
    """Sidebar navigation component."""
    return rx.box(
        menu(),
        width="200px",
        bg="gray.50",
        border_right="1px solid #e2e8f0",
        min_height="100vh",
        display="flex",
        flex_direction="column",
    )

def dashboard() -> rx.Component:
    """Dashboard page with statistics and overview."""
    return rx.vstack(
        navbar(),
        rx.hstack(
            sidebar(),
            rx.container(
                # Header
                rx.vstack(
                    rx.heading("Dashboard", size="9", color="blue.600"),
                    rx.text("Welcome back! Here's an overview of your metrics.", size="4", color="gray.600"),
                    spacing="2",
                    margin_bottom="30px",
                ),
                
                # Statistics Cards Grid
                rx.grid(
                    stat_card("Total Users", "2,847", "👥", "blue"),
                    stat_card("Revenue", "$24,582", "💰", "green"),
                    stat_card("Active Projects", "12", "📊", "purple"),
                    stat_card("Completed Tasks", "156", "✅", "orange"),
                    columns="4",
                    spacing="4",
                    margin_bottom="30px",
                ),
                
                # Charts Section
                rx.vstack(
                    rx.heading("Performance Overview", size="7", color="blue.600", margin_bottom="20px"),
                    rx.grid(
                        # Chart 1
                        rx.box(
                            rx.vstack(
                                rx.heading("Monthly Activity", size="5"),
                                rx.box(
                                    rx.text(
                                        "📈 Activity data would be visualized here with a chart library.",
                                        size="3",
                                        color="gray.600",
                                    ),
                                    padding="40px",
                                    align="center",
                                    justify="center",
                                    bg="gray.50",
                                    border_radius="8px",
                                    height="300px",
                                ),
                                spacing="3",
                            ),
                            padding="20px",
                            border_radius="8px",
                            border="1px solid #e2e8f0",
                            bg="white",
                            width="100%",
                        ),
                        # Chart 2
                        rx.box(
                            rx.vstack(
                                rx.heading("Distribution", size="5"),
                                rx.box(
                                    rx.text(
                                        "🥧 Distribution chart would be displayed here.",
                                        size="3",
                                        color="gray.600",
                                    ),
                                    padding="40px",
                                    align="center",
                                    justify="center",
                                    bg="gray.50",
                                    border_radius="8px",
                                    height="300px",
                                ),
                                spacing="3",
                            ),
                            padding="20px",
                            border_radius="8px",
                            border="1px solid #e2e8f0",
                            bg="white",
                            width="100%",
                        ),
                        columns="2",
                        spacing="4",
                    ),
                    margin_bottom="30px",
                ),
                
                # Recent Activity
                rx.vstack(
                    rx.heading("Recent Activity", size="7", color="blue.600", margin_bottom="20px"),
                    rx.box(
                        rx.vstack(
                            rx.hstack(
                                rx.text("Project Alpha updated", size="4", flex="1"),
                                rx.text("2 hours ago", size="3", color="gray.500"),
                                width="100%",
                            ),
                            rx.hstack(
                                rx.text("New user registered", size="4", flex="1"),
                                rx.text("5 hours ago", size="3", color="gray.500"),
                                width="100%",
                            ),
                            rx.hstack(
                                rx.text("Report generated", size="4", flex="1"),
                                rx.text("1 day ago", size="3", color="gray.500"),
                                width="100%",
                            ),
                            rx.hstack(
                                rx.text("Server maintenance completed", size="4", flex="1"),
                                rx.text("3 days ago", size="3", color="gray.500"),
                                width="100%",
                            ),
                            spacing="3",
                        ),
                        padding="20px",
                        border_radius="8px",
                        border="1px solid #e2e8f0",
                        bg="white",
                    ),
                ),
                
                min_height="85vh",
                padding="30px 0",
                flex="1",
            ),
            width="100%",
            spacing="0",
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
app.add_page(dashboard, route="/dashboard")

def charts() -> rx.Component:
    """Charts page with various chart visualizations."""
    return rx.vstack(
        navbar(),
        rx.hstack(
            sidebar(),
            rx.container(
                # Header
                rx.vstack(
                    rx.heading("Charts & Analytics", size="9", color="blue.600"),
                    rx.text("Visualize your data with interactive charts.", size="4", color="gray.600"),
                    spacing="2",
                    margin_bottom="30px",
                ),
                
                # Charts Grid
                rx.grid(
                    # Line Chart
                    rx.box(
                        rx.vstack(
                            rx.heading("Revenue Trend", size="5"),
                            rx.recharts.line_chart(
                                rx.recharts.line(
                                    data_key="revenue",
                                    stroke="#3b82f6",
                                    stroke_width=2,
                                ),
                                rx.recharts.x_axis(data_key="month"),
                                rx.recharts.y_axis(),
                                rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
                                rx.recharts.tooltip(),
                                data=[
                                    {"month": "Jan", "revenue": 4000},
                                    {"month": "Feb", "revenue": 3000},
                                    {"month": "Mar", "revenue": 2000},
                                    {"month": "Apr", "revenue": 2780},
                                    {"month": "May", "revenue": 1890},
                                    {"month": "Jun", "revenue": 2390},
                                    {"month": "Jul", "revenue": 3490},
                                ],
                                width="100%",
                                height=300,
                            ),
                            spacing="3",
                        ),
                        padding="20px",
                        border_radius="8px",
                        border="1px solid #e2e8f0",
                        bg="white",
                        width="100%",
                    ),
                    # Bar Chart
                    rx.box(
                        rx.vstack(
                            rx.heading("Sales by Category", size="5"),
                            rx.box(
                                rx.vstack(
                                    rx.hstack(
                                        rx.text("Electronics", size="3", flex="1"),
                                        rx.box(bg="blue.400", height="10px", width="60%"),
                                        spacing="2",
                                    ),
                                    rx.hstack(
                                        rx.text("Clothing", size="3", flex="1"),
                                        rx.box(bg="blue.400", height="10px", width="45%"),
                                        spacing="2",
                                    ),
                                    rx.hstack(
                                        rx.text("Home & Garden", size="3", flex="1"),
                                        rx.box(bg="blue.400", height="10px", width="55%"),
                                        spacing="2",
                                    ),
                                    rx.hstack(
                                        rx.text("Sports", size="3", flex="1"),
                                        rx.box(bg="blue.400", height="10px", width="35%"),
                                        spacing="2",
                                    ),
                                    spacing="3",
                                ),
                                padding="30px 20px",
                                bg="gray.50",
                                border_radius="8px",
                                height="300px",
                                width="100%",
                            ),
                            spacing="3",
                        ),
                        padding="20px",
                        border_radius="8px",
                        border="1px solid #e2e8f0",
                        bg="white",
                        width="100%",
                    ),
                    columns="2",
                    spacing="4",
                    margin_bottom="30px",
                ),
                
                # Pie Chart
                rx.box(
                    rx.vstack(
                        rx.heading("Market Share", size="5"),
                        rx.box(
                            rx.vstack(
                                rx.hstack(
                                    rx.box(bg="blue.500", width="16px", height="16px", border_radius="2px"),
                                    rx.text("Product A - 35%", size="3"),
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.box(bg="green.500", width="16px", height="16px", border_radius="2px"),
                                    rx.text("Product B - 28%", size="3"),
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.box(bg="purple.500", width="16px", height="16px", border_radius="2px"),
                                    rx.text("Product C - 20%", size="3"),
                                    spacing="2",
                                ),
                                rx.hstack(
                                    rx.box(bg="orange.500", width="16px", height="16px", border_radius="2px"),
                                    rx.text("Product D - 17%", size="3"),
                                    spacing="2",
                                ),
                                spacing="3",
                            ),
                            padding="40px",
                            align="center",
                            justify="center",
                            bg="gray.50",
                            border_radius="8px",
                            height="300px",
                        ),
                        spacing="3",
                    ),
                    padding="20px",
                    border_radius="8px",
                    border="1px solid #e2e8f0",
                    bg="white",
                    width="100%",
                    margin_bottom="30px",
                ),
                
                min_height="85vh",
                padding="30px 0",
                flex="1",
            ),
            width="100%",
            spacing="0",
        ),
        width="100%",
    )

app.add_page(charts, route="/charts")

def users() -> rx.Component:
    """Users page with user list displayed in a DataTable."""
    user_data = [
        {"id": 1, "name": "John Doe", "email": "john@example.com", "role": "Admin", "status": "Active"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "role": "Manager", "status": "Active"},
        {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "role": "User", "status": "Inactive"},
        {"id": 4, "name": "Alice Williams", "email": "alice@example.com", "role": "User", "status": "Active"},
        {"id": 5, "name": "Charlie Brown", "email": "charlie@example.com", "role": "Moderator", "status": "Active"},
        {"id": 6, "name": "Diana Prince", "email": "diana@example.com", "role": "User", "status": "Active"},
        {"id": 7, "name": "Eve Davis", "email": "eve@example.com", "role": "User", "status": "Inactive"},
        {"id": 8, "name": "Frank Miller", "email": "frank@example.com", "role": "Manager", "status": "Active"},
    ]
    
    return rx.vstack(
        navbar(),
        rx.hstack(
            sidebar(),
            rx.container(
                # Header
                rx.vstack(
                    rx.heading("Users", size="9", color="blue.600"),
                    rx.text("Manage and view all system users.", size="4", color="gray.600"),
                    spacing="2",
                    margin_bottom="30px",
                ),
                
                # Users Table
                rx.box(
                    rx.data_table(
                        data=user_data,
                        columns=["id", "name", "email", "role", "status"],
                        column_headers=["ID", "Name", "Email", "Role", "Status"],
                    ),
                    padding="20px",
                    border_radius="8px",
                    border="1px solid #e2e8f0",
                    bg="white",
                    overflow_x="auto",
                ),
                
                min_height="85vh",
                padding="30px 0",
                flex="1",
            ),
            width="100%",
            spacing="0",
        ),
        width="100%",
    )

app.add_page(users, route="/users")