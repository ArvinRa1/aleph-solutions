# aleph-solutions assignment
 casework for aleph-solutions

I would like you to develop a software that will provide a REST API interface to query the attached XML (Opc.Ua.Di.NodeSet2.xml).

 

The XML is made by “node” elements which are identified by “NodeId” field.

There are several type of “node”:

UADataType

UAObject

UAVariable

UAMethod

 

All these kinds of node share common information because they derive from UANode (see XML schema definition referenced by the shared XML file for more details).

 

The API shall expose the following endpoints:

	/item/{node-id}
	Returns the full “node” in the native format i.e. “application/xml”
	/query

The output will be all “node” with the minimum set of information in json format (application/json):

NodeId

NodeClass (Variable, DataType, Object, Method, …)

BrowseName

DisplayName

Description

It allows to return a filtered list of the above output by the following query params :

NodeClass

BrowseName
 

Please share the code in a git repo (preferred) or zip file.

Please present the software in the next interview by running it as docker container (preferred) or by the development tool.

 

Recommended development framework is .NET / C#. If you are not familiar with it, develop with framework / language of your choice.

 

Feel free contact me for any question.

We’ll contact you separately to schedule the next interview.

# Using the apis.py

1) Clone the github repository. 

2) install the requirements file 

	pip install -r requirements.txt

3) Open apis.py in your preferred IDE and run it.

4) copy the link and paste it into your browser

This would run the apis without any frontend. (Not my preferred method)

# Using the app.py (preferred)

1) Clone the github repository. 

2) install the requirements file 

	pip install -r requirements.txt

3) Open app.py in your preferred IDE and run it.

4) copy the link and paste it into your browser

This would run the apis with a frontend. (My preferred method)