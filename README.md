# Sarcasm-Detection-on-Contextual-Embeddings 
Researched on the existing techniques for the sarcasm detection. Comprehending and using them, developed a web-based model for sarcasm detection with accuracy 81.35% 
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Sarcasm detection, is an important step for sentiment analysis because it is not easy to tell the sentence is sarcastic or non sarcastic unlike other sentiment. And also, it is crucial for machine to detect sarcasm for better understanding to serve as an interface for mutual communication between machines and humans. Sarcasm detection is still an unexplored part because not only for machine but sometimes humans are also not able to understand sarcasm. In this study we have tried to understand sarcasm and train the model using LSTM.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
This web-based application predicts a sentence as either sarcastic or non-sarcastic by analyzing and exploiting its linguistic and cognitive features. The model we trained, preprocesses the entered sentence and applies sigmoid function and various gates to generate an output. This output works as an input for next memory cell, and retain it for the longer period of time.
To use, run the streamlit file Prediction.py on the Command Prompt. 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Step-1: Open Command Prompt.
Step-2: Ensure the installation of 'streamlit' library.
Step-3: Use the command "streamlit run Prediction.py" to run the Prediction file directly.
Step-4: The application will open on the default web browser.
Step-5: User is required to enter any sentence and click on the 'Predict' button to check whether the sentence is sarcastic or not.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
This program requires the installation. 
You should install the pyhton-based library 'streamlit'.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

