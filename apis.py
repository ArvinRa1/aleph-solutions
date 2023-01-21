import pandas as pd
import xml.etree.ElementTree as ET
from flask import Flask, request
from bs4 import BeautifulSoup

app = Flask(__name__)

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

# for node in root:
#     if node.get("NodeId") == "ns=1;i=6548":
#         # print(node)
#         result = ET.tostring(node)


def getNodeId(nodeid):
    """
    This function takes in a nodeid argument and returns an XML representation of the result found in the df
    dataframe. The result is found by searching for the NodeId
    column in the dataframe for a value equal to the argument.
    :param nodeid: string
    :return: entire node element as xml
    """
    out = df.loc[df.NodeId == nodeid]
    return out.to_xml(index=True)
    # return out.to_json(orient="index")


def getNodeClass(clss):
    '''
    :param clss: NodeClass in string type
    :return: DataFrame in json format sliced on that NodeClass
    '''
    out = out_df.loc[out_df.NodeClass == clss]
    return out.to_json(orient="index")


def getBrowseName(name):
    '''
    :param name: BrowseName in String type
    :return: DataFrame in json format sliced on that BrowseName
    '''
    out = out_df.loc[out_df.BrowseName == name]
    return out.to_json(orient="index")


@app.route('/item/<nodeId>')
def get_node_id(nodeId):
    return getNodeId(nodeId)


@app.route('/NodeClass/<class_name>')
def get_nodeclass(class_name):
    return getNodeClass(class_name)


@app.route('/BrowseName/<class_name>')
def get_browsename(class_name):
    return getBrowseName(class_name)


# # -------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(port='5001', debug=True)
