# **Historical Alternative Realities Generator**

## **Overview**
The **Historical Alternative Realities Generator** is a web-based application that generates alternative historical narratives using AI. Users can select "What if?" scenarios and receive AI-generated narratives that explore alternative outcomes of historical events.

- **Frontend**: HTML/CSS and Flask templates for user interaction.
- **Backend**: Flask-based web framework that processes user inputs and generates narratives using the DistilGPT2 AI model.
- **Database**: SQLite is used to store predefined scenarios and generated narratives.

## **How It Works**
1. **User selects a historical scenario** from a dropdown list.
2. **AI generates a narrative** based on the selected scenario using a pre-trained language model (DistilGPT2).
3. **The generated narrative is post-processed** to clean up repetition and improve coherence.
4. **The final narrative is displayed** to the user.

## **Features**
- Explore "What if?" historical scenarios.
- AI-generated narratives using the DistilGPT2 model.
- Clean and post-process narratives for readability.
- Simple, intuitive web-based interface.

## **Installation**

### **1. Clone the Repository**
To get started, clone this repository to your local machine:
```bash
git clone https://github.com/your-username/historical-alternative-realities-generator.git
