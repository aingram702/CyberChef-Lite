from flask import Flask, render_template, request
from operations import OPERATIONS

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    error = ""
    input_text = ""
    pipeline = []
    
    if request.method == "POST":
        input_text = request.form.get("input", "")
        steps = request.form.getlist("step")
        params = request.form.getlist("param")
        
        result = input_text
        try:
            for i, step in enumerate(steps):
                op = step
                func = OPERATIONS.get(op)
                if not func:
                    raise Exception(f"Invalid operation: {op}")

                # Handle optional parameters
                if op == "xor":
                    key = params[i]
                    result = func(result, key)
                elif op == "replace":
                    old, new = params[i].split(',')
                    result = func(result, old, new)
                else:
                    result = func(result)
                pipeline.append((op, params[i] if params[i] else ""))
        except Exception as e:
            error = str(e)
    
    return render_template("index.html", result=result, input_text=input_text, error=error, pipeline=pipeline)

if __name__ == "__main__":
    app.run(debug=True)
