import pandas as pd
import xml.etree.ElementTree as ET
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table

app = dash.Dash(__name__)

df = pd.read_xml("Opc.Ua.Di.NodeSet2[32].xml")

tree = ET.parse("Opc.Ua.Di.NodeSet2[32].xml")
root = tree.getroot()

df_cols = ["NodeId", "NodeClass", "BrowseName", "DisplayName", "Description"]
rows = []

s_nodeId = None
s_nodeclass = None
s_browsename = None
s_dis = None
s_des = None

for node in root:
    s_nodeclass = node.tag[51:]
    s_nodeId = node.attrib.get("NodeId")
    s_browsename = node.attrib.get("BrowseName")

    for elem in node:
        if elem.tag[51:] == "DisplayName":
            s_dis = elem.text
        if elem.tag[51:] == "Description":
            s_des = elem.text

    if s_nodeclass in ["UADataType", "UAObject", "UAVariable", "UAMethod"]:
        s_nodeclass = s_nodeclass.replace("UA", "")

    rows.append({"NodeId": s_nodeId, "NodeClass": s_nodeclass,
                 "BrowseName": s_browsename, "DisplayName": s_dis, "Description": s_des})

out_df = pd.DataFrame(rows, columns=df_cols)
nameoptions = out_df.BrowseName.dropna()
nameoptions = [{"label": str(i), "value": i} for i in nameoptions.unique()]


def getNodeId(nodeid):
    """
    This function takes in a nodeid argument and returns an XML representation of the result found in the df
    dataframe. The result is found by searching for the NodeId
    column in the dataframe for a value equal to the argument.
    :param nodeid: string
    :return: entire node element as xml
    """
    out = df.loc[df.NodeId == nodeid]
    return out.to_xml()


def getNodeClass(clss):
    """

    :param clss:
    :return:
    """
    out = out_df.loc[out_df.NodeClass == clss]
    return out


def getBrowseName(name):
    out = out_df.loc[out_df.BrowseName == name]
    return out


# -------------------------------------------------------------------------------
app.layout = html.Div([
    html.Div(
        children=[
            html.H2(
                id="banner-title",
                children=[
                    html.A(
                        "Aleph Solutions data engineering assignment",
                        style={
                            "text-decoration": "none",
                            "color": "inherit",
                        },
                    )
                ],
            ),
            html.A(),
        ],
        style={"text-align": "center", "padding": "20px 0px"}
    ),

    html.Div([
        dcc.Markdown('''We are testing get item'''),
        dcc.Markdown('''Please input the nodeId and press enter'''),
        dcc.Input(id="nodeId", type="text", value="ns=1;i=15001",
                  style={'marginRight': '10px'}),

        html.Div([
            html.Div(id="output1"),
        ],
            style={"text-align": "center", "padding": "20px 0px"}, )
    ],
        style={"text-align": "center", "padding": "20px 0px"}),

    html.Div(children=[
        dcc.Markdown('''We are testing get NodeClass'''),
        dcc.Markdown('''Please choose from the dropdown menu'''),
        dcc.Dropdown(
            ['Object', 'Variable', 'Method', 'DataType'],
            value="Object",
            id="nodeclass",

        ),
        html.Div(id="output2"),

    ]),

    html.Div(children=[
        dcc.Markdown('''We are testing get BrowseName'''),
        dcc.Markdown('''Please choose from the dropdown menu'''),
        dcc.Dropdown(
            nameoptions,
            value='Default XML',
            id="name",
        ),
        html.Div(id="output3"),

    ]),

])


@app.callback(
    Output(component_id="output1", component_property="children"),
    [Input(component_id='nodeId', component_property='value'), ])
def getitem(nodeId):
    return getNodeId(nodeId)


#
# ###=========================================================================================
@app.callback(
    Output(component_id='output2', component_property='children'),
    [Input(component_id='nodeclass', component_property='value'), ]
)
def querryforclass(nodeclass):
    tabledf = getNodeClass(nodeclass)
    table = dash_table.DataTable(
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in tabledf.columns
        ],
        style_cell={'textAlign': 'left'},
        data=tabledf.to_dict('records'),
        page_current=0,
        page_size=10,
    )
    return table


@app.callback(
    Output(component_id='output3', component_property='children'),
    [Input(component_id='name', component_property='value'), ]
)
def querryforname(name):
    tabledf = getBrowseName(name)
    table = dash_table.DataTable(
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": True} for i in tabledf.columns
        ],
        style_cell={'textAlign': 'left'},
        data=tabledf.to_dict('records'),
        page_current=0,
        page_size=10,
    )
    return table


# -------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
