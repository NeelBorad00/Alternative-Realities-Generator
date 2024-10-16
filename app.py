from flask import Flask, render_template, request
from models import db, Scenario, Narrative
from transformers import pipeline

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///narratives.db'
db.init_app(app)

def post_process_narrative(narrative):
    # Basic cleanup: Remove excessive repetition
    words = narrative.split()
    seen = set()
    result = []

    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    
    # Join the words back into a cleaned-up narrative
    cleaned_narrative = ' '.join(result)
    
    # Optionally: Trim the output if it's too long
    if len(cleaned_narrative) > 500:
        cleaned_narrative = cleaned_narrative[:500] + "..."
    
    return cleaned_narrative

@app.route('/')
def index():
    scenarios = Scenario.query.all()
    return render_template('index.html', scenarios=scenarios)

@app.route('/generate', methods=['POST'])
def generate():
    scenario_id = request.form['scenario_id']
    scenario = db.session.get(Scenario, scenario_id)

    # Prompt for narrative generation
    prompt = f"If the printing press was invented 500 years earlier, it would revolutionize society by enabling mass communication."

    # Use the GPT model to generate a narrative
    generator = pipeline('text-generation', model='distilgpt2')
    narrative = generator(
        prompt,
        max_length=300,
        num_return_sequences=1,
        temperature=0.8,
        top_k=50
    )[0]['generated_text']

    # Post-process the narrative
    cleaned_narrative = post_process_narrative(narrative)

    # Save cleaned narrative to database (optional)
    new_narrative = Narrative(text=cleaned_narrative)
    db.session.add(new_narrative)
    db.session.commit()  # Save the changes

    return render_template('result.html', narrative=cleaned_narrative)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables if they don't exist
    app.run(debug=True)
