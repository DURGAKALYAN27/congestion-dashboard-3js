import os
import json
import re  
from flask import Flask, request, render_template, jsonify
from google import genai
from google.genai import types
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

INSTRUCTIONS = """
You are a vision model tasked with extracting a node-link graph from a network diagram image.
Your goal is to identify devices and their connections, and also to infer their operational status.

From the given image, output ONLY a JSON object in this exact format:

{
  "nodes": [
    { "id": "Node1", "status": "healthy" },
    { "id": "Node2", "status": "critical" }
  ],
  "links": [
    { "source": "Node1", "target": "Node2" }
  ]
}

- Each node must have a unique "id". The "id" can be the name or label of the node.
- Each node must have a "status" field, which can be one of three values: "healthy", "warning", or "critical".
- To make the output more realistic, please pick at least a third of the nodes randomly and assign them a "warning" or "critical" status. Assign all other nodes a "healthy" status.
- Each link must indicate connection from "source" to "target".
- Do not include any labels, explanations, or extra formatting. Return valid, minimal JSON only.
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/graph-data')
def get_graph_data():
    try:
        # Read PNG image as bytes
        with open('diagram.png', 'rb') as f:
            img_bytes = f.read()

        # Send inline image with prompt
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                types.Part.from_bytes(
                    data=img_bytes,
                    mime_type="image/png"
                ),
                INSTRUCTIONS
            ]
        )

        print(response.text) # for debugging   
        
        raw_text = response.text
        
        # Use regex to find and extract the JSON object, even if it's wrapped in markdown.
        # This looks for the first '{' and the last '}' and gets everything in between.
        match = re.search(r'\{.*\}', raw_text, re.DOTALL)
        
        # If no JSON object is found in the response, raise an error.
        if not match:
            raise ValueError(f"No valid JSON object found in Gemini response. Raw text: {raw_text}")
            
        # Extract the clean JSON string from the match
        json_str = match.group(0)
        
        # Now, parse the *clean* JSON string
        json_data = json.loads(json_str)
        
        return jsonify(json_data)

    except Exception as e:
        # This will catch any error (file not found, API error, parsing error)
        # and send a clean JSON error to the frontend.
        print(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred on the server.", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

