import dash_html_components as html
import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink(
                    html.H1("NBA", className="nba"),
                    href="https://www.nba.com/",
                    target="blank",
                    # style={"paddingTop": "15%"}
                ),

                className="nba-logo-img",
                style={"display": "flex", "align-items": "baseline"}
            ),
            # dbc.NavItem(
            #     dbc.NavLink(
            #         [
            #             html.Img(
            #                 src="https://s3.amazonaws.com/file.imleagues/Images/Teams/Uploaded/201801/201812316271650f5a72e9de44767031d56a47aca3fcadf.png",
            #                 style={"height": "35%", "width": "35%", "padding-right": "1rem"}
            #             ),
            #
            #             dbc.NavLink(
            #                 html.H1("NBA", className="nba"),
            #                 href="https://www.nba.com/",
            #                 target="blank",
            #                 style={"paddingTop":"15%"}
            #             )
            #         ],
            #
            #         className="nba-logo-img",
            #         style={"display": "flex", "align-items": "baseline"}
            #     ),
            # ),

            dbc.NavItem(
                dbc.NavLink(
                    html.H1(
                        "Hoops",
                        #className="nba",
                    ),
                    #href="https://github.com/RobertJG17",
                    # href="#",
                    # target="blank"
                ),
                style={"display": "flex", "align-items": "baseline"}
            ),

            dbc.NavItem(
                dbc.NavLink(
                    html.H1("Draft Results", className="nba"),
                    href="/apps/draft",
                ),
                style={"display": "flex", "align-items": "baseline"}
            ),

            dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem(i, id=i)
                    for i in sorted(
                        ["All Teams", "Atlantic", "Southeast", "Central", "Northwest", "Pacific", "Southwest"]
                    )
                ],
                nav=True,
                label="All Teams",
                id="team-list",
                in_navbar=True,
                className="dropdown",
            ),

            dbc.NavItem(
                dbc.NavLink(
                    html.H1("About", className="nba", style={"fontSize":"1.3rem"}),
                    href="/apps/about",
                ),
                style={"display": "flex", "align-items": "baseline"}
            ),

        ],

        className="navbar",
        fluid=True,
        color="primary",
        sticky=True,
        dark=True
    )


    return navbar




# working navbar
# nav = dbc.NavbarSimple(
#         children=[
#
#             html.Img(
#                 src="https://s3.amazonaws.com/file.imleagues/Images/Teams/Uploaded/201801/201812316271650f5a72e9de44767031d56a47aca3fcadf.png",
#                 style={
#                     "height": "10%",
#                     "width": "10%",
#                     "display": "inline-bock",
#                 }
#             ),
#
#             html.Div(
#                 dbc.NavLink(
#                     html.H1("NBA"),
#                     href="https://www.nba.com/",
#                     target="blank",
#                     className="nba",
#                     style={"padding-right": "30%", "overflow": "hidden", "display": "inline-block"}
#
#                 ),
#             ),
#
#             html.H1(
#                 "TITLE HERE",
#                 style={"padding-left":"200px"}
#             ),
#
#
#             dbc.DropdownMenu(
#                 [
#                     dbc.DropdownMenuItem(i, id=i)
#                     for i in sorted(
#                         ["All Teams", "Atlantic", "Southeast", "Central", "Northwest", "Pacific", "Southwest"]
#                     )
#                 ],
#                 nav=True,
#                 label="Select Division",
#                 id="team-list",
#                 in_navbar=True,
#                 className="dropdown",
#                 style={"padding-left":"300px"}
#             )
#
#         ],
#
#         className="navbar",
#         color="primary",
#         sticky=True,
#         dark=True
#     )
