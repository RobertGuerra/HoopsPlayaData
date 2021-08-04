import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app

layout = html.Div(
    id='about-layout'
)


@app.callback(Output('about-layout', 'children'),
              [Input('url', 'pathname')])
def about_section(*args):

    about_cards = [

        html.Div(
            html.A(
                dbc.Button(
                    'HOME',
                    className="home-button",
                    style={'height': '3em', 'width': '8em', 'background-color': 'blue', 'color': 'white'}
                ),
                href='/apps/start',
                style={"margin": "auto", "textAlign": "center", "align-items": "baseline",
                       "textDecoration": "none", "display": "center"}
            ),
            style={"justifyContent": "center", "display": "flex"}
        ),
        html.Div(
                dbc.Card(
                    [
                        dbc.CardImg(
                            src="../assets/Bobby2_git.png", top=True, bottom=False,
                            style={"position": "relative"}
                        ),

                        # dbc.CardImg(
                        #     src="../assets/chi_op.png", top=False, bottom=True,
                        #     style={
                        #         "background-image": 'url("../assets/chi_op.png")',
                        #         "background-repeat": "no-repeat",
                        #         "display": "block",
                        #         "width": "99vw",
                        #         "height": "25vh",
                        #         "object-fit": "cover",
                        #         "z-index": "0"
                        #     },
                        # ),
                        html.A(
                            dbc.CardBody(
                                [
                                    html.H1("Robert James Guerra",
                                            className='nba',
                                            style={"fontSize": "2rem",
                                                   "position": "relative",})
                                ],
                                style={"textAlignLast": "center", }
                            ),
                            style={"textDecoration": "none", "margin": "auto"},
                            href="https://github.com/RobertJG17",
                            target="blank"
                        ),
                        # dbc.CardImgOverlay(
                        #     children=[
                        #         html.Img(
                        #             src="../assets/chi_op.jpg",
                        #             style={
                        #                 "z-index": "0",
                        #                 "position": "absolute",
                        #                 "padding-bottom": "0px",
                        #                 "padding-top":"67px",
                        #                 "bottom":"-2px",
                        #                 "left":"0px",
                        #                 "width": "99vw",
                        #                 "height": "30vh",
                        #                 "object-fit": "cover",
                        #                 "mix-blend-mode":"hard-light"
                        #             }
                        #         )
                        #     ],
                        # ),
                    ],
                    style={"background-color":"#fc4c49"}
                ),
        ),
        html.Div(
            dbc.Card(
                [
                    dbc.CardImg(
                            src="../assets/rob2_git.png", top=True, bottom=False
                        ),
                    html.A(
                        dbc.CardBody(
                            [
                                html.H1("Roberto Guerra",
                                className='nba',
                                style={"fontSize": "2rem", "z-index":"1"}),
                            ],
                            style={"textAlignLast": "start"},
                        ),
                        style={"textDecoration": "none", "color":"blue", "margin":"auto"},
                        href="https://github.com/RobertGuerra",
                        target="blank"
                    ),

                ],
                style={"background-color": "#8AD"}
            ),
        )

    ]

    return about_cards


