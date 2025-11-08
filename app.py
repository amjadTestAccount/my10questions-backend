from flask import Flask, request, jsonify
from flask_cors import CORS
import replicate
import os
app = Flask(__name__)
CORS(app)
replicate_client = replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])
@app.route("/generate")
def generate():
   prompt = request.args.get("prompt", "")
   output = replicate_client.run(
       "stability-ai/sdxl:latest",
       input={"prompt": prompt}
   )
   return jsonify({"image_url": output[0]})
