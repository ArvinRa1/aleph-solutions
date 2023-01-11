import xml.etree.ElementTree as ET
import json

# xml_data = open("Opc.Ua.Di.NodeSet2[32].xml", 'r').read()  # Read file
# print(xml_data.find("NodeId"))
tree = ET.parse("Opc.Ua.Di.NodeSet2[32].xml")
root = tree.getroot()
# print(root)

# for child in root:
    # print(child.attrib.get("BrowseName"))
        # print(child.tag[51:], child.attrib, child.text)
        # for elem in child:
        #     print(elem.tag[51:], elem.text)
classes = {"UADataType": "DataType", "UAObject": "Object", "UAVariable": "Variable", "UAMethod": "Method"}

lsts = []
lsts1 = []
for child in root:
    lst = []
    if child.tag[51:] == "UADataType":
        lst.append(("NodeId: ", child.attrib.get("NodeId"), "NodeClass: ", classes["UADataType"], "BrowseName: ",
                   child.attrib.get("BrowseName")))
        for elem in child:
            if elem.tag[51:] == "DisplayName":
                lst.append(("DisplayName: ", elem.text))
            if elem.tag[51:] == "Description":
                lst.append(("Description: ", elem.text))
        lsts.append(lst)
    lst = []
    if child.attrib.get("BrowseName") == "StateNumber":
        lst.append(("NodeId: ", child.attrib.get("NodeId"), "NodeClass: ", classes["UADataType"], "BrowseName: ",
                   child.attrib.get("BrowseName")))
        for elem in child:
            if elem.tag[51:] == "DisplayName":
                lst.append(("DisplayName: ", elem.text))
            if elem.tag[51:] == "Description":
                lst.append(("Description: ", elem.text))
        lsts1.append(lst)

print(json.dumps(lsts1))


    # elif child.tag[51:] == "UAObject":
    #     print("NodeId: ", child.attrib.get("NodeId"), "NodeClass: ", "Object", "BrowseName: ",
    #           child.attrib.get("BrowseName"))
    #     for elem in child:
    #         if elem.tag[51:] == "DisplayName":
    #             print("DisplayName: ", elem.text)
    #         if elem.tag[51:] == "Description":
    #             print("Description: ", elem.text)

# NodeId
# NodeClass (Variable, DataType, Object, Method, …)
# BrowseName
# DisplayName
# Description

# for child in root:
#     if child.tag == "{http://opcfoundation.org/UA/2011/03/UANodeSet.xsd}UAObject":
#         print(child.tag)

# for child in root:
#     for elem in child:
#         print(elem)

# if child.tag == "UAObject":
#     print(child.tag)
# for child in root:
# print(child.tag, child.attrib)
# import json
# import xmltodict

# open the input xml file and read
# data in form of python dictionary
# using xmltodict module
# with open("Opc.Ua.Di.NodeSet2[32].xml") as xml_file:
#     data_dict = xmltodict.parse(xml_file.read())
# xml_file.close()
# if data_dict['NodeId'] == 'ns=1;i=15001':
# print(type(data_dict))
# generate the object using json.dumps()
# corresponding to json data

# json_data = json.dumps(data_dict)

# Write the json data to output
# json file
# with open("data.json", "w") as json_file:
#     json_file.write(json_data)
# print(child.getchildren())
# print(root.findall("BrowseName"))

# def getNodeId(nodeid):
#     for i in root:
#         if i.get("NodeId") == nodeid:
#             output = i.attrib
#             json_data = json.dumps(output)
#     return json_data
